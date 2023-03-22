# Python re(gex)? exercises

I wrote a TUI application to help you practice Python regular expressions interactively. There are more than 100 exercises covering both the builtin `re` and third-party `regex` module. Most of the exercises from the [Understanding Python re(gex)?](https://github.com/learnbyexample/py_regular_expressions) ebook have been used in this interactive app.

# Installation

This app is available on PyPI as [regexexercises](https://pypi.org/project/regexexercises/). Example installation instructions are shown below, adjust them based on your preferences and OS.

```bash
# virtual environment
$ python3 -m venv textual_apps
$ cd textual_apps
$ source bin/activate
$ pip install regexexercises

# launch the app
$ regexexercises
```

To run the app without having to enter the virtual environment again, add this alias to `.bashrc` (or equivalent):

```bash
# you'll have to change the path
alias regexexercises='/path/to/textual_apps/bin/regexexercises'
```

As an alternative, you can install `textual` (see [Textual documentation](https://textual.textualize.io/getting_started/) for more details), clone my [TUI-apps](https://github.com/learnbyexample/TUI-apps) repository and run the `pyregex_exercises.py` file.

Adjust the terminal dimensions for the widgets to appear properly, for example 84x25 (characters x lines). Here's a sample screenshot:

<p align="center"><img src="https://raw.githubusercontent.com/learnbyexample/TUI-apps/main/PyRegexExercises/pyregex_exercises.png" alt="Sample Python regex exercise" /></p>

# Guide

See [app_guide.md](https://github.com/learnbyexample/TUI-apps/blob/main/PyRegexExercises/app_guide.md)

# Video demo

You can view a demo video about this app on Youtube: [https://youtu.be/0oXPeF8HutQ](https://youtu.be/0oXPeF8HutQ)

# Looking for the tkinter version?

See [this repo commit](https://github.com/learnbyexample/py_regular_expressions/tree/8433b34bd3f03662abac25c754a5ecf871712980/interactive_exercises) for an earlier version written in `tkinter`. That GUI app had 75 questions and supported only `re.search()`, `re.sub()`, `re.findall()` and `re.split()` functions.

