import random
import string

def generate_passW(length, alphanum):
    characters = string.ascii_letters + string.digits
    if not alphanum:
        characters += string.punctuation
    
    passW = ''.join(random.choice(characters) for _ in range(length))
    return passW

def main():
    try:
        passW_length = int(input("Enter the desired length of the passW: "))
        if passW_length <= 0:
            print("passW length must be a positive integer.")
            return

        alphanum_choice = input("Do you want the passW to be alphanum only? (y/n): ")
        alphanum = True if alphanum_choice.lower() == "y" else False

        passW = generate_passW(passW_length, alphanum)
        print("Generated passW:", passW)
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

if __name__ == "__main__":
    main()
