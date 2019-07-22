class Account:
    def __init__(self, first_name, last_name = None, human_dob, dog_name, dog_dob, location = None, account_number = 00000000):
        self.first_name = first_name
        self.last_name = last_name
        self.human_dob = human_dob
        self.dog_name = dog_name
        self.dog_dob = dog_dob
        self.location = location
        self.account_number = account_number
        if user_count == None:
            user_count = 0

    user_count += 1

    def update_firstname(self, new_first):
        self.first_name = new_first

    def update_lastname(self, new_last):
        self.last_name = new_last

    def update_dogname(self, new_dogname):
        self.dog_name = new_dogname

    def update_location(self, new_location):
        self.location = new_location

    def add_companion(self, new_companion):
        self.companion.insert(0, new_companion)