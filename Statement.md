# Project Statement

## ● Problem Statement
Command-line tools often lack simple, accessible mathematical utilities that go beyond elementary arithmetic. Users needing quick computations—such as trigonometric ratios, exponential powers, roots, or logarithms—must frequently rely on graphical applications or heavy software suites. There is a need for a lightweight, dependency-free command-line utility that provides quick access to essential scientific functions within an interactive console environment.

## ● Scope of the Project
The project encompasses the design and implementation of a single-file terminal interface for mathematical operations built with Python's core libraries. 
* **In Scope:** Basic four-operation arithmetic, single-operand trigonometric and logarithmic functions, power/root routines, input validation for division by zero, and continuous interactive loop management.
* **Out of Scope:** Graphical user interfaces (GUI), graphing functionalities, multi-variable calculus, history logging across sessions, and custom memory management registers.

## ● Target Users
* **Students & Learners:** Individuals learning fundamental Python programming concepts such as conditional branches, loops, and built-in modules (`math`).
* **Developers & CLI Enthusiasts:** Users who spend significant time in the terminal and need a fast tool for basic to intermediate mathematical conversions without switching windows.
* **Educators:** Tutors and teachers looking for a clear, real-world example of control flow logic in introductory Python courses.

## ● High-Level Features
* **Interactive CLI Interface:** Formatted menu display with continuous processing until explicit termination (`Exit`).
* **Basic & Advanced Arithmetic:** Support for basic operations (`+`, `-`, `*`, `/`) along with exponentiation (`pow`).
* **Trigonometric Functions:** Direct computation of Sine (`sin`), Cosine (`cos`), and Tangent (`tan`) values in radians.
* **Logarithmic & Exponential Calculations:** Support for natural logarithms (`log`) and exponential functions (`exp`).
* **Root Computations:** Calculations for both square root (`sqrt`) and cube root (`cbrt`).
* **Built-in Error Handling:** Prevention of runtime crashes from invalid input operations or division-by-zero attempts.
