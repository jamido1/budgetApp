import os


class Budget:

    def __init__(self, items):
        os.system('cls')
        self.items = items
        self.balance = 0
        self.main()


    def main(self):
        print("****" * 60)

        print("'====****welcome to BudgetApp****====\n")
        print("****" "***" * 40)
        print("select budget category")
        Cate_choice = int(input(
            "\nPress (1) For Food category \nPress (2) For Clothing category\nPress (3) For Entertainment category \n"))
        if Cate_choice == 1:
            print('Food category')
            main_menu = int(input(
                "What would you like to do? \nPress (1) to deposit \nPress (2) to withdraw \nPress (3) to check Balance \n press (4) to transfer funds \n"))
            if main_menu == 1:
                food.deposit()
            elif main_menu == 2:
                food.withdraw()
            elif main_menu == 3:
                food.get_balance()
            elif main_menu == 4:
                food.transfer()
            else:
                print("Invalid Input")
            return main_menu
        elif Cate_choice == 2:
            print('Clothing category')
            main_menu2 = int(input(
                "What would you like to do? \nPress (1) to deposit \nPress (2) to withdraw \nPress (3) to check Balance \n press (4) to transfer funds \n"))
            if main_menu2 == 1:
                clothing.deposit()
            elif main_menu2 == 2:
                clothing.withdraw()
            elif main_menu2 == 3:
                clothing.get_balance()
            elif main_menu2 == 4:
                clothing.transfer()
            else:
                print("Invalid Input")
            pass
        elif Cate_choice == 3:
            print('Entertainment category')
            main_menu3 = int(input(
                "What would you like to do? \nPress (1) to deposit \nPress (2) to withdraw \nPress (3) to check Balance \n press (4) to transfer funds \n"))
            if main_menu3 == 1:
                entertainment.deposit()
            elif main_menu3 == 2:
                entertainment.withdraw()
            elif main_menu3 == 3:
                entertainment.get_balance()
            elif main_menu3 == 4:
                entertainment.transfer()
            else:
                print("Invalid Input")
            pass

    def deposit(self, amount):
        os.system('cls')
        amount = int(input("How much would you like to deposit into\n"))
        self.balance += amount

        return f"Your new balance is {self.balance} in {self.items} budget"

    def withdraw(self, amount):
        os.system('cls')
        with_amount = int(input("How much would you like to withdraw"))
        if self.balance < with_amount:
            print("********** Transaction Failed **********")
            print("Insufficient funds")

        else:
            self.balance -= with_amount
            result = "********** Successful Transaction **********\n"
            result += f"Your new balance is {self.balance} in {self.items} budget"

            return result

    def get_balance(self):
        balance = f"The balance for {self.items} is {self.balance}"
        return balance

    def transfer(self, amount, category):

        amount = int(input("How much would you like to transfer"))
        if self.items == category.name:
            result = "ERROR!\n"
            result += "You cannot transfer funds within the same category\n"
            result += "You can only transfer funds to another category"
            return result

        else:
            if self.balance < amount:
                print("********** Transaction Failed **********")
                print("Insufficient funds")
            else:
                self.balance -= amount
                category.balance += amount

                transfer_result = "********** Successful Transaction **********\n"
                transfer_result += f"The balance for the {self.items} budget is {self.balance}\n"
                transfer_result += f"The balance for the {category.name} budget is {category.balance}"

                return transfer_result


food = Budget('Food category')
clothing = Budget('Clothing category')
entertainment = Budget('Entertainment category')
