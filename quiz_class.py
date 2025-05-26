import random
#Quiz Class
class Quiz:
    def __init__(self, filename):
        self.filename = filename
        self.questions = []
        self.choices = []
        self.correct_answers = []
    
    def read_file(self):
        with open(self.filename, "r") as file:
            contents = file.readlines()
        
        each_choices = []
        valid = ("a", "b", "c", "d")

        for line in contents:
            line = line.strip()
            if line.startswith("Question"):
                self.questions.append(line.removeprefix("Question: "))
            elif line.startswith(valid):
                each_choices.append(line)
                if len(each_choices) == 4:
                    self.choices.append(each_choices)
                    each_choices = []
            elif line.startswith("Answer"):
                self.correct_answers.append(line.removeprefix("Answer: "))

    def randomize_order(self):
        random_order = []
        count = len(self.questions)
        while True:
            random_num = random.randint(0, count - 1)
            if random_num not in random_order:
                random_order.append(random_num)
                if len(random_order) == count:
                    break
