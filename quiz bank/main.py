from data import question_data


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.question_number = 0

    def quiz_questions(self):
        current_question = self.questions[self.question_number]
        self.question_number += 1
        user_answer = input(f"{self.question_number}.{current_question}:(True/False)?")
        self.check_answer(user_answer,current_question['answer'])
    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Right")
            self.score += 1
        else:
            print("wrong")
        print(f'your current score is:{self.score}/{self.question_number}')

    def start_quiz(self):
        while self.question_number < len(self.questions):
            self.quiz_questions()
        print(f'your final score is:{self.score}/{len(self.questions)}')


quiz = Quiz(question_data)
quiz.start_quiz()
