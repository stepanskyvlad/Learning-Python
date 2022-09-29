# Unit Testing
#### Why do we unit test?
- Software bugs hurt the business
- Software testing catches the bugs before the get to the field.
- Need several levels of safety

#### Levels of testing
- **Unit Testing** - Testing at the function level.
- **Component Testing** - Testing is at the library and compiled binary level
- **System Testing** - Tests the external interfaces of a system which is a collection of sub-systems.
- **Performance Testing** - Testing done at sub-system and system levels to verify timing and resource usages are acceptable.

#### Unit testing specifics
- Tests individual functions
- A test should be written for each test case for a function (all positive and negative test cases).
- Groups of tests can be combined into test suites for better organization.
- Executes in the development environment rather than the production environment.
- Execution of the tests should be automated

#### A simple example
```python
import pytest

# Production Code
def str_len(the_str):
    return len(the_str)

# A Unit Test
def test_string_length():
    test_str = "1"  # Setup
    result = str_len(test_str)  # Action
    assert result == 1  # Assert
```

## What is test-driven development?
- A process where the developer takes personal responsibility for the quality of their code.
- Unit tests are written before the production code
- Don't write all the tests or production code at once.
- Tests and production code are both written together in small bits of functionality.

#### Benefits of TDD
- Gives you the confidence to change the code.
- Gives you immediate feedback
- Documents what the code is doing.
- Drives good object oriented design

#### TDD has the following phases in its work flow: 
- Write a failing unit test (the RED phase)
- Write just enough production code to make that test pass (the GREEN phase)
- Refactor the unit test and the production code to make it clean (the REFACTOR phase).
- Repeat until the feature is complete.

#### UNCLE BOB'S 3 LAWS OF TDD:
- You may not write any production code until you have written a failing unit test. 
- You may not write more of a unit test than is sufficient to fail, and not compiling is failing.
- You may not write more production code than is sufficient to pass the currently failing unit test.
## Pytest
#### Pytest Discovery:
- Pytest will automatically discover tests when you execute based on a standard naming convention.
- Test functions should include "test" at the beginning of the function name.
- Classes with tests in them should have "Test" at the beginning of the class name and not have an "__init\__" method.
- Filenames of test modules should start or end with "test". (i.e. test_example.py or example_test.py)
```python
class TestClass:
    def test_me1(self):
        assert True

    def test_me2(self):
        assert True
```
#### XUnit style setup and teardown
XUnit style setup/teardown functions will execute code before and after:
- Test Modules
- Test Functions
- Test Classes
- Test Methods in Test Classes
```python
def setup_module(): pass
def teardown_module(): pass
def setup_functions(): pass
def teardown_functions(): pass
def setup_class(): pass
def teardown_class(): pass
def setup_method(): pass
def teardown_method(): pass
```
Using these setup and teardown functions can help reduce code duplication by letting you specify the setup and teardown
code once at each of the different levels as necessary rather than repeating the code in each individual unit test. 
This can help keep your code clean and manageable.

Example:
```python
def setup_module(module):
    print("Setup Module!")


def teardown_module(module):
    print("Teardown Module")


def setup_function(function):
    if function == test1:
        print("\nSetting up test1!")
    elif function == test2:
        print("\nSetting up test2!")
    else:
        print("\nSettings up unknown test!")


def teardown_function(function):
    if function == test1:
        print("\nTearing down test1")
    elif function == test2:
        print("\nTearing down test2!")
    else:
        print("\nTearing down unknown test!")


def test1():
    print("Executing test1")
    assert True


def test2():
    print("Executing test2")
    assert True
```
Output:
```
test_file1.py::test1 Setup Module!

Setting up test1!
Executing test1
PASSED
Tearing down test1

test_file1.py::test2
Setting up test2!
Executing test2
PASSED
Tearing down test2!
Teardown Module
```
Example:
```python
class TestClass:
    @classmethod
    def setup_class(cls):
        print("Setup TestClass")

    @classmethod
    def teardown_class(cls):
        print("Teardown TestClass")

    def setup_method(self, method):
        if method == self.test1:
            print("\nSetting up test1!")
        elif method == self.test2:
            print("\nSetting up test2!")
        else:
            print("\nSetting up unknown test!")

    def teardown_method(self, method):
        if method == self.test1:
            print("\nTearing down test1!")
        elif method == self.test2:
            print("\nTearing down test2!")
        else:
            print("\nTearing down unknown test!")

    def test1(self):
        print("Executing test1!")
        assert True

    def test2(self):
        print("Executing test2!")
        assert True
```
Output:
```
test_file2.py::TestClass::test1 Setup TestClass

Setting up test1!
Executing test1!
PASSED
Tearing down test1!

test_file2.py::TestClass::test2
Setting up test2!
Executing test2!
PASSED
Tearing down test2!
Teardown TestClass
```
#### Test Fixtures
- Test Fixtures allow for re-use of setup and teardown code across tests.
- The "pytest.fixture" decorator is applied to functions that are decorators.
- Individual unit tests can specify which fixtures they want executed.
- The autouse parameter can be set to true to automatically execute a fixture before each test.
##### Test Fixture Setup:
Example:
```python
import pytest

@pytest.fixture(autouse=True)
def setup():
    print("\nSetup")

def test1():
    print("Executing test1!")
    assert True

def test2():
    print("Executing test2!")
```
Output:
```
test_fixtures.py::test1
Setup
Executing test1!
PASSED
test_fixtures.py::test2
Setup
Executing test2!
PASSED
```
##### Test Fixture Teardown:
- Test Fixtures can each have their own optional teardown code which is called after a fixture goes out of scope.
- There are two methods for specifying teardown code. The "yield" keyword and the request-context object's "addfinalizer" method.
    - Yield:
      - When the "yield" keyword is used the code after the yield is executed after the fixture goes out of scope.
      - The "yield" keyword is a replacement for the return keyword so any return values are also specified in the yield statement.
    - Addfinalizer:
      - With the addfinalizer method a teardown method is defined added via the request-context's addfinalizer method.
      - Multiple finalization functions can be specified.
```python
import pytest

@pytest.fixture()
def setup():
    print("Setup!")
    yield 
    print("Teardown!")
```
```python
import pytest

@pytest.fixture()
def setup(request):
    print("Setup!")
    def teardown():
        print("Teardown!")
    request.addfinalizer(teardown)
```
A practical example
```python
import pytest


@pytest.fixture()
def setup1():
    print("\nSetup 1")
    yield
    print("\nTeardown 1")


@pytest.fixture()
def setup2(request):
    print("\nSetup 2")

    def teardown_a():
        print("\nTeardown A")

    def teardown_b():
        print("\nTeardown B")

    request.addfinalizer(teardown_a)
    request.addfinalizer(teardown_b)


def test1(setup1):
    print("Executing test1!")
    assert True


def test2(setup2):
    print("Executing test2!")
    assert True
```
Output:
```
test_fixtures2.py::test1
Setup 1
Executing test1!
PASSED
Teardown 1

test_fixtures2.py::test2
Setup 2
Executing test2!
PASSED
Teardown B

Teardown A
```
##### Test Fixture Return Objects and Params
- Test Fixtures can optionally return data which can be used in the test.
- The optional "params" array argument in the fixture decorator can be used to specify the data returned to the test.
- When a "params" argument is specified then the test will be called one time with each value specified.

An example:
```python
import pytest

@pytest.fixture(params=[1, 2, 3])
def setup(request):
    retVal = request.param
    print("\nSetup! retVal = {}".format(retVal))
    return retVal


def test1(setup):
    print("\nsetup = {}".format(setup))
    assert True
```
Output:
```
test_fixtures3.py::test1[1]
Setup! retVal = 1

setup = 1
PASSED
test_fixtures3.py::test1[2]
Setup! retVal = 2

setup = 2
PASSED
test_fixtures3.py::test1[3]
Setup! retVal = 3

setup = 3
PASSED
```
#### Assert statements and exceptions
##### Using the assert statement
- Pytest allows the use of the built in python assert statement for performing verifications in a unit test.
- Comparison on all of the python data types can be performed using the standard comparison operators: <, >, <=, >=, ==, and !=
- Pytest expands on the message returned from assert failures to provide more context in the test results. 
```python
def test_int_assert():
    assert 1 == 1

def test_str_assert():
    assert 'str' == 'str'

def test_float_assert():
    assert 1.0 == 1.0

def test_dict_assert():
    assert {"1": 1} == {"1": 1}
```
##### Comparing Floating Point Values
- Validating floating point values can sometimes be difficult as internally the value is a binary fractions (i.e. 1/3 is internally 0.33333333...)
- Because of this some floating point comparisons that would be expected to pass fail.
- The pytest "approx" function can be used to verify that two floating point values are "approximately" equivalent to each other with a default tolerance of le-6.

```python
# Failing Test!!!
from pytest import approx

def test_bad_float_compare():
    assert (0.1 + 0.2) == 0.3

# Passing Test!!!
def test_good_float_compare():
    val = 0.1 + 0.2
    assert val == approx(0.3)
```
##### Verifying Exceptions
- In some cases we want verify that a function throws an exception under certain conditions.
- Pytest provides the "raises" helper to perform this verification using the "with" keyword.
- If the specified exception is not raised in the code block specified after the "raises" line then the test fails.
```python
from pytest import raises

def raisesValueException():
    raise ValueError

def test_exception():
    with raises(ValueError):
        raisesValueException()
```
#### Command line arguments: pytest
##### Specifying what tests should run
- By default PyTest will automatically discover and run all tests in all properly named modules from the current working directory and sub-directories
- There are several command line arguments for controlling which discovered tests actually are executed.
  - moduleName - Simply specify the module name to run only the tests in that module.
  - DirectoryName/ - Runs any tests found in the specified directory.
  - -k "expression" - Matches tests found that match the evaluatable expression in the string. The string values can include module, class and function names (i.e. "TestClass and TestFunction").
  - -m "expression" - Matches tests found that have a "pytest.mark" decorator that matches the specified expression.

##### Useful command line arguments
- -v: Report in verbose mode.
- -q: Run in quiet mode (can be helpful when running hundreds or thousands of tests at once).
- -s : Don't capture console output (show print statements on the console).
- --ignore : Ignore the specified path when discovering tests.
- --maxfail: Stop after the specified number of failures.