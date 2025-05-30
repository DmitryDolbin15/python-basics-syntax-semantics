import sys

def list_to_set(example):
    return set(example)

def to_do(x1,x2):
    return list(x1 -x2 )


def market(word):
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
               'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
               'elon@paypal.com', 'jessica@gmail.com']
    
    participants = ['walter@heisenberg.com', 'vasily@mail.ru',
                    'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
                    'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

    set_clients = list_to_set(clients)

    set_participants  = list_to_set(participants)

    set_recipients  = list_to_set(recipients)

    if word == "call_center" :
        list_of= to_do(set_clients, set_recipients)
    elif word =="potential_clients" :
        list_of = to_do(set_participants, set_clients)
    elif word == "loyalty_program" :
        list_of = to_do(set_clients,set_participants)
    print(f"{', '.join(t for t in list_of)}")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        if (sys.argv[1] in ("call_center" ,"potential_clients" ,"loyalty_program")):
            market(sys.argv[1])
        else :
            print("Usage: python3 marketing.py <task>")
            print("Available tasks: call_center, potential_clients, loyalty_program")
    else :
        print("Usage: python3 marketing.py <task>")
        print("Available tasks: call_center, potential_clients, loyalty_program")