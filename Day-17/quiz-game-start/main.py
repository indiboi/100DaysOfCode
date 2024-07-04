from question_model import Question
from data import question_data
from quiz_brain import QuestionBrain

question_bank = []

for i in question_data:
    question_text = i["text"]
    answer_text = i["answer"]
    new_question = Question(q_text=question_text, q_answer=answer_text)
    question_bank.append(new_question)

quiz = QuestionBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
