from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for d in question_data:
    question_bank.append(Question(d['text'], d['answer']))



q = QuizBrain(question_bank)
while q.still_has_questions():
    q.next_question()



print("You have completed the quiz")
print(f"Your final score was: {q.score}/{q.question_number}")
