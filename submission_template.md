# AI Code Review Assignment (Python)

## Candidate
- Name: Bisrat Berhanu Negus
- Approximate time spent:

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- Mathematical Logic Error (Incorrect Denominator): The function divides the sum of non-cancelled orders by the total number of orders (len(orders)). This includes cancelled orders in the average calculation, which mathematically deflates the result.
- ZeroDivisionError: If an empty list [] is passed as an argument, len(orders) is 0, causing the program to crash during the return statement.
- KeyError Vulnerability: The code assumes every item in the list is a dictionary containing "status" and "amount". If a key is missing, it crashes.

### Edge cases & risks
- Input Type Mismatch: The code does not check if orders is actually a list (or iterable). Passing None or a single dictionary would cause a crash.
- Data Type Safety: It assumes "amount" is always a number. If amount is a string (e.g., "10.00") or None, the summation fails.
- All Orders Cancelled: If the list contains orders but all are cancelled, the function returns 0 (which is technically correct but logically relies on the flawed denominator).


### Code quality / design issues
- Variable Misnaming: The variable count is initialized at the top but doesn't track the actual count of items being summed, making the logic confusing.
- Lack of Guard Clauses: There is no early exit for empty inputs or invalid data structures.


## 2) Proposed Fixes / Improvements
### Summary of changes
- Corrected Average Logic: Updated the denominator to use only the count of valid (non-cancelled) orders.
- Input Validation: Added a check isinstance(orders, (list, tuple)) to ensure the input is a valid iterable container, rejecting strings or single objects.
- Data Type Safety: Implemented float() conversion inside a try-except block to handle numeric strings and safely skip items with invalid data types.
- Schema Resilience: Used .get() and isinstance(order, dict) to prevent crashes on malformed data.

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
1. Empty/Null Input: Verify [], None, and () return 0.0 without error.

2. Data Types: Test with amount as integer (10), float (10.5), and string ("10.5").

3. Malformed Data: Include inputs where an item is not a dictionary or is missing the "status" key to ensure the loop skips them safely.

4. Math Accuracy: Test a scenario with 1 valid order ($100) and 1 cancelled order. The result must be 100.0 (100/1), not 50.0 (100/2).

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- Factual Inaccuracy: The claim that it "correctly excludes cancelled orders" is false regarding the denominator. It uses the total count, leading to incorrect math.
- Incomplete: It fails to mention how the function handles empty lists (it crashes) or invalid data types.

### Rewritten explanation
- This function calculates the average value of valid (non-cancelled) orders. It iterates through the input to filter out cancelled orders and invalid data entries. It sums the amounts of the valid orders and divides by the specific count of those orders. The function includes guard clauses to safely handle empty inputs, missing keys, or text-based numbers, preventing runtime errors.

## 4) Final Judgment
- Decision: Reject
- Justification:The original code contains a fundamental mathematical error (incorrect denominator) that invalidates the result. Additionally, it lacks basic error handling for empty inputs, making it unsuitable for production.
- Confidence & unknowns: High. The logic error is definitive. Unknowns include the specific requirement for currency rounding (e.g., to 2 decimal places), the type of input we are accepting(here assumed to be a list or tuple) but returning a standard float is safe for this context.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- 

### Edge cases & risks
- 

### Code quality / design issues
- 

## 2) Proposed Fixes / Improvements
### Summary of changes
- 

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- 

### Rewritten explanation
- 

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- 

### Edge cases & risks
- 

### Code quality / design issues
- 

## 2) Proposed Fixes / Improvements
### Summary of changes
- 

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- 

### Rewritten explanation
- 

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:
