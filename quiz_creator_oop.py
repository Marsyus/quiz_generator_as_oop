#Import the question class
from question_class import Question
#Create a function that asks user input to generate a question
class NewQuestion(Question):
    def __init__(self, choice_a, choice_b, choice_c, choice_d):
        self.choice_a = choice_a
        self.choice_b = choice_b
        self.choice_c = choice_c
        self.choice_d = choice_d
#Create a function that writes the question in a text file
#Create a function that asks user to continue or not
#Call the functions to run the program
