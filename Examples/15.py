"""
15. Imagine you are designing a banking application. What would a
customer look like? What attributes would she have? What methods
would she have?
"""


class Customer:
    def __init__(self, name, ac_no, email, address, balance=0):
        self.__name = name
        self.__ac_no = ac_no
        self.__email = email
        self.__address = address
        self.__balance = balance

    def __str__(self):
        return self.__name

    def get_details(self):
        """
        get all the details about the user
        :return: a dict of data as keys and values
        """
        return {
            'Name': self.__name,
            'AC No.': self.__ac_no,
            'Address': self.__address,
            'Email': self.__email
        }

    def check_balance(self):
        """
        :return: returns the balance
        """
        return 'balance({self.__ac_no}): {self.__balance}/-'

    def add_balance(self, balance=0):
        """
        Add the balance to the account.
        :param balance: the amount the customer deposits
        """
        self.__balance += balance

    def withdraw_balance(self, amount=0):
        """
        It performs operation when the user withdraws the balance.
        :param amount: Amount user withdraws
        """
        self.__balance -= amount

    def update_details(self, name, email, address):
        """
        Update the details provided as updated data
        :param name: the updated name
        :param email:
        :param address:
        """
        self.__name = name
        self.__email = email
        self.__address = address

    def update_name(self, name):
        """
        updated the name as provided
        :param name: The updated name
        """
        self.__name = name

    def update_address(self, address):
        """
        updated the name as provided
        :param address: The updated address
        """
        self.__address = address

    def update_email(self, email):
        """
        update the customer Email address.
        :param email: Updated email
        """
        self.__email = email

    def change_ac_no(self, new_ac_no):
        """
        Changes the user ac_no to the given new account no.
        :param new_ac_no: The new account number to be changed
        """
        self.__ac_no = new_ac_no


customer_1 = Customer('Sita Kc', '3456788',
                      'sita@gmail.com', 'Kalanki, Kathmandu',
                      3000
                      )

print(customer_1)  # prints Name because of the __str__ magic method

# update name
customer_1.update_name('Sita Kc')
# updated name
print(customer_1)
print(customer_1.check_balance())

print(customer_1.get_details())
customer_1.update_email('sitakc2020@gmail.com')  # updates email
customer_1.update_address('Sitapaila, Kathmandu')

# customer deposits the balance
customer_1.add_balance(10000)
print(customer_1.check_balance())

customer_1.withdraw_balance(8000)
print(customer_1.check_balance())
