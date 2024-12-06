

user1 = {
    'name': 'Sorna',
    'valid': False 
}

def authenticated(fn):
    # code here
    def wrapper(*args, **kwargs):
        if args[0]["valid"]:
            fn(*args, **kwargs)
        else:
            print('Not valid user')
    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)