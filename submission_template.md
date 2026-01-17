# AI Code Review Assignment (Python)

## Candidate
- Name: Bantamlak Tilahun
- Approximate time spent: 73 minutes

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- The function incorrectly calculates the average by dividing by the total number of orders, not just the completed ones. It also incorrectly includes orders of any status other than "cancelled," instead of *only* including "completed" orders. The code will crash with a `ZeroDivisionError` for an empty list and a `KeyError` or `TypeError` for invalid order data.

### Edge cases & risks
- The function doesn't safely handle non-list inputs or orders that aren't dictionaries. It assumes the data structure is always perfect.

### Code quality / design issues
- The function lacks a docstring, and variable names like `total` and `count` are too generic and not descriptive.

## 2) Proposed Fixes / Improvements
### Summary of changes
- I rewrote the logic to calculate the average correctly. My changes ensure that I only count orders with a "completed" status and that the total amount is divided by the correct count. I also added comprehensive checks to handle invalid inputs, such as ensuring the input is a list and each order is a well-formed dictionary with a numeric amount. This prevents the function from crashing and ensures accuracy. Finally, I improved the variable names for clarity.

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- I would test with an empty list (`[]`) and `None` to ensure it returns `0.0` without crashing. I would also test with a list containing various order statuses (`completed`, `cancelled`, `pending`) to verify only `completed` orders are counted. Finally, I would include invalid inputs, like non-dictionary items in the list or orders with missing keys, to confirm the error handling works as expected.


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- The explanation is wrong. It claims to exclude "cancelled" orders but fails to mention that it incorrectly includes all other statuses. It also incorrectly states it divides by the "number of orders," which is ambiguous and, in the code's logic, the incorrect denominator.

### Rewritten explanation
- This function calculates the average order value for completed orders. It iterates through a list, summing the amounts of only the orders marked as "completed". It safely handles empty or invalid inputs and avoids division-by-zero errors by returning `0.0` if there are no completed orders.

## 4) Final Judgment
- Decision: Reject
- Justification: The original code is critically flawed. It produces incorrect calculations and is not efficient against common data inconsistencies, leading to crashes.
- Confidence & unknowns: I have high confidence that the corrected code is working as expected.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- The email validation is too simplistic, only checking for "@" symbol, which allows invalid emails. It will crash with a `TypeError` if the input list contains non-string items.

### Edge cases & risks
- The function doesn't handle non-list inputs. An empty list is handled correctly, but the validation logic itself is flawed.

### Code quality / design issues
- The function lacks a docstring. And the validation logic is not correct.

## 2) Proposed Fixes / Improvements
### Summary of changes
- I implemented a strong email validation using a regular expression (regex) to accurately identify valid email formats. I added checks to ensure the input is a list and that each item is a string before attempting validation. This prevents crashes and improves accuracy.

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- I would test with various invalid email formats (e.g. "user.@", "@domain.com", "email.domain.com"), non-string inputs in the list, an empty list, and a non-list input (like `None` or a string) to ensure the function is as expected.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- The original explanation is misleading because it claims the function "safely ignores invalid entries," but it doesn't actually validate emails properly.

### Rewritten explanation
- This function counts the number of validly formatted email addresses in a list. It uses a regular expression to check each email against a standard format and skips any non-string items, ensuring an accurate count.

## 4) Final Judgment
- Decision: Reject
- Justification: The original code's validation logic is fundamentally flawed and unreliable for its purpose.
- Confidence & unknowns: I have a high level of confidence in my assessment.

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- The function incorrectly calculates the average by dividing by the total length of the input list, not the count of valid numbers. It will crash with a `TypeError` if the list contains non-numeric data (like strings). It will crash with a `ZeroDivisionError` if the input list is empty.

### Edge cases & risks
- The function doesn't handle non-list inputs.

### Code quality / design issues
- The function lacks a docstring. And the logic is prone to errors.

## 2) Proposed Fixes / Improvements
### Summary of changes
- I corrected the average calculation by counting only valid numeric (int or float) measurements and dividing by that count. I added a check to prevent division by zero if no valid measurements are found, and added input type checking to handle non-list inputs gracefully.

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- I would test with a mix of valid numbers (ints, floats), `None` values, strings, and other data types. I'd also test with an empty list and a list containing only non-numeric data to ensure the `ZeroDivisionError` is prevented.


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- The explanation is incorrect. It claims to ignore `None` values but doesn't properly handle other invalid types (like strings) and uses the wrong denominator for the average, which makes the result inaccurate.

### Rewritten explanation
- This function calculates the average of a list of measurements. It safely iterates through the list, including only integer and float values in the calculation, and ignores all other data types. It returns `None` if the list is empty or contains no valid numbers.

## 4) Final Judgment
- Decision: Reject
- Justification: The original code is critically flawed. It produces incorrect results and is not safe from crashing on common invalid inputs.
- Confidence & unknowns: I have a high level of confidence in my assessment.
