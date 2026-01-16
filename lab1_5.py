def check_multiple(number):
    """
    Returns True if number is a multiple of both 3 and 5.
    """
    # If a number is divisible by 3 AND 5, the remainder for both must be 0
    if number % 3 == 0 and number % 5 == 0:
        return True
    else:
        return False

def check_password(input_string):
    """
    Checks input against a secret word.
    """
    # The test expects the secret to be exactly "Python123"
    secret = "Python123" 
    
    if input_string == secret:
        return "access granted"
    else:
        return "access denied"
def calculate_federal_tax(salary):
    """
    Calculates tax based on salary brackets using chained conditionals.
    Note: This implements a simplified flat-rate tax logic based on the 
    prompt description, rather than marginal tax brackets.
    """
    if salary <= 11000:
        return salary * 0.10
    elif salary <= 44725:
        return salary * 0.12
    elif salary <= 95375:
        return salary * 0.22
    else:
        # Over $95,375
        return salary * 0.24