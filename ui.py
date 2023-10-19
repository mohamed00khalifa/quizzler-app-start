from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
GREEN = "	#008000"
RED = "#FF0000"
class Ui:
    def __init__(self, quiz_brian: QuizBrain):
        self.quiz = quiz_brian
        self.window = Tk("quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label()
        self.score_label.config(text="score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(bg="white")
        self.canvas.config(width=300, height=250)
        self.q_text = self.canvas.create_text(150,125,
                                              text="text",
                                              fill=THEME_COLOR,
                                              font=("Arial", 20, "italic"),
                                              width=280
                                              )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.right_path = PhotoImage(file="images/true.png")
        self.right_click = Button()
        self.right_click.config(image=self.right_path, highlightthickness=0, command=self.true_preesed)
        self.right_click.grid(row=2, column=0)
        self.wrong_path = PhotoImage(file="images/false.png")
        self.wrong_click = Button()
        self.wrong_click.config(image=self.wrong_path, highlightthickness=0, command=self.false_pressed)
        self.wrong_click.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            text= self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=text)
        else:
            self.canvas.itemconfig(self.q_text, text="you have finished your quiz.")
            self.right_click.config(state="disabled")
            self.wrong_click.config(state="disabled")
    def true_preesed(self):
        self.give_feedback(self.quiz.check_answer(user_answer="True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer(user_answer="False"))


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
