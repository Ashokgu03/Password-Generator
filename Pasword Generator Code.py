import random
import string

def generate_password(length=12):
    # Characters to include in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure password has at least one of each type: lower, upper, digit, special character
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    # Fill the rest of the password length with random characters
    password += random.choices(characters, k=length - 4)
    
    # Shuffle the password to avoid predictable patterns
    random.shuffle(password)
    
    return ''.join(password)

# Example usage
password_length = int(input("Enter the desired length of the password (minimum 4): "))
n_numbers=int(input("how many numbers you want in your password?\n"))
n_symbol=int(input("how many symbols you want in your unique password\n"))
n_letters=int(input("and how many  letters\n"))
if password_length < 4:
    print("Password length should be at least 4 characters.")
else:
    print("Generated Password:", generate_password(password_length))
    