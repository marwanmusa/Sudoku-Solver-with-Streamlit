# Sudoku Solver web application

[![Python](https://img.shields.io/badge/Python-3.9-3776AB.svg?style=flat&logo=python&logoColor=FFDB4D)](https://www.python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-app-FF4B4B.svg?style=flat)](https://www.streamlit.io)
![GitHub Action CI](https://github.com/jhrcook/streamlit-sudoku/workflows/CI/badge.svg)
[![Heroku](https://img.shields.io/badge/Heroku-undeployed-430098.svg?style=flat&logo=heroku)](https://www.heroku.com)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![jhc github](https://img.shields.io/badge/GitHub-marwanmusa-181717.svg?style=flat&logo=github)](https://github.com/marwanmusa)

**A fast, interactive web application for solving Sudoku puzzles.**
The solver engine is built using the Linear Programming library [Pyomo](https://www.pyomo.org) and the UI is built with [Streamlit](https://www.streamlit.io). Inspired by `jhrcook`.

---

![demo](demo.gif)

# Sudoku
The **Sudoku** is a logic-based combinatorial number-placement puzzle (source: [wikipedia](https://en.wikipedia.org/wiki/Sudoku)). The objective is to fill a $9 \times 9$ grid with digits so that each column, each row, and each of the nine $3 \times 3$ subgrids that compose the grid contain all of the digits from 1 to 9. 

The puzzle setter provides a partially completed grid, which for a well-posed puzzle has a single solution.

Completed games are always an example of a *Latin square* which include an additional constraint on the contents of individual regions.

### Example: Game of the day (22-03-2020)
An example of an instance of the [game of the day](http://www.dailysudoku.com/sudoku/today.shtml) is a s follows:

```
. . . | . 9 4 | 8 . .
. 2 . | . 1 7 | 5 . .
. . 6 | . . . | . 1 .
---------------------
. 6 2 | . . 8 | . . 7
. . . | 3 . 2 | . . .
3 . . | 9 . . | 4 2 .
---------------------
. 9 . | . . . | 6 . .
. . 1 | 7 8 . | . 9 .
. . 3 | 4 5 . | . . .
```

We show next how to solve this puzzle (and any other instance of the game) by using **Integer Linear Programming (ILP)**.

---
## ***To run the app:***

>Open *command prompt / cmd* <br> `streamlit run app.py`

## ***References:***
https://github.com/jhrcook/streamlit-sudoku<br>
https://towardsdatascience.com/solve-sudoku-using-linear-programming-python-pulp-b41b29f479f3<br>
https://github.com/Lakshmi-1212/Sudoku_Solver_LP<br>
https://stackoverflow.com/questions/70218525/how-to-import-a-sudoku-board-in-txt-in-python<br>
https://github.com/techwithtim/Sudoku-GUI-Solver<br>
https://stackoverflow.com/questions/45471152/how-to-create-a-sudoku-puzzle-in-python<br>
https://www.geeksforgeeks.org/reading-writing-text-files-python/<br>
https://docs.streamlit.io/library/api-reference/performance/st.experimental_singleton.clear<br>
https://pyomo.readthedocs.io/en/stable/solving_pyomo_models.html<br>
http://most.ccib.rutgers.edu/glpk.pdf<br>
https://www.britannica.com/science/linear-programming-mathematics<br>
https://github.com/mathcoding/opt4ds/blob/master/aa2020/notebooks/Sudoku.ipynb
