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

    def randomize_order(self, count):
        random_order = []
        self.count = len(self.questions)
        while True:
            random_num = random.randint(0, count - 1)
            if random_num not in random_order:
                random_order.append(random_num)
                if len(random_order) == count:
                    return random_order

    def generate_quiz(self, number, order):
        item = order[number]
        print(f"{number + 1}. {self.questions[item]}")
        for each in self.choices[item]:
            print("  " + each)
        while True:
            valid_choices = ("a", "b", "c", "d")
            user_ans = input("\nEnter your answer [a/b/c/d]: ")
            if user_ans in valid_choices:
                if user_ans == self.correct_answers[item]:
                    print("\nYou are correct!")
                    return 1
                else:
                    print("\nSorry, you are incorrect!")
                    return 0
            else:
                print("\nInvalid input. Please try again.")

    def start_quiz(self):
        while True:
            try:
                num = int(input(f"There are {self.count} questions available. How many would you like to answer? : "))
                if self.count >= num >= 0:
                    return num
                else:
                    print("\nInvalid input. Please try again.\n")
            except:
                print("\nInvalid input. Please try again.\n")

    def score(self, points, max_points):
        if points == max_points:
            return "Congrats! You perfectly passed the quiz!"
        elif max_points > points >= max_points / 2:
            return "Congrats! You passed the quiz!"
        elif max_points / 2 > points >= 0:
            return "You did not pass the quiz. Better luck next time!"

    def run(self):
        self.read_file()
        question_count = self.start_quiz()
        order = self.randomize_order(self.count)
        score = 0
        for num in range(question_count):
            print("\n===========")
            print(f"Score: {points}/{question_count}")
            print("===========\n")
            points += self.generate_quiz(num, order)
            