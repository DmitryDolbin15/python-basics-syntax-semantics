import sys

def extract_names(file_path):
    try:
        with open(file_path, 'r') as file:
            emails = file.read().split('\n')

        with open('employees.tsv', 'w') as output_file:
            output_file.write("Name\tSurname\tE-mail\n")
            for email in emails:
                if email.endswith("@corp.com"):
                    try:
                        name, surname = email.split('@')[0].split('.')
                        name = name.capitalize()
                        surname = surname.capitalize()
                        output_file.write(f"{name}\t{surname}\t{email}\n")
                    except :
                        print(f"Skipping invalid email format: {email}")
        print("Employee data extracted to employees.tsv")
    except :
        print(f"File not found or open: {file_path}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
        extract_names(file_path)
    else:
        print("Usage: python3 names_extractor.py <file_path>")
    