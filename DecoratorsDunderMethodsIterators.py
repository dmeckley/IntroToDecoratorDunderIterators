class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self.__transactions = []

    def __repr__(self):
        return('Account({!r}, {!r})'.format(self.owner, self.amount))

    def __str__(self):
        return("Account of {} with starting amount: {}".format(self.owner, self.amount))

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("Please use integer for amount.")
        self.__transactions.append(amount)

    @property
    def balance(self):
        return(self.amount + sum(self.__transactions))
    
    def widthdrawal(self, amount):
        self.amount -= amount

    
def main():
    s = 'abc'
    it = iter(s)
    print(it)
    print(it.__iter__())
    print(next(it))
    print(it.__next__())
      
    account = Account('bob')
    account = Account('bob', 10)

    print('str(account) = ', str(account))
    print('account = ', account)
    print('repr(account) = ', repr(account))

    account.add_transaction(20)
    account.add_transaction(-10)
    account.add_transaction(50)
    account.add_transaction(-20)
    account.add_transaction(30)
    print('The account balance is:', account.balance)
    account.widthdrawal(10)
    print('The account balance is:', account.balance)


if __name__ == "__main__":
    main()