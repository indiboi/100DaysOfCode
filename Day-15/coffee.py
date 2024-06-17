MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 150,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 250,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300,
    }
}

resources = {
    "water": 500,
    "milk": 300,
    "coffee": 300,
}

machine_money = 0
notes_100 = 0
notes_50 = 0
notes_20 = 0
notes_10 = 0
change = 0



while True:
    user_drink = str(input("Enter the drink you want (espresso/latte/cappuccino): ").lower())   #takes user input
    if user_drink == "exit":    #stops offering drinks and services
        break
    if user_drink == "report":  #provides a report regarding the resources and cash 

        for i in resources:
            print(resources[i])
        print(f"${machine_money}")
        continue

    print("Enter the money below: ")
    notes_100 = int(input("Enter the Rs 100 notes: "))
    notes_50 = int(input("Enter the Rs 50 notes: "))
    notes_20 = int(input("Enter the Rs 20 notes: "))
    notes_10 = int(input("Enter the Rs 10 notes: "))
    total_money = 100*notes_100 + 50*notes_50 + 20*notes_20 + 10*notes_10
    if user_drink == "espresso" or "latte" or "cappuccino":
        if total_money < MENU[user_drink]["cost"]:      #checks wether enough money has been deposited or not
            print(f"Insufficent money added, {total_money} has been refunded.")
        else:
            #checks resources
            if resources["milk"] - MENU[user_drink]["ingredients"]["milk"] < 0 or resources["water"] - MENU[user_drink]["ingredients"]["water"] < 0 or resources["coffee"] - MENU[user_drink]["ingredients"]["coffee"] < 0:
                print(f"Insufficient resources, {total_money} has been refunded.")
                break
            else:
                #final process and transaction
                change = total_money - MENU[user_drink]["cost"]
                resources["milk"] -= MENU[user_drink]["ingredients"]["milk"]
                resources["water"] -= MENU[user_drink]["ingredients"]["water"]
                resources["coffee"] -= MENU[user_drink]["ingredients"]["coffee"]
                if change == 0:
                    print("Enjoy your drink")
                    machine_money += MENU[user_drink]["cost"]
                else:
                    print(f"Here's your change: {change}")
                    print("Enjoy your drink")
                    machine_money += MENU[user_drink]["cost"]


        
