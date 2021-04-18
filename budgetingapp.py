database = {}


# BudgetingApp


class Category:
    def __init__(self, category):
        self.budget_type = category
        self.category_balance = 0
        # self.database.keys() = self.budget_type
        database[self.budget_type] = self.category_balance

    def deposit(self, amount):
        self.category_balance += amount
        database[self.budget_type] += amount

    def withdraw(self, amount):
        self.category_balance -= amount

    def balance(self):
        print(database[self.budget_type])
        return database[self.budget_type]

    def transfer(self, amount, category):
        if category in database.keys():
            if category != self.budget_type:
                database[category] += amount
            else:
                print('You cant transfer to the same budget')
        else:
            print('Invalid category')


def init():
    print('  ***********Welcome to BudgetApp************\nWhat would you wanna do?')
    print("******" * 40)
    originator = int(input('Press 1:To Create budget, 2:To Check Budget, 3:To Quit: '))

    def depictor():
        cateName = Category(input('Enter your budget name: '))
        return cateName

    def operations():
        call = int(input('Enter 1:Deposit, 2:Withdraw, 3:Balance, 4:Transfer, 5:To Start Again'))
        if call == 1:
            amount = int(input('Enter amount to deposit: '))
            budget.deposit(amount)
        elif call == 2:
            amount = int(input('Enter amount to withdraw: '))
            budget.withdraw(amount)
        elif call == 3:
            print(budget.balance())
        elif call == 4:
            amount = int(input('Enter amount to transfer: '))
            category = input('Enter category to transfer to: ')
            budget.transfer(amount, category)
        elif call == 5:
            init()
        else:
            print('Invalid value, please try again ')
            init()

    while originator != 3:
        if originator == 1:
            budget = depictor()
            print('What would you love to do?')
            operations()
        elif originator == 2:
            for keys in database:
                print("***", keys, "***")
            value = input('Do you want the entire balance or a specific budget. YES|NO: ')
            if value.upper() == 'YES':
                for keys, values in database.items():
                    print("***", keys, "\t", values, "***")

                operations()
                # print(database)
            elif value.upper() == 'NO':
                request = input('Enter budget name: ')
                if request in database.keys():
                    print(request, ' ', database[request])
                    operations()
                else:
                    print('Budget do not exist')
                    init()
            else:
                print('Invalid value, please try again ')
                init()
        elif originator == 3:
            exit()
        else:
            print('Invalid value, please try again ')
            init()
        originator = int(input('\nPress 1:To Create budget, \n2:To Check Budget, \n3:To Quit: \n'))


init()

# @jamido
