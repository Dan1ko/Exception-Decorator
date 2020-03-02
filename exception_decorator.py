def decorator(func):
    def wrapper(self, *args, **kwargs):
        # if self.username is None:
        #     raise Exception("No username defined!")
        if self.password is None:
            raise Exception("No password to change!") 
        func(self, *args, **kwargs)
    return wrapper

class User:
    def __init__(self):
        self.username = None
        self.password = None

    @decorator
    def get_account_balance(self):
        balance = 0
        self.username.append(balance)

    @decorator
    def change_password(self):
        new = "passw"
        if self.password == new:
            pass

u = User()
u.username = None 
u.get_account_balance()
u.change_password()