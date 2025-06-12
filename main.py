
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    # print(f"{question_data[0]['text']}")
    # print(quiz)
    question_text = question["text"]
    question_answer = question["answer"]

    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    
# print(question_bank[0].text)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()


print("You have completed the quiz")
print(f"your final score was = {quiz.score/quiz.question_number}")


