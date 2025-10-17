class user:
    all_users = []
    def __init__(self,name,):
        self.name = name
        user.all_users.append(self)

    @classmethod
    def get_user_count(cls):
        return len(cls.all_users)
u1 = user('Alic')
u2 = user('Bob')
print(user.get_user_count())
