# Liskov's substitution principle
# A subclass should be substitutable for its superclass without affecting the correctness of the program, meaning that derived classes must be usable through the base class interface without the need for the user to know the difference.

# bad example

class User:
    def __init__(self, id):
        self.id = id
    
    def access_resource(self):
        raise NotImplementedError("Subclasses must implement this method")

class NormalUser(User):
    def __init__(self, id):
        super().__init__(id)

    def access_resource(self):
        # have to pay before accessing resource
        print("Load payment page for Normal User")
        paid = input("Did the user pay? (yes/no): ")
        if paid.lower() == "yes":
            print("Normal User has paid.")
            print("Normal User accessing resource.")
        else:
            print("Normal User has not paid.")
            print("Normal User cannot access resource.")

class PremiumUser(User):
    def __init__(self, id):
        super().__init__(id)

    def access_resource(self):
        # check if premium is not expired
        expired = input("Is the Premium User's subscription expired? (yes/no): ")
        if expired.lower() == "yes":
            print("Premium User's subscription is expired.")
            print("Premium User cannot access resource.")
        else:
            print("Premium User accessing resource.")

class UnlimitedUser(User):
    def __init__(self, id):
        super().__init__(id)

    def access_resource(self):
        print("Unlimited User accessing resource without restrictions.")

normal = NormalUser(1)
premium = PremiumUser(2)
unlimited = UnlimitedUser(3)

normal.access_resource()  # Normal User has to pay
premium.access_resource()  # Premium User has to check subscription
unlimited.access_resource()  # Unlimited User has no restrictions

# good practice

from abc import ABC, abstractmethod
import datetime

ONE_DAY_PRICE = 10
MONTH_PRICE = 2500
YEAR_PRICE = 30000
LIFE_PRICE = 100000

class payable():
    def __init__(self):
        super().__init__()

    def pay(self, amount, to_account):
        print(f"Paying {amount} to {to_account}")
        paid = input("Did the user pay? (yes/no): ")
        if paid.lower() == "yes":
            print("Payment successful.")
            return True
        else:
            print("Payment failed.")
            return False

class expirable():
    def __init__(self):
        super().__init__()
        self.expire_date = datetime.datetime.now() - datetime.timedelta(days=1)  # Default to expired
    
    def check_expiration(self):
        return self.expire_date < datetime.datetime.now()

    def renew(self, days):
        self.expire_date = datetime.datetime.now() + datetime.timedelta(days=days)

class user(ABC, expirable, payable):
    def __init__(self, id):
        super().__init__()
        self.id = id
    
    def access_resource(self):
        if (super().check_expiration()):
            print(f"User {self.id}'s subscription has expired.")
        else:
            print(f"User {self.id}'s subscription is active. Access resource.")

class normal_user(user):
    def __init__(self, id):
        super().__init__(id)
        if (super().pay(ONE_DAY_PRICE, "resource_owner_account")):
            print(f"User {self.id} has paid for resource access.")
            super().renew(1)  # Renew for 1 day
        else:
            print(f"User {self.id} has not paid for resource access.")

    def access_resource(self):
        super().access_resource()

class premium_user(user):
    def __init__(self, id):
        super().__init__(id)
        if (super().pay(MONTH_PRICE, "resource_owner_account")):
            print(f"User {self.id} has paid for resource access.")
            super().renew(30)  # Renew for 30 days
        else:
            print(f"User {self.id} has not paid for resource access.")

    def access_resource(self):
        super().access_resource()

class unlimited_user(user):
    def __init__(self, id):
        super().__init__(id)
        if (super().pay(LIFE_PRICE, "resource_owner_account")):
            print(f"User {self.id} has paid for resource access.")
            super().renew(36500)  # Renew for 100 years
        else:
            print(f"User {self.id} has not paid for resource access.")

    def access_resource(self):
        super().access_resource()

normal = normal_user(1)
premium = premium_user(2)
unlimited = unlimited_user(3)

normal.access_resource()
premium.access_resource()
unlimited.access_resource()