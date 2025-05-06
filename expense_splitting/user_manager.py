class User:
    def __init__(self, user_id, name, mobile_number):
        self.id = user_id
        self.name = name
        self.mobile_number = mobile_number

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', mobile_number='{self.mobile_number}')"


class UserManager:
    def __init__(self):
        self.users_by_id = {}
        self.users_by_mobile = {}
        self.next_id = 1

    def add_user(self, name, mobile_number):
        if mobile_number in self.users_by_mobile:
            print("Error: User with this mobile number already exists!")
            return None

        user = User(self.next_id, name, mobile_number)
        self.users_by_id[self.next_id] = user
        self.users_by_mobile[mobile_number] = user
        print(f"User added with ID: {self.next_id}")
        self.next_id += 1
        return user

    def remove_user(self, user_id):
        user = self.users_by_id.get(user_id)
        if not user:
            print("Error: User does not exist.")
            return

        del self.users_by_id[user_id]
        del self.users_by_mobile[user.mobile_number]
        print("User removed successfully.")

    def get_user_by_id(self, user_id):
        return self.users_by_id.get(user_id)

    def get_user_by_mobile(self, mobile_number):
        return self.users_by_mobile.get(mobile_number)

    def get_all_users(self):
        return list(self.users_by_id.values())

if __name__ == "__main__":
    manager = UserManager()
    manager.add_user("Alice", "9991110001")
    manager.add_user("Bob", "9991110002")
    print(manager.get_all_users())
    manager.remove_user(1)
    print(manager.get_user_by_id(2))