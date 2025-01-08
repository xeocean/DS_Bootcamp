import sys


def letter(search_email):
    with open("employees.tsv", 'r') as file:
        for line in file:
            name = line.split("\t")[0]
            mail = line.split("\t")[2]
            if mail.strip() == search_email:
                print(f'Dear {name}, welcome to our team. '
                      f'We are sure that it will be a pleasure to work'
                      f' with you. That’s a precondition for the professionals'
                      f' that our company hires.')


if __name__ == "__main__":
    if len(sys.argv) == 2:
        email = sys.argv[1]
        letter(email)
    else:
        print(f"Use: {sys.argv[0]} <search_mail>")
