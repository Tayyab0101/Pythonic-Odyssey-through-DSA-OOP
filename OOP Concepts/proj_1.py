#Quiz Game
import random
import string
class Question:
    def __init__(self, text, options, correct_answer):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer

    def display(self):
        print(self.text)
        for i, option in enumerate(self.options):  # Start from 0 auto as enumerate knows what start means
            print(f"{string.ascii_uppercase[i]}. {option}")

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question):
        question.display()
        user_answer = input("Choose A/B/C/D: ").upper()
        if user_answer == question.correct_answer:
            print("Correct Answer!")
            self.score += 1
        else:
            print("Incorrect Answer!")

    def run_quiz(self):
        print("Welcome to Quiz Game")
        random.shuffle(self.questions)
        for i, question in enumerate(self.questions, start=1):
            print("                                                             ")
            print(f"Question {i}:")
            self.display_question(question)
            print(f"Current score is {self.score}/{i}")
        print("Quiz completed!")
        print(f"You answered {self.score} out of {len(self.questions)} questions correctly.")

# Define questions with alphabetic options
questions = [
    Question("Which planet is known as the 'Red Planet'?", ["Venus", "Mars", "Jupiter", "Saturn"], "B"),
    Question("Author of the Harry Potter?", ["J.K. Rowling", "S. King", "G. Martin", "Suzanne Collins"], "A"),
]

quiz = Quiz(questions)
quiz.run_quiz()
