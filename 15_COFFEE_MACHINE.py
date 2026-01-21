coffee_menu = r"E:\Program Files\RobinData\WORK\RawData"

import sys
from tabulate import tabulate

sys.path.append(coffee_menu)
import COFFEE_MACHINE_MENU as Menu

resources = {
    "water": 1000,
    "milk": 1000,
    "coffee": 1000,
    "sugar": 1000,
}
profit = 0

# Resource costs per unit
resource_costs = {
    "water": 0.01,   # $ per ml
    "milk": 0.02,    # $ per ml
    "coffee": 0.05,  # $ per g
    "sugar": 0.01    # $ per g
}

def item_is_sufficient(item_ingredients):
    for ingredient, amount in item_ingredients.items():
        if ingredient in resources:  # skip 'name' and 'price'
            if amount > resources[ingredient]:
                print(f"Sorry, there is not enough {ingredient}.")
                return False
    return True

def Payment_as_coins():
    print("Hey Please Insert Coins... ")
    quarters = int(input("How many quarters? \n")) * 0.25
    dimes = int(input("How many dimes? \n")) * 0.10
    nickels = int(input("How many nickels? \n")) * 0.05
    pennies = int(input("How many pennies? \n")) * 0.01
    
    total = quarters + dimes + nickels + pennies
    print(f"You inserted: ${round(total,2)}")
    return total

def is_transaction_success(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"Here is your change: ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, your payment is not enough. Money refunded.")
        return False

def make_coffee(coffee):
    for ingredient in ["water", "milk", "coffee", "sugar"]:
        resources[ingredient] -= coffee[ingredient]
    print(f"Here is your {coffee['name']} ☕ Enjoy!\n")

def check_and_refill():
    global profit
    for resource, amount in resources.items():
        if amount < 70:  # threshold
            print(f"\n⚠️ {resource.capitalize()} is low ({amount} left).")
            choice = input(f"Do you want to buy 500 units of {resource}? (yes/no): ").lower()
            if choice == "yes":
                refill_amount = 500
                refill_cost = refill_amount * resource_costs[resource]
                print(f"Refill cost: ${refill_cost:.2f}")

                if profit >= refill_cost:
                    profit -= refill_cost
                    resources[resource] += refill_amount
                    print(f"{resource.capitalize()} refilled by {refill_amount}. Profit left: ${profit:.2f}")
                else:
                    print(f"Profit is only ${profit:.2f}, not enough.")
                    print("Please can you give money to refill resources?")
                    print("💡 If you help, I’ll offer you 500 ml extra coffee because you refill my resources!")
                    extra_payment = Payment_as_coins()
                    if profit + extra_payment >= refill_cost:
                        profit = profit + extra_payment - refill_cost
                        resources[resource] += refill_amount
                        print(f"{resource.capitalize()} refilled by {refill_amount}. Profit left: ${profit:.2f}")
                        print("🎁 Bonus: You earned 500 ml extra coffee capacity!")
                    else:
                        print("Refill failed. Not enough money.")

                # Show report immediately after refill
                print("\nUpdated Machine Resources Status:")
                print(f"Water: {resources['water']} ml")
                print(f"Milk: {resources['milk']} ml")
                print(f"Coffee: {resources['coffee']} g")
                print(f"Sugar: {resources['sugar']} g")
                print(f"Profit: ${profit}\n")
            else:
                # Important: warning stays active
                print("Refill skipped. Warning will appear again next order until resource is refilled.")

coffee_names = [item["name"] for item in Menu.menu]

print("Welcome to the Coffee vending Machine ")
print("--------------------------------------")

print(f"{Menu.art}")
on_off = True
while on_off:
    order = input(
        "Type a coffee name to order\n"
        "Type 'Menu' to see the coffee menu\n"
        "Type 'Report' to see machine status\n"
        "Type 'Off' to turn off the machine\n"
        "Your choice: "
    ).strip()

    if order.lower() == "off":
        on_off = False

    elif order.lower() == "report":
        print("\nMachine Resources Status:")
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Sugar: {resources['sugar']} g")
        print(f"Profit: ${profit}\n")

    elif order.lower() == "menu":
        headers = ["Name"]
        rows = [[item["name"]] for item in Menu.menu]
        print(tabulate(rows, headers=headers, tablefmt="grid"))
        print()

    else:
        found = None
        for coffee in Menu.menu:
            if coffee["name"].lower() == order.lower().strip():
                found = coffee
                break

        if found:
            # Always check refill first
            check_and_refill()

            if item_is_sufficient(found):
                payment = Payment_as_coins()
                if is_transaction_success(payment, found["price"]):
                    make_coffee(found)
            else:
                print("Order cannot be completed.\n")
        else:
            print("Sorry, that item is not on the menu.\n")
