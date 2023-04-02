# author: Jaisuraj Kaleeswaran
# date: March 6, 2023
# file: calculator.py converts an infix expression into postfix and evaluates the expression
# input: Infix expression
# output: Value of the postfix expression

import stack as Stack
import tree as BT

def infix_to_postfix(infix):
    opstack = Stack.Stack() #Initialize opstack
    ans = '' #Initialize the answer string
    opers = ['+', '-', '*', '/', '(', ')', '^'] #Initialize a list of operators
    
    #Initialize a dictionary with precedence of operators
    prec = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    
    #Iterate over enumerate to keep track of the index of each character in infix
    for i, ch in enumerate(infix):
        if ch == '(':
            opstack.push(ch)
        #If ch isn't an operator while the value in infix is and the index is valid
        elif ch not in opers and infix[i+1] in opers if len(infix)-1 > i else True:
            ans += ch + ' ' #Adds the number to the answer with a space
            
        #If ch and value in infix is not an operator, ch isn't a space, and the index is valid
        elif infix[i+1] not in opers and ch not in opers and infix[i+1] != ' ' if len(infix)-1 > i else False:
            ans += ch # Adds the number to the answer without a space
        elif ch == ')':
            while opstack.peek() != '(' and opstack.size() != 0:
                ans += opstack.pop() + ' ' #Add opstack.pop() to ans only if stack can be popped
            opstack.pop()
        else:
            while opstack.peek() != '(' and opstack.size() != 0 and prec[ch] <= prec[opstack.peek()]:
                ans += opstack.pop() + ' ' #Add opstack.pop() and a space to ans
            opstack.push(ch) #Push operator onto opstack
            
    while opstack.size() != 0: #Add opstack.pop() to var ans only if the stack can be popped
        ans += opstack.pop() + ' ' #Add an extra space everytime the while loop holds true
    last_ind = len(ans)-1
    if ans[last_ind] == ' ': #If the last character in the ans string is a space
        ans = ans[:last_ind] #The ans is equal to the ans string without that space
    for i in '()':
        ans = ans.replace(i, '')
    return ans
def calculate(infix):
    postfix_str = infix_to_postfix(infix)
    postfix_str = postfix_str.split()

    #Create an Expression Tree object to store the expression
    tree = BT.ExpTree.make_tree(postfix_str)
    return BT.ExpTree.evaluate(tree) #Returns the evaluated expression

# a driver to test calculate module
if __name__ == '__main__':
    print("Welcome to Calculator Program!")
    while True:
        infix = input("Please enter your expression here. To quit enter 'quit' or 'q':\n")
        if infix == 'quit' or infix == 'q':
            break
        print(calculate(infix))
    print("Goodbye!")