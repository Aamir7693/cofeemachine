import Menu
class coffeeMaker:
    def __init__(self):
        self.menu=Menu.MENU
        self.resources=Menu.resources
    def insertMoney(self):
        print("Please insert coins.\n")
        quart=int(input("how many quarters?:\n"))
        dime=int(input("how many dimes?:\n"))
        nick=int(input("how many nickles?:\n"))
        penn=int(input("how many pennies?:\n"))
        return quart,dime,nick,penn
    def calculate(self,coffee):
        quart,dime,nick,penn=self.insertMoney()
        sum=(quart*0.25)+(dime*0.10)+(nick*0.05)+(penn*0.01)
        temp=self.menu[coffee]['cost']
        if sum > temp:
            return sum-temp
        elif sum == temp:
            return 0
        else:
            return -sum

    def main(self):
        coffee=coffeeMaker()
        coffee.coffeeType()
    def resourceCheck(self,coffee):
        tempdict=self.menu[coffee]['ingredients']
        for key,value in tempdict.items():
            if value <= self.resources[key]:
                self.resources[key]-=value
            else:
                print(f"Sorry there is not enough {key}.")
                return False
        return True

    def coffeeType(self):
        coffee=input("What would you like? (espresso/latte/cappuccino):\n")
        cond=self.resourceCheck(coffee)
        if cond==True:

            amount=self.calculate(coffee)
            if amount == 0 or amount > 0:
                print(f"Here is ${amount} in change.\n")
                print(f"Here is your {coffee} ☕️. Enjoy!\n")
                self.main()
            elif amount < 0:
                print("Sorry that's not enough money. Money refunded.\n")
                self.main()
        else:
            self.main()
if __name__=="__main__":
    coffee=coffeeMaker()
    coffee.main()