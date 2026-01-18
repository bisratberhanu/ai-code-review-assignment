
## Task Two — Count Valid Emails

There are some information about email validation that should be addressed. The regex solution handles 99% of common email formats but does not cover all edge cases defined in RFC 5322(The official standard for email format). For most applications, this level of validation is sufficient, but for systems requiring strict compliance, additional checks may be necessary.
- More information can be found at : https://tools.ietf.org/html/rfc5322#section-3.4.1
- If more validation is required, external libraries like `email-validator` can be used for comprehensive checks.

The Regex pattern breakdown can be found below:
    pattern used for reference: r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    
    1. ^: Anchors to the start of the string (prevents partial matches).
    2. [^@\s]+: Matches the local part (username). It ensures one or more characters that are NOT an @ symbol and NOT whitespace.
    3. @: Matches the literal separator.
    4. [^@\s]+: Matches the domain name (ensures no spaces or extra @).
    5. \.: Matches the literal dot . separator.
    6. [^@\s]+: Matches the TLD (e.g., com, org).
    7. $: Anchors to the end of the string.