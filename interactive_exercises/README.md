## About

This is a **work-in-progress** GUI app to help you practice Python regular expressions.

The script has been tested for `python3.9` version on Linux.

Currently, only a few questions for `re.search()` function have been added. `flags=re.M` is enabled to differentiate line and string anchors. Here's a screenshot:

<p align="center">
    <img src="./regex_practice_example.png" />
</p>

See [Exercises.md](https://github.com/learnbyexample/py_regular_expressions/blob/master/exercises/Exercises.md) for exercise questions from the **Python re(gex)?** book.

## Instructions

Download [regex_practice.py](https://github.com/learnbyexample/py_regular_expressions/raw/master/interactive_exercises/regex_practice.py) and [questions.json](https://github.com/learnbyexample/py_regular_expressions/raw/master/interactive_exercises/questions.json) or clone this repo as shown below.

```bash
$ git clone --depth=1 https://github.com/learnbyexample/py_regular_expressions

$ cd py_regular_expressions/interactive_exercises/

# use py instead of python3.9 for Windows
$ python3.9 regex_practice.py
```

Your progress will be saved in a new file named `user_progress.json`. If you close the app and launch it again, already solved questions will be automatically skipped.

## TODO

* Add many more questions
* Use `ttk`
* Refactor
* Add tests?
* Etc
