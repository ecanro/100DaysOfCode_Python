# TODO 1: asking the questions
# TODO 2: checking if the answer was correct
# TODO 3: checking if we're the end  of the quiz

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import html

question_bank = []
for question in question_data:
    question_text = html.unescape(question["text"])
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():  #->if quiz still  has questions remaining
    quiz.next_question()

print("You completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")