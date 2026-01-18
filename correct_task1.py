def calculate_average_order_value(orders):
    """
    Calculates the average order value from a list of orders

    This function iterates through the list of orders and checks if the order is dictionary, and 
    if it has the required fields and the status is "completed" and the amount is a number, it adds
    the amount to the total and increments the total orders count.

    Args:
        orders (list): A list of orders.

    Returns:
        float: The average order value.
    """
    total_amount = 0
    total_orders_count = 0

    if not isinstance(orders, list) or len(orders) == 0:
        return 0.0

    for order in orders:
        if not isinstance(order, dict):
            continue
        if "status" in order and "amount" in order and order["status"] == "completed" and type(order["amount"]) in [int, float]:
            total_amount += order["amount"]
            total_orders_count += 1

    return total_amount / total_orders_count if total_orders_count > 0 else 0.0
