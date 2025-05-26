#Quiz Class
class Quiz:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        with open(self.filename, "r") as file:
            contents = file.readlines()
        
        questions = []
        choices = []
        each_choices = []
        correct_answers = []
        valid = ("a", "b", "c", "d")

        for line in contents:
            line = line.strip()
            if line.startswith("Question"):
                questions.append(line.removeprefix("Question: "))
            elif line.startswith(valid):
                each_choices.append(line)
                if len(each_choices) == 4:
                    choices.append(each_choices)
                    each_choices = []
            elif line.startswith("Answer"):
                correct_answers.append(line.removeprefix("Answer: "))

    def randomize_order(self):
        random_order = []
        while True:
            random_num = random.randint(0, count - 1)
            if random_num not in random_order:
                random_order.append(random_num)
                if len(random_order) == count:
                    break
                