#Virtual Coffee Machine
class CoffeeMachine:
    def __init__(self):
        self.water = 250
        self.milk = 150
        self.coffee = 76
        self.money = 140
        self.prices = {"coffee": 100, "latte": 120, "cappuccino": 135}
        self.resource_requirements = {"coffee": {"water": 50, "milk": 0, "coffee": 16},
                                      "latte": {"water": 50, "milk": 75, "coffee": 16},
                                      "cappuccino": {"water": 50, "milk": 75, "coffee": 16}}

    def report(self):
        print("Resources available are:")
        print(f"Water: {self.water}ml\nMilk: {self.milk}ml\nCoffee: {self.coffee}g\nMoney: Rs {self.money}")

    def turn_off(self):
        print("Turning off the coffee machine.")
        exit()

    def make_coffee(self, drink):
        required_resources = self.resource_requirements[drink] # Get the required resources for chosen drink
        if not self.has_enough_resources(required_resources): # Check if, enough resources for chosen drink
            return False
        if not self.check_resources_available(required_resources): # Check no resource, prompt user to refill
            return False
        
        price = self.prices[drink] # Proceed with the purchase if there are enough resources
        total_rs = self.accept_payment(price)  # Get the total amount inserted
        if total_rs is False:
            return False

        # Deduct the resources used for making the drink
        self.deduct_resources(required_resources)

        # Prepare and serve the coffee
        self.serve_coffee(drink, price, total_rs)  # Pass total_rs as an argument

        return True

    def check_resources_available(self, required_resources):
        for resource, amount in required_resources.items():
            if getattr(self, resource) < amount:
                print(f"Sorry, there is not enough {resource}. Please refill.")
                if not self.add_resource(resource):
                    return False
        return True

    def add_resource(self, resource):
        try:
            cost_per_unit = 5  # Cost per unit of resource (adjust as needed)
            amount = int(input(f"Please add {resource}. Enter the amount in ml/g: "))
            total_cost = amount * cost_per_unit
            total_rs = self.accept_payment(total_cost)
            if total_rs is False:
                return False
            setattr(self, resource, getattr(self, resource) + amount)
            print(f"Added {amount} to {resource}.")
            return True
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return False

    def has_enough_resources(self, required_resources):
        for resource, amount in required_resources.items():
            if getattr(self, resource) < amount:
                print(f"Sorry, there is not enough {resource}.")
                return False
        return True

    def accept_payment(self, price):
        try:
            total_rs = int(input(f"Please insert Rs {price}: "))
            if total_rs < price:
                print("Sorry, not enough money. Money refunded.")
                return False
            self.money += price
            return total_rs  # Return total_rs instead of True
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return False

    def deduct_resources(self, required_resources):
        for resource, amount in required_resources.items():
            setattr(self, resource, getattr(self, resource) - amount)

    def serve_coffee(self, drink, price, total_rs):
        change = total_rs - price
        print(f"Here is your Rs {change} in change.")
        print(f"Here is your {drink}. Enjoy!")

    def start(self):
        while True:
            choice = input("What would you like to have (Coffee, Latte, Cappuccino): ").lower()
            if choice == "report":
                self.report()
            elif choice == "off":
                self.turn_off()
            elif choice not in ["coffee", "latte", "cappuccino"]:
                print("Invalid input. Please try again.")
            else:
                self.make_coffee(choice)

# Create an instance of CoffeeMachine and start the coffee machine
machine = CoffeeMachine()
machine.start()
