import string
def check_password_strength(password: str) -> str:
    """
    Evaluates the strength of a password based on length, 
    uppercase letters, digits, and special characters.
    Runs with O(n) complexity using Pythonic short-circuiting.
    """
    if len(password) < 8:
        return "Weak (Immediate Fail: Less than 8 characters)"
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password) 
    has_symbol = any(char in string.punctuation for char in password) 
    score = 0
    if has_upper:
        score += 1
    if has_digit:
        score += 1
    if has_symbol:
        score += 1   
    if score == 3 and len(password) >= 12:
        return "Strong"
    elif score >= 2:
        return "Medium"
    else:
        return "Weak (Lacks variety in character types)"
def main():
    print("=== DecodeLabs Password Strength Checker ===")
    print("Type 'exit' to quit the program.\n")
    while True:
        user_input = input("Enter a password to evaluate: ")
        if user_input.lower() == 'exit':
            print("Exiting program. Stay secure!")
            break 
        strength = check_password_strength(user_input)
        print(f"Result: {strength}\n")
if __name__ == "__main__":
    main()