#Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances..
class Bank:
    bank_name = "National Bank"
    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name
    def show_bank_name(self):
        return(f"The bank name is {self.bank_name}..")
account1 = Bank()
account2 = Bank()
account3 = Bank()
print(account1.show_bank_name()) # Output: The bank name is National Bank
print(account2.show_bank_name()) # Output: The bank name is National Bank
print(account3.show_bank_name()) # Output: The bank name is National Bank
account1.change_bank_name("International Bank")
print("After changing the bank name:")
print(account1.show_bank_name()) # Output: The bank name is International Bank
print(account2.show_bank_name()) # Output: The bank name is International Bank
print(account3.show_bank_name()) # Output: The bank name is International Bank

