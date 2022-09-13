#Author: Kridtity Ikhlaas Lawang
#Program Name: Calculator 42

#License: GNU GPLv3.0
#Status: Release
#Version: 1.0
#Release Date: 09-13-2022
#Description: Python console calculator using the shunting yard alogrithm

#Copyright (C) 2022 Kridtity Lawang, Licensed to BlackHat IT Pty Ltd

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.

#Import modules
import os
import webbrowser
import re

#Define valid operators and their precedence over others
operators = ("+", "-", "*", "/", "%", "^")
precedence = (2, 2, 1, 1, 1, 0)

#Define list of operations to do using dictionary lookup referencing lambda functions to calulate values
operations = {
    "+": (lambda a, b: a + b),
    "-": (lambda a, b: a - b),
    "*": (lambda a, b: a * b),
    "/": (lambda a, b: a / b),
    "%": (lambda a, b: a % b),
    "^": (lambda a, b: a**b)
}

#Define wait to close function so program does not immediately terminate upon completion when compiled to standalone exceutable
def wait_to_close():
    i = input("")
    quit()

#Define print main menu and options function
def menu():
    print("Calculator 42, Version 1.420.69\n")
    mode = int(
        input("Calculator menu modes:\n"
              "    1: Main calculator\n"
              "    2: Print history to command line\n"
              "    3: Clear history\n"
              "    4: Exit program\n"
              "Choose a mode and enter the number here: "))
    print("")

    return mode

#Define check for 42 function
def check_for_42(value_stack):
    float(value_stack)

    if value_stack == 42:
        print("42! That is the answer to the Ultimate Question of Life, the Universe, and Everything!\n")
    else:
        pass

#Define function to determine precedence of operators over others in the operator stack
def determine_precedence(operator):
    if precedence[operators.index(operator)] <= precedence[operators.index(
            operator_stack[-1])]:
        same_greater_precedence = True
    elif precedence[operators.index(operator)] > precedence[operators.index(
            operator_stack[-1])]:
        same_greater_precedence = False
    else:
        print("Error in determining operator precedence.")

#Define function to print valid operations as part of the menu
def print_operations():
    print("Valid operations and symbols: Addition (+)\n"
          "                              Subtraction (-)\n"
          "                              Multiplication (*)\n"
          "                              Division (/)\n"
          "                              Modulo (%)\n"
          "                              Indices (^)\n"
          "                              Brackets ()\n")

#Initialise main loop (improvised forever loop)
while True:
    #Call menu function to print menu and get mode input
    mode = menu()

    #If mode 1 -> calculate, mode 2 -> print history, mode 3 -> delete history, mode 4 -> exit program
    if mode == 1:
        print_operations()

        #Main calculator algorithm using the Shunting Yard Algorithm to sort the input expression into RPN evaluatable form and evaluate
        #Initialise stacks for the SYA
        operator_stack = []
        value_stack = []

        #Receive input expressions and separate into different tokens using the space between equation terms
        expression = input("Enter equation separating values and operators with spaces: ")
        print("")
        token_stack = expression.split()

        #For every item in the token stack, sort into operator stack (symbols) and value stack (numbers) and evaluate expressions based on the order of operations
        for x in token_stack:
            if x.isdigit() == True:
                value_stack.append(x)
            elif x == "(":
                operator_stack.append(x)
            elif x == ")":
                while operator_stack[-1] != "(":
                    operator = operator_stack.pop()
                    operand1 = float(value_stack.pop())
                    operand2 = float(value_stack.pop())
                    value = operations[operator](operand1, operand2)

                    value_stack.append(value)
                else:
                    operator_stack.pop()
            elif x in operators:
                while len(operator_stack) > 0 and determine_precedence(
                        x) == True:
                    operator = operator_stack.pop()
                    operand1 = float(value_stack.pop())
                    operand2 = float(value_stack.pop())
                    value = operations[operator](operand1, operand2)

                    value_stack.append(value)
                else:
                    operator_stack.append(x)

        #While the operator stack is not empty, pop values from the operator and value stacks and evaluate
        while len(operator_stack) > 0 == False:
            operator = operator_stack.pop()
            operand1 = float(value_stack.pop())
            operand2 = float(value_stack.pop())
            value = operations[operator](operand1, operand2)

            value_stack.append(value)
        else:
            pass

        #When the operator stack is empty and there is one value in the value stack, print the final result and check for the number 42
        if len(operator_stack) <= 0 and len(value_stack) == 1:
            print("Result: {}".format(float(value_stack[-1])))
        else:
            print("Error performing calculation.")
            print(len(value_stack))
            print(len(operator_stack))

        #Append equation and results to text file
        with open('history.txt', 'a') as file:
            file.write("Equation: {}\n".format(expression))
            file.write("Result: {}\n\n".format(value_stack))

        wait_to_close()
    elif mode == 2:
        try:
            #Writes file contents to list
            with open('history.txt', 'r') as file:
                file_lines = file.readlines()

            for line in file_lines:
                line = re.sub(r'\n', '', line)
                line = re.sub(r'\n\n\n', '\n\n', line)

                print(line)
        except Exception as e:
            print(e)
            print("\nThere is either no file named 'history.txt' or previous calculator session or both.")

        wait_to_close()
    elif mode == 3:
        os.remove("history.txt")
        print("History deleted.\n")
        wait_to_close()
    elif mode == 4:
        quit()
    elif mode == 42:
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        wait_to_close()
    elif mode == 69:
        os.system(r'shutdown /s /d u:5:15 /f /t 10 /c "Bonk, no horny. By the way, you have 10 seconds before your computer shuts down. Sucks to be you lol"')
    else:
        print("Number outside range or other invalid input. Please enter a valid input.\n")
        continue