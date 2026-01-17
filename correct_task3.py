def average_valid_measurements(values):
    """
    Calculates the average of valid measurements by ignoring missing values.

    This function iterates through the list of values and checks if the value is a number,
    if it is it adds the value to the total and increments the count. If the value is not a number, it skips it.

    Args:
        values (list): A list of values.

    Returns:
        float: The average of valid measurements.
        None: If the input is not a list or the list is empty.
    """
    total = 0
    count = 0

    if not isinstance(values, list):
        return None

    for v in values:
        if type(v) in [int, float]:
            total += float(v)
            count += 1

    return total / count if count > 0 else None
