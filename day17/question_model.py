class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def checkAnswer(self, answer):
        if answer == self.answer:
            print("Correct answer!")
        else:
            print