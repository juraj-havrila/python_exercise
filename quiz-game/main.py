from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for item in question_data:
    question_bank.append(Question(item["text"], item["answer"]))

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You finished the Quiz")
print(f"Your final score is:  {quiz.score}/{quiz.question_number}")
