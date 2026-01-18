# Write your corrected implementation for Task 3 here.
# Do not modify `task3.py`.

def average_valid_measurements(values):
    """
    Calculates the average of valid numeric measurements.
    Safely handles mixed types (strings, None) and empty inputs.
    """
    # Input Validation: Ensure input is a list or tuple other wise the iteration will fail
    if not values or not isinstance(values, (list, tuple)):
        return 0.0

    valid_measurements = []

    for v in values:
        # Filter Nulls immediately
        if v is None:
            continue
            
        # Type Safety: Try to convert to float
        # This handles integers, floats, and numeric strings (e.g., "42.5")
        try:
            val = float(v)
            valid_measurements.append(val)
        except (ValueError, TypeError):
            # Skip non-numeric strings (e.g., "error") or complex types
            continue

    # Math Safety: Prevent division by zero
    if not valid_measurements:
        return 0.0 # error log can be written based on where this function is being used. e.g a data pipeline still with out breaking the flow. 

    return sum(valid_measurements) / len(valid_measurements)