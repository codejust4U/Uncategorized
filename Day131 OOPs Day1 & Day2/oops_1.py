class ATM:
    #static/class varibale
    __counter=1
    def __init__(self):
        self.__pin = ""  # private pin = __pin
        self.__balance = 0
        self.sno = ATM.__counter
        ATM.__counter = ATM.__counter+1
        #self.__menu()

        print(id(self))

    @staticmethod
    def get_counter():
        return  ATM.__counter
    
    @staticmethod
    def set_counter(new):
        if type(new)==int:
            ATM.__counter=new
        else:
            print("Not allowed")

    def __datas(self):
        pass

    def get_pin(self):
        return self.__pin

    def set_pin(self, new_pin):
        if type(new_pin)==str:
            self.__pin == new_pin
            print('New Pin Set')
        else:
            print("Not allowed")

    def __menu(self):
        user_input = input("""
    Hello, how would you like to proceed?
                           1. Enter 1 to create pin
                           2. Enter 2 to deposit
                           3. Enter 3 to withdraw
                           4. Enter 4 to check balance
                           5. Enter 5 to exit
""")
        if (user_input) == '1':
            self.create_pin()
        elif user_input == '2':
            self.deposit()
        elif user_input == '3':
            self.withdraw()
        elif user_input == '4':
            self.check_balance()
        else:
            print("Exit")

    def create_pin(self):
        self.__pin = input("Enter your pin : ")
        print("Pin created successfully.")

    def deposit(self):
        temp = input("Enter your pin : ")
        if temp == self.__pin:
            amount = int(input("Enter the amount : "))
            self.__balance = self.__balance+amount
            print("Deposit successfully")
        else:
            print("Invalid pin")

    def withdraw(self):
        temp = input("Enter your pin : ")
        if temp == self.__pin:
            amount = int(input("Enter the amount : "))
            # Check for insufficient funds condition here
            if amount < self.__balance:
                self.__balance = self.__balance-amount
                print("Amount Withdrawn Successfully!")
            else:
                print("Insufficient Funds! Please Deposit More Money...")
        else:
            print("Invalid pin")

    def check_balance(self):
        temp = input("Enter your pin : ")
        if temp == self.__pin:
            print("Your Balance is:", str(self.__balance))
        else:
            print("Invalid Pin!! Try Again..")


# Creating a class Fraction with its own datatype

class Fraction:
    def __init__(self, n, d):
        self.num = n
        self.den = d

    def __str__(self):
        return "{}/{}".format(self.num, self.den)

    def __add__(self, other):
        temp_num = self.num*other.den+other.num*self.den
        temp_den = self.den*other.den
        return "{}/{}".format(temp_num, temp_den)

    def __sub__(self, other):
        temp_num = self.num*other.den-other.num*self.den
        temp_den = self.den*other.den
        return "{}/{}".format(temp_num, temp_den)

    def __mul__(self, other):
        temp_num = self.num*other.den*other.num*self.den
        temp_den = self.den*other.den
        return "{}/{}".format(temp_num, temp_den)

    def __truediv__(self, other):
        temp_num = self.num*other.den/other.num*self.den
        temp_den = self.den*other.den
        return "{}/{}".format(temp_num, temp_den)
