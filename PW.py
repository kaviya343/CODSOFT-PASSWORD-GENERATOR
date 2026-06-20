import random
import string

print("=" * 50)
print("        SECURE PASSWORD GENERATOR")
print("=" * 50)

try:
    length = int(input("Enter password length: "))

    if length < 4:
        print("Password length should be at least 4 characters.")
    else:
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"

        all_characters = lowercase + uppercase + digits + symbols

        password = [
            random.choice(lowercase),
            random.choice(uppercase),
            random.choice(digits),
            random.choice(symbols)
        ]

        for _ in range(length - 4):
            password.append(random.choice(all_characters))

        random.shuffle(password)

        final_password = "".join(password)

        print("\nGenerated Password:")
        print(final_password)

except ValueError:
    print("Invalid input! Please enter a valid number.")