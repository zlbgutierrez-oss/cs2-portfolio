# Clean Decision Code Makeover: Student Score Checker
**Zeff Lucas B. Gutierrez**
**8-Dahlia**
---
## Activity Overview

In this activity, I improved a Student Score Checker program by applying proper coding standards and
selection structures.
The program accepts a student score from 0 to 100 and determines the appropriate classification.

The classifications are:
| Score | Classification |
|---:|---|
| 90–100 | Outstanding |
| 80–89 | Very Satisfactory |
| 75–79 | Satisfactory |
| 0–74 | Needs Improvement |

Scores below 0 or above 100 are considered invalid.

---
# Part 1 - Analyze the Logic

## Input
What information does the program need?
> The program needs one piece of information: the student's score, entered as a whole number.

## Valid Range
**Minimum valid score:**
> 0

**Maximum valid score:**
> 100

## Possible Outputs
List all possible outputs of the program.
1. Invalid Score.
2. Outstanding
3. Very Satisfactory
4. Satisfactory
5. Needs Improvement

## Boundary Condition
What condition will you use to determine whether the score is valid?
> `score < 0 OR score > 100`. If either of these is true, the score is outside the allowed range and is treated as invalid.

## Multiple Decision Paths
Explain how the program decides which classification should be displayed.
> Once the score passes the validity check, the program compares it against a series of cutoffs starting from the highest (90), then 80, then 75. The first condition that is true determines the classification. If none of the higher cutoffs are met, the score falls into "Needs Improvement" by default.

---
# Part 2 - Flowchart
Create a flowchart showing the logic of your program.
Your flowchart should show:
- Start
- Input score
- Valid score check
- Decision paths
- Classification
- Invalid score
- End

## Flowchart

![Score Checker Flowchart](./score_checker_flowchart.png)

---
# Part 3 - Pseudocode
Create a pseudocode showing the logic of your program.

## Pseudocode  

START
INPUT score
IF score < 0 OR score > 100 THEN
DISPLAY "Invalid Score."
ELSE IF score >= 90 THEN
DISPLAY "Outstanding"
ELSE IF score >= 80 THEN
DISPLAY "Very Satisfactory"
ELSE IF score >= 75 THEN
DISPLAY "Satisfactory"
ELSE
DISPLAY "Needs Improvement"
END

---
# Part 5 - Testing
| Test | Input | Purpose | Expected Output | Actual Output | Result |
|---|---:|---|---|---|---|
| 1 | -1 | Below minimum | Invalid Score. | Invalid Score. | PASS |
| 2 | 0 | Minimum boundary | Needs Improvement | Needs Improvement | PASS |
| 3 | 74 | Below Satisfactory boundary | Needs Improvement | Needs Improvement | PASS |
| 4 | 75 | Satisfactory boundary | Satisfactory | Satisfactory | PASS |
| 5 | 80 | Very Satisfactory boundary | Very Satisfactory | Very Satisfactory | PASS |
| 6 | 90 | Outstanding boundary | Outstanding | Outstanding | PASS |
| 7 | 100 | Maximum boundary | Outstanding | Outstanding | PASS |
| 8 | 101 | Above maximum | Invalid Score. | Invalid Score. | PASS |

---

## Testing Reflection
### 1. Why is it important to test the values 0 and 100?
> These are the exact edges of the valid range. Testing them confirms the program uses inclusive comparisons (`>=` / `<=` logic) so valid boundary scores aren't accidentally rejected.

### 2. Why did you also test -1 and 101?
> These are the first invalid values just outside each edge. Testing them confirms the program correctly rejects scores that are only slightly out of range, not just extreme ones.

### 3. Which test helped you understand boundary conditions the most?
> Testing 74 vs. 75 was the most useful, since it's the exact line between "Needs Improvement" and "Satisfactory" and shows why the order and comparison operators in the elif chain matter.

### 4. Did any of your tests initially fail? If yes, what did you change in your program?
> All tests passed once the range check was placed before the classification checks and the cutoffs were ordered from highest to lowest. Placing the boundary check first, and ordering the elif chain correctly, was what made every test pass.

---

# Reflection
### 1. How did selection structures make the program more useful?
> Selection structures (if/elif/else) let the program respond differently depending on the score instead of always doing the same thing. This makes it possible to handle invalid input and multiple grade levels with a single, organized set of rules.

### 2. How did proper comments and readable formatting improve your program?
> Clear variable names and short comments make it obvious what each block of code is checking, so anyone reading it later (including me) can understand the logic without having to trace through it line by line.

### 3. Why is it useful to plan the program using a flowchart and pseudocode before writing the code?
> Planning first helps catch logic mistakes, like checking cutoffs in the wrong order, before any code is written. It's much faster to fix a diagram or a few lines of pseudocode than to debug code after the fact.






