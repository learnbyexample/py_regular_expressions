import json
import os
import re
import sys
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showwarning, showerror

class Root(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Python Regex Practice')
        self.dimensions()
        self.geometry(self.xy)

        self.styling()

        self.create_question_frame()
        self.create_pattern_frame()
        self.create_replace_frame()
        self.create_flags_frame()
        self.create_format_frame()
        self.create_test_frame()
        self.create_solution_frame()
        self.create_button_frame()

        self.initialize()

    def dimensions(self):
        self.xy = '800x650'
        self.question_width = 82
        self.question_wraplength = 650
        self.entry_width = 53
        self.test_width = 40

    def styling(self):
        ttk.Style().theme_use('alt')

        ttk.Style().configure('QA.TFrame', borderwidth=5, relief='groove')
        ttk.Style().configure('DF.TFrame')

        ttk.Style().configure('QA.TLabel', foreground='#a52a2a')
        ttk.Style().configure('DF.TLabel')
        ttk.Style().configure('LC.TLabel', background='#24ff24')
        ttk.Style().configure('RC.TLabel', background='#ff2424')
        ttk.Style().configure('CS.TLabel', background='#a3ffa3')
        ttk.Style().configure('WS.TLabel', background='#ffa3a3')

    def create_question_frame(self):
        self.question_frame = ttk.Frame(style='QA.TFrame', padding=15)
        self.question_frame.pack(side=tk.TOP, pady=15)

        self.l_question = ttk.Label(self.question_frame, style='QA.TLabel',
                                    justify='left', font='TkFixedFont',
                                    width=self.question_width,
                                    wraplength=self.question_wraplength)
        self.l_question.pack()

    def create_pattern_frame(self):
        self.pattern_frame = ttk.Frame()
        self.pattern_frame.pack(side=tk.TOP, pady=5)

        label = ttk.Label(self.pattern_frame, text='Pattern: ',
                          font='TkFixedFont')
        label.grid(row=0, column=0)

        self.user_pattern = tk.StringVar()
        self.user_pattern.trace_add('write', self.update_display)
        self.e_pattern = ttk.Entry(self.pattern_frame, font='TkFixedFont',
                                   textvariable=self.user_pattern,
                                   width=self.entry_width)
        self.e_pattern.grid(row=0, column=1)

    def create_replace_frame(self):
        self.replace_frame = ttk.Frame()

        label = ttk.Label(self.replace_frame, text='Replace: ',
                          font='TkFixedFont')
        label.grid(row=0, column=0)

        self.user_replace = tk.StringVar()
        self.user_replace.trace_add('write', self.update_display)
        self.e_replace = ttk.Entry(self.replace_frame, font='TkFixedFont',
                                   textvariable=self.user_replace,
                                   width=self.entry_width)
        self.e_replace.grid(row=0, column=1)

    def create_flags_frame(self):
        self.flags_frame = ttk.Frame()
        self.flags_frame.pack(side=tk.TOP, pady=5)

        label = ttk.Label(self.flags_frame, text='   Flags: ',
                          font='TkFixedFont')
        label.grid(row=0, column=0)

        self.flags = (re.I, re.M, re.S, re.A)
        self.user_flags = []
        for idx, flag in enumerate(self.flags, 1):
            var = tk.IntVar(value=0)
            self.user_flags.append(var)
            ttk.Checkbutton(self.flags_frame, text=flag,
                            variable=var, onvalue=int(flag), offvalue=0,
                            command=self.update_display
                           ).grid(row=0, column=idx, padx=5)

    def create_format_frame(self):
        self.format_frame = ttk.Frame()
        self.format_frame.pack(side=tk.TOP, pady=5)

        self.test_string_format = tk.IntVar(value=0)
        ttk.Radiobutton(self.format_frame, text='visual string',
                        variable=self.test_string_format, value=0,
                        command=self.change_format
                       ).pack(side=tk.LEFT)
        ttk.Radiobutton(self.format_frame, text='representation',
                        variable=self.test_string_format, value=1,
                        command=self.change_format
                       ).pack(side=tk.RIGHT)

    def create_test_frame(self):
        self.test_frame = ttk.Frame()
        self.test_frame.pack(pady=5)

    def create_solution_frame(self):
        self.solution_frame = ttk.Frame(padding=5)
        self.solution_frame.pack(pady=5)

        self.l_solution = ttk.Label(self.solution_frame, font='TkFixedFont',
                                    style='QA.TLabel')
        self.l_solution.pack(padx=10, pady=10)

    def create_button_frame(self):
        self.button_frame = ttk.Frame()
        self.button_frame.pack(pady=5)

        buttons = {'Quit': self.quit,
                   'Solution': self.solution,
                   'Previous': lambda: self.next(previous=True),
                   'Next': self.next}

        for t, c in buttons.items():
            ttk.Button(self.button_frame, text=t, command=c
                      ).pack(side=tk.LEFT, padx=2)

    def initialize(self):
        self.format = {0: str, 1: repr}
        self.previous_format = self.test_string_format.get()

        self.progress_file = 'user_progress.json'
        if os.path.isfile(self.progress_file):
            with open(self.progress_file) as f:
                self.user_progress = json.load(f)
        else:
            self.user_progress = {}

        with open('questions.json') as f:
            all_questions = json.load(f)
        self.questions = tuple(v for k, v in all_questions.items())
        self.question_count = len(self.questions)

        self.question_idx = 0
        if len(sys.argv) == 2:
            try:
                self.question_idx = int(sys.argv[1]) - 1
            except ValueError:
                showwarning("Warning!",
                            ("Couldn't convert cli argument to integer!"
                             "\n\nDefault question will be shown"))
            else:
                if self.question_idx < 0:
                    self.question_idx = 0
                elif self.question_idx >= self.question_count:
                    self.question_idx = self.question_count - 1

        self.display_question(self.questions[self.question_idx])
        # skip already answered questions
        # selecting already answered question (via sys.argv[1]) is also skipped!
        for idx in range(self.question_idx, self.question_count):
            progress_key = str(idx)
            if self.user_progress.get(progress_key, ('', '', 0, False))[3]:
                self.next()
            else:
                break

    def display_question(self, question):
        def create_label(s):
            return ttk.Label(self.test_frame, text=s,
                             width=self.test_width, justify=tk.LEFT,
                             anchor='w', font='TkFixedFont',
                             borderwidth=2, relief='raised',
                             padding=10, style='DF.TLabel')

        self.l_question['text'] = f"Q{self.question_idx+1}) {question['question']}"
        self.function = question['function']
        self.ref_solution = question['Reference solution']

        self.replace_frame.pack_forget()
        if self.function == 're.search':
            self.left_col = ('Should match', *question['left column'])
            self.right_col = ('Should NOT match', *question['right column'])
        else:
            if self.function == 're.sub':
                self.replace_frame.pack(after=self.pattern_frame, pady=5)
            self.left_col = ('Input', *question['left column'])
            self.right_col = ('Output', *question['right column'])

        self.l_test_strings = [None] * (len(self.left_col) * 2)
        row = 0
        fmt_func = self.format[self.test_string_format.get()]
        for lc, rc in zip(self.left_col, self.right_col):
            label = create_label(fmt_func(lc))
            label.grid(row=row, column=0)
            if row == 0:
                label['style'] = 'LC.TLabel'
                label['justify'] = tk.CENTER
                label['anchor'] = 'center'
            self.l_test_strings[row * 2] = label

            label = create_label(fmt_func(rc))
            label.grid(row=row, column=1)
            if row == 0:
                if self.function == 're.search':
                    label['style'] = 'RC.TLabel'
                else:
                    label['style'] = 'LC.TLabel'
                label['justify'] = tk.CENTER
                label['anchor'] = 'center'
            self.l_test_strings[row * 2 + 1] = label

            row += 1
        
        progress_key = str(self.question_idx)
        if progress_key in self.user_progress:
            pat, repl, flag_value, _ = self.user_progress[progress_key]
            self.set_flags(flag_value)
            self.user_pattern.set(pat)
            self.user_replace.set(repl)
        else:
            flag_value = int(question['flags'])
            self.set_flags(flag_value)

    def set_flags(self, flag_value):
        for idx, flag in enumerate(self.flags):
            if flag_value & flag:
                self.user_flags[idx].set(int(flag))
            else:
                self.user_flags[idx].set(0)

    def change_format(self):
        new_format = self.test_string_format.get()
        if new_format != self.previous_format:
            self.previous_format = new_format
            fmt_func = self.format[new_format]
            for row, t in enumerate(zip(self.left_col, self.right_col)):
                idx = row * 2
                self.l_test_strings[idx]['text'] = fmt_func(t[0])
                self.l_test_strings[idx + 1]['text'] = fmt_func(t[1])

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

        self.user_pattern.set('')
        self.user_replace.set('')
        self.solution_frame['style'] = 'DF.TFrame'
        for label in self.l_test_strings:
            label.destroy()
        self.l_solution['text'] = ''
        self.display_question(self.questions[self.question_idx])

    def update_display(self, *_):
        try:
            self.flag_value = sum(f.get() for f in self.user_flags)
            pat = re.compile(self.e_pattern.get(), flags=self.flag_value)
        except re.error:
            for label in self.l_test_strings[2:]:
                label['state'] = 'disable'
                label['style'] = 'DF.TLabel'
            return
        else:
            for label in self.l_test_strings[2:]:
                label['state'] = 'normal'
                label['style'] = 'DF.TLabel'
            if pat.pattern == '':
                return

        row = 1
        self.correct_solution = True
        for lc, rc in zip(self.left_col[1:], self.right_col[1:]):
            if self.function == 're.search':
                if pat.search(lc):
                    self.l_test_strings[row * 2]['style'] = 'CS.TLabel'
                else:
                    self.correct_solution = False

                if not pat.search(rc):
                    self.l_test_strings[row * 2 + 1]['style'] = 'WS.TLabel'
                else:
                    self.correct_solution = False
            else:
                try:
                    if self.function == 're.sub':
                        op = pat.sub(self.e_replace.get(), lc)
                    elif self.function == 're.findall':
                        op = str(pat.findall(lc))
                    elif self.function == 're.split':
                        op = str(pat.split(lc))
                except re.error:
                    for label in self.l_test_strings[2:]:
                        label['state'] = 'disable'
                        label['style'] = 'DF.TLabel'
                    return
                else:
                    if op == rc:
                        self.l_test_strings[row * 2]['style'] = 'CS.TLabel'
                        self.l_test_strings[row * 2 + 1]['style'] = 'CS.TLabel'
                    else:
                        self.correct_solution = False

            row += 1

        if self.correct_solution:
            self.solution()

    def save_progress(self):
        progress_key = str(self.question_idx)

        # don't overwrite a correct solution with newer incorrect solution
        if progress_key in self.user_progress:
            if self.user_progress[progress_key][3] and not self.correct_solution:
                return

        pat = self.e_pattern.get()
        repl = self.e_replace.get()
        if pat or repl:
            self.user_progress[progress_key] = (pat,
                                                repl,
                                                self.flag_value,
                                                self.correct_solution)
            with open(self.progress_file, 'w') as f:
                f.write(json.dumps(self.user_progress, indent=4))

    def solution(self):
        self.l_solution['text'] = f'Reference solution(s):\n{self.ref_solution}'
        self.solution_frame['style'] = 'QA.TFrame'
        self.save_progress()

    def quit(self):
        self.save_progress()
        self.destroy()

if __name__ == '__main__':
    if not os.path.isfile('questions.json'):
        showerror("Error!", "questions.json not found!")
    else:
        root = Root()
        root.protocol('WM_DELETE_WINDOW', root.quit)
        root.mainloop()

