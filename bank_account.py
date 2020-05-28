class BankAccount:
    """ Models a bank account """
    def __init__(this, number, name, balance):
        """ Initilize the instance variables of a bank account object.
            Disallows a negative initial balance. """
        if balance < 0:
            raise ValueError('Negative initial balance')
        this.__acount_number = number
        this.__name = name
        this.__balance = balance

    def id(this):
        """ Returns the account number of this bank account object. """
        return this.__acount_number

    def deposit(this, amount):
        """ Add funds to the account. There is no limit
            to the size of the deposit.
        """
        this.__balance += amount

    def withdraw(this, amount):

        """ Remove funds from the account, if possible.
            Only completes the withdrawal successfully if
            there are enough funds in the account to
            fulfill the withdrawal .
            Return true if successful, false otherwise
        """
        result = False
        if this.__balance - amount >=0:
            this.__balance -= amount
            result = True
        return result

    def __str__(this):
        """ Returns the stringrepresentaion for this object"""
        return '[{:>5} {:<10} {:>7}]'.format(this.__account_number,this.__name, this.__balance)

# ----------------------------------------------------------------
# Global functions that use BankAccount objects

def open_database(filename, db):
    """ Read account information from a given file and store it
        in the given list. """
    with open(filename) as lines:
        for line in lines:
            line.strip()
            number, name, balance = line.split(",")
            db.append(BankAccount(int(number), name, int(balance)))

def print_database(db):

    """ Displays the content of the database """
    for acct in db:
        # Calls the __str__ method of aact
        print(acct)
        
def get_account(db,account_number):

    """ Retrieve an account object with a given account number. """
    for acct in db:
        if acct.id() == acount_number:
            return acct

def main():
    database = []

    try:
        # Open the database of accounts
        open_database('accuntdata.text', database)
        print_database(database)
        print("---------------------")
        customer = get_account(database, 129)
        if customer:
            print('Account 129 before deposit of $100: ', end='')
            print(customer)
            customer.deposit(100)
            print("Account 129 after deposit of $100: ", end="")
            print(customer)
            print("--------------------")
            print("Account 129 before withdraw of $500: ", end="")
            print(customer)
            customer.withdraw(500)
            print("Account 129 after withdraw of $500: ", end="")
            print(customer)
            print("--------------------")
            print("Account 129 before withdraw of $80000: ", end="")
            print(customer)
            customer.withdraw(80000)
            print("Account 129 after withdraw of $80000: ", end="")
            print(customer)
    except Exception:
        print('Error in acccount database')
        raise
main()
