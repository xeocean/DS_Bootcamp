import sys


def marketing(task):
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
               'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
               'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru',
                    'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
                    'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

    if task == "call_center":
        my_list = list((set(clients) | set(participants)) - set(recipients))
        print(my_list)
    elif task == "potential_clients":
        my_list = list(set(participants) - set(clients) - set(recipients))
        print(my_list)
    elif task == "loly_program":
        my_list = list((set(recipients) | set(clients)) - set(participants))
        print(my_list)

if __name__ == "__main__":
    keywords = ["call_center", "potential_clients", "loly_program"]
    try:
        if len(sys.argv) == 2 and sys.argv[1] in keywords:
            request = sys.argv[1]
            marketing(request)
    except ValueError as e:
        print(f'Error: {e}')