## This is Python code that outlines the key features of an online calculator and displays these features on a GUI. 

### Here are each of the files and their description:
- calculator.py: Converts an infix mathematical expression to postfix notation using a stack, constructs an expression tree, evaluates the expression, and provides a command-line calculator interface for user input.
- calculatorGUI.py: Creates a GUI-based calculator using Tkinter, allowing users to input mathematical expressions via buttons, evaluate them using a separate calculate function, and display the results in a text entry box. Each button represents an element in an array that is inputted into a grid from a GUI Entry object.
- coins.py: Implements a dynamic programming approach to determine the minimum number of coins needed to make a given amount of change and prints the specific coins used.
- linear.py: Implements linear programming to solve a maximization problem by converting it into a minimization problem and then solving it using SciPy's linprog function with the revised simplex method.
- stack.py: Defines a Stack class with common stack operations (push, pop, peek, size, and isEmpty) and includes a driver program to test its functionality using assertions.
- tree.py: Defines a BinaryTree class for creating and manipulating binary trees and an ExpTree class that extends BinaryTree to construct, traverse (inorder, preorder, postorder), and evaluate expression trees from postfix expressions.

### How to run the main file:

- Simply run "python calculatorGUI.py" and the output should look something like this:
![Screenshot 2025-03-29 at 11 13 54 PM](https://github.com/user-attachments/assets/aadf09bf-edb3-432c-8947-d063f52a55a7)
- From here you can type in any number and perform arithmetic operations on any set of numbers to get your desired results.
