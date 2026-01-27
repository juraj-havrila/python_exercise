class QuizBrain:
    def __init__(self,question_bank):
        self.question_number = 0
        self.score = 0
        self.question_list = question_bank

    def next_question(self):
            users_answer = input(f" Q.{self.question_number+1}: {self.question_list[self.question_number].text} (True/False): ")
            self.check_answer(users_answer, self.question_list[self.question_number].answer)
            self.question_number += 1


    def still_has_question(self):
        return len(self.question_list) > self.question_number

    def check_answer(self, answer, correct_answer):
        if answer == correct_answer:
            self.score += 1
            print("Correct!")
        else:
            print("Wrong!")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number+1}\n")


