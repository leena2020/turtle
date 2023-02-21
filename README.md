# turtle
A sample turtle interpreter
This implementation creates a TurtleInterpreter class which handles the logic of interpreting the Turtle Graphics Language commands. 
The interpreter maintains a dictionary of turtles and their corresponding turtle commands

When the run method is called with a string of Turtle Graphics code, the interpreter splits the code into lines and executes each line by calling the appropriate method, such as turtle, move, left, right, pen, and color.

In the __main__ block, an example code is provided to create two turtles named "alice" and "bob". "alice" draws a square, while "bob" draws a smaller square inside it and is colored red.
