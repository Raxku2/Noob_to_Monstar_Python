def validate_username(username):
    if len(username) < 8:
        return False, "Username must be at least 8 characters long"

    has_lower = False
    has_upper = False
    has_digit = False

    for ch in username:
        if ch.islower():
            has_lower = True
        elif ch.isupper():
            has_upper = True
        elif ch.isdigit():
            has_digit = True
        else:
            return False, "Special characters are not allowed"

    if not has_lower:
        return False, "Username must contain at least one lowercase letter"
    if not has_upper:
        return False, "Username must contain at least one uppercase letter"
    if not has_digit:
        return False, "Username must contain at least one number"

    return True, "Username is valid"


# Main
user_input = input("Enter username: ")

status, message = validate_username(user_input)

print(message)
