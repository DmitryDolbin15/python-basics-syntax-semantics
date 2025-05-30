import sys

def find_name(email, file_path="employees.tsv"):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines[1:]:
            name, surname, email_address = line.strip().split('\t')
            if email_address == email:
                return name
    print(f"Email not found: {email}")            


if __name__ == "__main__":
    if len(sys.argv) == 2:
        email = sys.argv[1]
        name = find_name(email)
        if name:
            print(f"Dear {name}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.")
    else:
        print("Usage: python3 letter_starter.py <email>")

    