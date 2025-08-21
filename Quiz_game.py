import tkinter as tk
from tkinter import messagebox

# ----------------- Question Class -----------------
class Question:
    def __init__(self, question_text, options, correct_option):
        self.question_text = question_text
        self.options = options
        self.correct_option = correct_option

# ----------------- Quiz Class -----------------
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.current = 0
        self.score = 0

    def current_question(self):
        if self.current < len(self.questions):
            return self.questions[self.current]
        return None

    def check_answer(self, answer_index):
        question = self.current_question()
        if question and answer_index == question.correct_option:
            self.score += 1
        self.current += 1

# ----------------- GUI Class -----------------
class QuizGUI:
    def __init__(self, quiz):
        self.quiz = quiz
        self.window = tk.Tk()
        self.window.title("Quiz Game")
        self.window.geometry("500x300")

        self.question_label = tk.Label(self.window, text="", wraplength=400, font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.buttons = []
        for i in range(4):
            btn = tk.Button(self.window, text="", width=20, font=("Arial", 12),
                            command=lambda idx=i: self.answer(idx))
            btn.pack(pady=5)
            self.buttons.append(btn)

        self.display_question()
        self.window.mainloop()

    def display_question(self):
        question = self.quiz.current_question()
        if question:
            self.question_label.config(text=question.question_text)
            for i, option in enumerate(question.options):
                self.buttons[i].config(text=option)
        else:
            messagebox.showinfo("Quiz Finished", f"Your final score: {self.quiz.score}/{len(self.quiz.questions)}")
            self.window.destroy()

    def answer(self, index):
        self.quiz.check_answer(index)
        self.display_question()

# ----------------- Main -----------------
if __name__ == "__main__":
    # Create questions
    q1 = Question("What is the capital of France?", ["London", "Paris", "Berlin", "Rome"], 1)
    q2 = Question("What is 5 + 7?", ["10", "11", "12", "13"], 2)
    q3 = Question("Which language is used for AI?", ["Python", "HTML", "CSS", "Java"], 0)

    # Start quiz
    my_quiz = Quiz([q1, q2, q3])
    QuizGUI(my_quiz)
