import sys

def extractor(file_path):
    with open(file_path, 'r') as file:
        with open("employees.tsv", 'w') as employees:
            employees.write("Name\tSurname\tE-mail\n")
            for email in file.readlines():
                full_name = email.split('@')[0].split(".")
                employees.write(f'{full_name[0].capitalize()}\t'
                                f'{full_name[1].capitalize()}\t{email}')


if __name__ == "__main__":
    if len(sys.argv) == 2:
        path = sys.argv[1]
        extractor(path)
        print("Save in employees.txt")
    else:
        print(f"Use: {sys.argv[0]} <filename.txt>")