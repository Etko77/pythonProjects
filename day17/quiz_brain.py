from data import question_data
from question_model import Question

question_number = 0


class QuizBrain:
    def __init__(self, q_number, q_list):
        self.q_number = q_number
        self.q_list = q_list
        self.points = 0

    def next_question(self):
        cur_quest = self.q_list[self.q_number]
        return input(f"Question №{self.q_number + 1}: {cur_quest['text']}(True/False):")

    def next_num(self):
        self.q_number = self.q_number + 1

    def check_answer(self, answer):
        question = self.q_list[self.q_number]
        match answer:
            case "True":
                if question['answer'] == answer:
                    print("Correct answer")
                    self.points = self.points + 1
                elif question['answer'] == "False":
                    print("Incorrect answer")
            case "False":
                if question['answer'] == answer:
                    print("Correct answer")
                    self.points = self.points + 1
                elif question['answer'] == "True":
                    print("Incorrect answer")
            case _:
                print("Not a valid answer")


the_quiz = QuizBrain(question_number, question_data)
print(the_quiz.q_list)

for q in question_data:
    quiz_answer = the_quiz.next_question()
    the_quiz.check_answer(quiz_answer)
    the_quiz.next_num()
print(f"Your score is {the_quiz.points}/{len(the_quiz.q_list)} points!")
