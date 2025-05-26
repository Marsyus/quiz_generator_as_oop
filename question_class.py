#Question Class
class Question:
    #Create a function that asks user input to generate a question
    def make_question(self):
        self.question = "Question: "
        self.question += input(f"Enter your question: ")
        self.choice_a, self.choice_b, self.choice_c, self.choice_d = "a.) ", "b.) ", "c.) ", "d.) "
        self.choice_a += input(f"Enter choice for letter a: ")
        self.choice_b += input(f"Enter choice for letter b: ")
        self.choice_c += input(f"Enter choice for letter c: ")
        self.choice_d += input(f"Enter choice for letter d: ")
        self.valid_choices = ["a", "b", "c", "d"]
        while True:
            ans = input("Choose a correct answer [a/b/c/d]: ").lower()
            if ans in self.valid_choices:
                self.answer = "Answer: " + ans
                break
            else:
                print("Invalid input. Please try again.")

    def compile_choices(self):
        self.choices = [self.choice_a, self.choice_b, self.choice_c, self.choice_d]    
    
    #Create a function that writes the question in a text file
    def make_file(self, filename="quiz.txt"):
        with open(filename, "a") as file:
            file.write(f"{self.question}\n")
            for choice in self.choices:
                file.write(f"{choice}\n")
            file.write(f"{self.answer}\n")
            
