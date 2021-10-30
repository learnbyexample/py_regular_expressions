import json
import re
import tkinter as tk

class Root(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Python Regex Practice')
        self.geometry('800x600')

        self.create_question_frame()
        self.create_pattern_frame()
        self.create_format_frame()
        self.create_test_frame()
        self.create_solution_frame()
        self.create_button_frame()

        self.initialize()

    def create_question_frame(self):
        self.question_frame = tk.Frame()
        self.question_frame.pack(side=tk.TOP, pady=5)

        self.l_question = tk.Label(self.question_frame, wraplength=500,
                                   justify='left', fg='#a52a2a',
                                   font='TkFixedFont')
        self.l_question.pack()

    def create_pattern_frame(self):
        self.pattern_frame = tk.Frame()
        self.pattern_frame.pack(side=tk.TOP, pady=5)

        label = tk.Label(self.pattern_frame, text='Search Pattern: ',
                         pady=10, font='TkFixedFont')
        label.pack(side=tk.LEFT)
        self.l_default_bg = label['bg']

        self.user_input = tk.StringVar()
        self.user_input.trace_add('write', self.update_display)
        self.e_pattern = tk.Entry(self.pattern_frame,
                                  textvariable=self.user_input,
                                  width=35, font='TkFixedFont')
        self.e_pattern.pack(side=tk.RIGHT)

    def create_format_frame(self):
        self.format_frame = tk.Frame()
        self.format_frame.pack(side=tk.TOP, pady=5)

        self.test_string_format = tk.IntVar()
        self.test_string_format.set(0)
        tk.Radiobutton(self.format_frame, text='visual string',
                       variable=self.test_string_format, value=0,
                       command=self.change_format
                      ).pack(side=tk.LEFT)
        tk.Radiobutton(self.format_frame, text='representation',
                       variable=self.test_string_format, value=1,
                       command=self.change_format
                      ).pack(side=tk.RIGHT)

    def create_test_frame(self):
        self.test_frame = tk.Frame()
        self.test_frame.pack()

    def create_solution_frame(self):
        self.solution_frame = tk.Frame()
        self.solution_frame.pack()

        self.l_solution = tk.Label(self.solution_frame,
                                   pady=10, font='TkFixedFont')
        self.l_solution.pack()

    def create_button_frame(self):
        self.button_frame = tk.Frame()
        self.button_frame.pack()

        tk.Button(self.button_frame, text='Quit', command=self.quit
                 ).pack(side=tk.LEFT)

        tk.Button(self.button_frame, text='Previous',
                  command=lambda: self.next(previous=True)
                 ).pack(side=tk.LEFT)

        tk.Button(self.button_frame, text='Next', command=self.next
                 ).pack(side=tk.RIGHT)

    def initialize(self):
        self.format = {0: str, 1: repr}
        self.format_change = {0: eval, 1: repr}
        self.previous_format = self.test_string_format.get()

        self.progress_file = 'user_progress.json'
        try:
            with open(self.progress_file) as f:
                self.user_progress = json.load(f)
        except FileNotFoundError:
            self.user_progress = {}

        # todo: handle FileNotFoundError
        with open('questions.json') as f:
            all_questions = json.load(f)
        self.questions = tuple(v for k, v in all_questions.items())
        self.question_idx = 0
        self.question_count = len(self.questions)

        self.display_question(self.questions[self.question_idx])
        # skip already answered questions
        for idx in range(self.question_count):
            progress_key = str(idx)
            if self.user_progress.get(progress_key, ('', False))[1]:
                self.next()
            else:
                break

    def display_question(self, question):
        def create_label(s):
            return tk.Label(self.test_frame, text=s,
                            bg=self.l_default_bg, highlightthickness=1,
                            highlightbackground='black',
                            width=35, justify=tk.LEFT, anchor='w',
                            padx=10, pady=10, font='TkFixedFont')

        self.l_question['text'] = f"Q{self.question_idx+1}) {question['question']}"
        self.should_match = ['Should match', *question['Should match']]
        self.should_not_match = ['Should NOT match', *question['Should NOT match']]
        self.ref_solution = question['Reference solution']

        self.l_test_strings = [None] * (len(self.should_match) * 2)
        row = 0
        fmt_func = self.format[self.test_string_format.get()]
        for sm, snm in zip(self.should_match, self.should_not_match):
            label = create_label(fmt_func(sm))
            label.grid(row=row, column=0)
            if row == 0:
                label['bg'] = '#24ff24'
                label['justify'] = tk.CENTER
                label['anchor'] = 'center'
            self.l_test_strings[row * 2] = label

            label = create_label(fmt_func(snm))
            label.grid(row=row, column=1)
            if row == 0:
                label['bg'] = '#ff2424'
                label['justify'] = tk.CENTER
                label['anchor'] = 'center'
            self.l_test_strings[row * 2 + 1] = label

            row += 1
        
        progress_key = str(self.question_idx)
        if progress_key in self.user_progress:
            user_answer, already_solved = self.user_progress[progress_key]
            self.user_input.set(user_answer)

    def change_format(self):
        new_format = self.test_string_format.get()
        if new_format != self.previous_format:
            self.previous_format = new_format
            for label in self.l_test_strings:
                label['text'] = self.format_change[new_format](label['text'])

    def next(self, previous=False):
        self.save_progress()
        self.correct_solution = False

        if previous:
            if self.question_idx > 0:
                self.question_idx -= 1
            else:
                return
        elif self.question_idx < self.question_count - 1:
            self.question_idx += 1
        else:
            return

        self.user_input.set('')
        for label in self.l_test_strings:
            label.destroy()
        self.l_solution['text'] = ''
        self.display_question(self.questions[self.question_idx])

    def update_display(self, *_):
        try:
            pat = re.compile(self.e_pattern.get(), flags=re.M)
        except re.error:
            for label in self.l_test_strings[2:]:
                label['state'] = 'disable'
                label['bg'] = self.l_default_bg
            return
        else:
            for label in self.l_test_strings[2:]:
                label['state'] = 'normal'
                label['bg'] = self.l_default_bg
            if pat.pattern == '':
                return

        row = 1
        self.correct_solution = True
        for sm, snm in zip(self.should_match[1:], self.should_not_match[1:]):
            if pat.search(sm):
                self.l_test_strings[row * 2]['bg'] = '#a3ffa3'
            else:
                self.correct_solution = False

            if not pat.search(snm):
                self.l_test_strings[row * 2 + 1]['bg'] = '#ffa3a3'
            else:
                self.correct_solution = False

            row += 1

        if self.correct_solution:
            self.l_solution['text'] = f'Reference solution: {self.ref_solution}'
            self.save_progress()

    def save_progress(self):
        progress_key = str(self.question_idx)

        # don't overwrite a correct solution with newer incorrect solution
        if progress_key in self.user_progress:
            if self.user_progress[progress_key][1] and not self.correct_solution:
                return

        if pat := self.e_pattern.get():
            self.user_progress[progress_key] = (pat, self.correct_solution)
            with open(self.progress_file, 'w') as f:
                f.write(json.dumps(self.user_progress, indent=4))

    def quit(self):
        self.save_progress()
        self.destroy()

if __name__ == '__main__':
    root = Root()
    root.protocol('WM_DELETE_WINDOW', root.quit)
    root.mainloop()

