# Write your corrected implementation for Task 1 here.
# Do not modify `task1.py`.

def calculate_average_order_value(orders):
    """
    Calculates the average value of non-cancelled orders.
    Safely handles invalid input types, string amounts, and empty lists.
    """
    # Input Validation: Ensure orders is a list or tuple and not empty
    if not orders or not isinstance(orders, (list,tuple)):
        return 0.0 # this is a fail safe approach, but more error should be logged in production code. 

    valid_amounts = []

    for order in orders:
        # Data Integrity: Ensure the item inside the list is actually a dictionary
        if not isinstance(order, dict):
            continue

        # Logic: Filter out cancelled orders
        # Using .get() prevents crash if 'status' key is missing
        if order.get("status") == "cancelled":
            continue

        # Type Safety: Safely parse 'amount'
        try:
            # Handles numeric strings (e.g., "10.50") and standard numbers
            amount = float(order.get("amount"))
            valid_amounts.append(amount)
        except (ValueError, TypeError):
            # Skip if amount is missing, None, or a non-numeric string
            continue

    # Math Safety: Prevent division by zero if no valid orders were found
    if not valid_amounts:
        return 0.0

    return sum(valid_amounts) / len(valid_amounts)