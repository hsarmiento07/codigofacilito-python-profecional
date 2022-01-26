class Usuario:

    def __init__(self, username, password):
        self.username = username
        self.password = password

user1 = Usuario('User1', 'password1')
user2 = Usuario('User2', 'password2')
user3 = Usuario('User3', 'password3')
user4 = Usuario('User4', 'password4')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(user4.__dict__)