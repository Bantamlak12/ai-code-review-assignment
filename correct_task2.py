import re

pattern = r"^[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$"

def count_valid_emails(emails):
    """
    Counts the number of valid email addressed
    This function iterates through the list of emails and checks if the email is valid or not using regex.
    
    Args:
        emails (list): A list of emails.

    Returns:
        int: The number of valid email addresses.
    """
    count = 0

    if not isinstance(emails, list):
        return 0

    for email in emails:
        if not isinstance(email, str):
            continue
        if re.fullmatch(pattern, email):
            count += 1

    return count