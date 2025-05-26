#Import the question class
from question_class import Question

#Inherit the Question class
class NewQuestion(Question):
    ...

#Create a function that asks user to continue or not
def ask_continue():
    while True:
        ans = input("Would you like to continue? [Y/N]: ").upper()
        if ans == "Y":
            return True
        elif ans == "N":
            return False
        else:
            print("Invalid input. Please try again.")

#Call the functions to run the program
while True:
    question = NewQuestion()
    question.make_question()
    question.compile_choices()
    question.make_file()
    if ask_continue():
        continue
    else:
        break
