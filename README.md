# Sudoku Solver web application

[![Python](https://img.shields.io/badge/Python-3.9-3776AB.svg?style=flat&logo=python&logoColor=FFDB4D)](https://www.python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-app-FF4B4B.svg?style=flat)](https://www.streamlit.io)

[![Marwan Musa github](https://img.shields.io/badge/GitHub-marwanmusa-181717.svg?style=flat&logo=github)](https://github.com/marwanmusa)

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
