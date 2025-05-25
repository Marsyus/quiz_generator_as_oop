#Import the question class
from question_class import Question
#Create a function that asks user input to generate a question
class NewQuestion(Question):
    def __init__(self, choice_a, choice_b, choice_c, choice_d):
        self.choice_a = choice_a
        self.choice_b = choice_b
        self.choice_c = choice_c
        self.choice_d = choice_d

    def make_question(self):
        self.question = "Question: "
        self.question += input(f"Enter your question: ")
        self.choice_a, self.choice_b, self.choice_c, self.choice_d = "a.) ", "b.) ", "c.) ", "d.) "
        self.choice_a += input(f"Enter choice for letter a: ")
        self.choice_b += input(f"Enter choice for letter b: ")
        self.choice_c += input(f"Enter choice for letter c: ")
        self.choice_d += input(f"Enter choice for letter d: ")
        self.choices = ["a", "b", "c", "d"]
        while True:
            ans = input("Choose a correct answer [a/b/c/d]: ").lower()
            if ans in self.choices:
                self.answer = "Answer: " + ans
                break
            else:
                print("Invalid input. Please try again.")

#Create a function that writes the question in a text file
#Create a function that asks user to continue or not
#Call the functions to run the program
