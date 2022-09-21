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

