# Interview Questions for Data Analyst Practice

These are my personal notes with practice interview questions and short answers.  
I’m keeping them simple and beginner-friendly, just like a student preparing for data analyst roles.

---

## Section 1: SQL Questions

**Q1. What is GROUP BY?**  
GROUP BY is used to group rows that have the same values in specified columns and apply aggregate functions like SUM or COUNT.

**Q2. Difference between WHERE and HAVING?**  
- WHERE filters rows before grouping.  
- HAVING filters groups after using GROUP BY.

**Q3. What is JOIN?**  
JOIN is used to combine rows from two or more tables based on a related column.

**Q4. Types of JOIN?**  
INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN.

**Q5. What is Primary Key?**  
A primary key uniquely identifies each row in a table. It cannot be NULL and must be unique.

---

## Section 2: Python Questions

**Q1. What is pandas?**  
Pandas is a Python library used for working with datasets and dataframes.

**Q2. What is numpy?**  
NumPy is a library for numerical operations and arrays.

**Q3. How to read CSV in Python?**  
Using pandas:  
```python
import pandas as pd
df = pd.read_csv("file.csv")
