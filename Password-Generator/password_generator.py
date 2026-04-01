import secrets
import string

def generate_password(length, use_digits=True, use_special=True):
    """Generates a random password.

    Args:
        length (int): Desired length of the password.
        use_digits (bool): Whether to include numbers.
        use_special (bool): Whether to include special characters.

    Returns:
        str: The generated password.
    """
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        return ""

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def main():
    """Interface for the Password Generator."""
    print("--- Secure Password Generator ---")
    try:
        length = int(input("Enter the desired password length: "))
        include_nums = input("Include numbers? (y/n): ").lower() == 'y'
        include_special = input("Include special characters? (y/n): ").lower() == 'y'

        if length < 6:
            print("Length must be at least 6.")
            return

        password = generate_password(length, include_nums, include_special)
        print(f"\nGenerated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a number for length.")

if __name__ == '__main__':
    main()