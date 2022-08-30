# Benefits of Functions
- Shorter programs - code can be used over and over
- More robust - less room to make mistakes
Functions are useful when a program needs to repeat a coded process:
- Reuse code for similar task
- Change code in one place.

def make_omelette(ingredient):
"Ingredient" is a parameter.
Parameter - variable name used inside of the function to access input passed to the function.

make_omelette(bacon) -
"Bacon" is an argument, or the value passed to the function. It is an input value, when func is called.

# Local and global variables
Local Variable:
- Variable created in the functions.

Global Variable:
- Variable created in the main body of the program, outside of any functions.
Functions search for variables locally first. If the variable is not in the local scope, it expands the search to the global scope.

# About parentheses after functions
The thing to remember is that when we put parantheses after a function, we're referring to the result of the functions instead of the function itself. When we want to refer to the function itself, we simply use the functions's name without any parantheses or arguments after it.
