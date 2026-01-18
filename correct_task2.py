# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.

import re #regular expressions library for pattern matching

def count_valid_emails(emails):
    """
    Counts the number of valid email addresses in a list.
    Validates structure (user@domain.ext) and handles invalid input types safely.
    """
    # Input Validation: Ensure we have a list/tuple to iterate over
    if not emails or not isinstance(emails, (list, tuple)):
        return 0 # more error logging for developers is needed based on where the function is being used

    valid_count = 0
    #  Define a standard regex for basic email validation
    # Pattern: Non-whitespace(s) + @ + Non-whitespace(s) + . + Non-whitespace(s)
    # This prevents cases like "@", "user@", "domain.com", or "a b@c.com"
    # more explanation found in NOTES.md
    email_pattern = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

    for email in emails:
        # Data Type Safety: Ensure the item is a string
        if not isinstance(email, str):
            continue

        # Logic: Apply regex check
        # .match checks from the beginning of the string
        if email_pattern.match(email):
            valid_count += 1

    return valid_count