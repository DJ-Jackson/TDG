from Account import Account

class Secure_Account(Account):
    def __init__(self, email, username, password, first_name, last_name = None, human_dob, dog_name, dog_dob, location = None, account_number = 00000000):
        super().__init__(first_name, last_name = None, human_dob, dog_name, dog_dob, location = None, account_number = 00000000)
        self.email = email
        self.username = username
        self.password = password