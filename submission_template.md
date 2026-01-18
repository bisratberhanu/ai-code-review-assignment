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
- Confidence & unknowns: **High**. The logic error is definitive. Unknowns include the specific requirement for currency rounding (e.g., to 2 decimal places), the type of input we are accepting(here assumed to be a list or tuple) but returning a standard float is safe for this context.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- Incorrect Validation Logic: The condition if "@" in email is insufficient. It generates false positives for invalid strings like "@", "name@", "@domain.com", or "not an email". It fails to ensure the basic structure of an email (local part, domain, TLD).
- TypeError Vulnerability: The code assumes every item in the list is a string. If the list contains None, integers, or dictionaries, the expression "@" in email will raise a TypeError and crash the program.

### Edge cases & risks
- Input Type Mismatch: If emails is None or a non-iterable type (e.g., an integer), the loop will throw a TypeError.
- Formatting Issues: The code (as written) counts strings with spaces (e.g., "user name@domain.com") or multiple @ signs (e.g., "user@@domain.com") as valid, which are technically invalid for standard email use.
- Empty Strings: While empty strings don't crash the original code, they are part of a larger category of "invalid text" that the logic fails to filter meaningfully.

### Code quality / design issues
- Over-simplification: Relying solely on in membership for structural validation is poor engineering practice for data processing tasks.
- Lack of Defensive Coding: No checks exist to verify the input is a list or that its contents are strings.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Standardized Validation: Replaced the simple substring check with the re (Regular Expression) library to enforce a standard structure (user@domain.tld).
- Input Validation: Added a guard clause isinstance(emails, (list, tuple)) to ensure the input is a valid container. so the iteration won't crash on non-iterables.
- Type Safety: Added a check isinstance(email, str) inside the loop to safely skip None, numbers, or other non-string types without crashing.

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- Structure compliance: Test inputs that mimic emails but are wrong, such as "missing_domain@", "@missing_user.com", and "user name@domain.com" (spaces).
- Mixed Data Types: Pass a list ["user@email.com", None, 123, {}] to ensure the function skips non-strings gracefully.
- Boundary Checks: Test empty lists [] and None input to verify the function returns 0.
- False Positives: Test strings like "user@domain" (missing TLD) to ensure the regex catches missing parts.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- Factual Inaccuracy: The code does not "safely ignore invalid entries"; it crashes on non-string types.
- Misleading: It claims to count "valid" emails, but its definition of validity ("contains @") is technically incorrect and insufficient for any real-world application.

### Rewritten explanation
- This function counts the number of valid email addresses in a list by verifying that each entry is a string matching a standard email pattern (e.g., user@domain.com). It uses regular expressions to ensure the email contains a local part, a domain, and a top-level domain, while rejecting entries with spaces or missing components. The function implies type checking to safely skip non-string items (like None or numbers) and handles empty or invalid input lists gracefully.
- **For more information check task 2 explanation part in [NOTES.md](NOTES.md) file**.
## 4) Final Judgment
- Decision: Reject
- Justification: The logic for determining a "valid email" is fundamentally flawed and too permissive, leading to corrupted data downstream. Additionally, the lack of type safety means the code is prone to runtime crashes when processing real-world messy data.
- Confidence & unknowns:  **High**. While email validation can be much more complex (RFC 5322), the original code fails even the most basic standard. The proposed regex is a standard "safe enough" compromise for general use.

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
