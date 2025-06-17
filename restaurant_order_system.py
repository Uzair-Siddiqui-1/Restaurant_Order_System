from datetime import datetime, time

time_now = datetime.now().time()
formatted_date = datetime.now().strftime("%d-%B-%Y")
formatted_time = time_now.strftime("%H:%M")
start_time = time(12, 0)   # 12:00 PM
end_time = time(18, 0)     # 6:00 PM
dashes_line = "-"

restaurant_menu = {
    "Chicken Karahi": 800,
    "Beef Karahi": 1000,
    "Chicken Biryani": 900,
    "Beef Biryani": 1500,
    "Beef Kabab": 340,
    "Chicken Kabab": 320,
    "Chapati": 50,
    "Paratha": 100,
    "Raita": 150,
    "Pepsi": 300,
    "Water": 200
}

print("\n\n\n\n\n--- WELCOME TO THE ROYAL RESTAURANT! ---")
print("\nThia is a Restaurant Menu:")
print(dashes_line * 26)

i = 1
for meal, price in restaurant_menu.items():
    print(f"{i}. {meal}: {price} Rs.")
    i += 1

user_meal_items_qty = {}
quantity = 0

while True:
    meal_choice = input("\nWhich meal would you like to order?: ").title()

    if meal_choice in restaurant_menu:

        if meal_choice == "Water" or meal_choice == "Pepsi":
            while True:
                try:
                    quantity_of_meal_choice = int(input(f"\nHow many bottles of {meal_choice} would you like? "))
                    quantity += quantity_of_meal_choice
                    break
                except ValueError:
                    print("\nInvalid quantity! Please enter a number only.")
            break
        else:
            while True:
                try:
                    quantity_of_meal_choice = int(input(f"\nHow many {meal_choice} would you like? "))
                    quantity += quantity_of_meal_choice
                    break
                except ValueError:
                    print("\nInvalid quantity! Please enter a number only.")
            break
    else:
        print("\nSorry, the selected meal is not available in the menu!")

user_meal_items_qty.update({meal_choice: quantity_of_meal_choice})
total_cost = restaurant_menu[meal_choice] * quantity_of_meal_choice

while True:
    another_meal_choice = input("\nWould you like to order another meal? Type 'Meal' to continue or 'No' to finish: ").title()

    if another_meal_choice == "No":
        break
    elif another_meal_choice in restaurant_menu:

        if another_meal_choice == "Water" or another_meal_choice == "Pepsi":
            while True:
                try:
                    quantity_of_another_meal_choice = int(input(f"\nHow many bottles of {another_meal_choice} would you like? "))
                    quantity += quantity_of_another_meal_choice
                    break
                except ValueError:
                    print("\nInvalid quantity! Please enter a number only.")
        else:
            while True:
                try:
                    quantity_of_another_meal_choice = int(input(f"\nHow many {another_meal_choice} would you like? "))
                    quantity += quantity_of_another_meal_choice
                    break
                except ValueError:
                    print("\nInvalid quantity! Please enter a number only.")

        user_meal_items_qty.update({another_meal_choice: quantity_of_another_meal_choice})

        total_cost += restaurant_menu[another_meal_choice] * quantity_of_another_meal_choice
    else:
        print("\nSorry, the selected meal is not available in the menu!")

discount = 0
if total_cost > 2000:
    discount += 10

# Applying additional 5% discount for lunch hours (12PM–6PM)
if start_time <= time_now <= end_time:
    discount += 5

final_amount = total_cost - (total_cost * discount / 100)

print("\n\n\n\n\n                  Royal Restaurant")
print("          11/2 Sector-37, PAKISTAN XXXXX")
print("         Ph. No: XXXXXXXXXX - XXXXXXXXXX")
print("    Invoic Number:          IN0001")
print(f"    Invoic Date:            {formatted_date}, {formatted_time}")
print("   ", dashes_line * 43)
print("    Item                  Qty.         Price")
print("   ", dashes_line * 43)
for item, item_qty in user_meal_items_qty.items():
    if (len(item) == 14):
        print(f"    {item}         {item_qty}            {float(restaurant_menu[item]):.2f}")
    elif (len(item) == 11):
        print(f"    {item}            {item_qty}            {float(restaurant_menu[item]):.2f}")
    elif (len(item) == 15):
        print(f"    {item}        {item_qty}            {float(restaurant_menu[item]):.2f}")
    elif (len(item) == 12):
        print(f"    {item}           {item_qty}            {float(restaurant_menu[item]):.2f}")
    elif (len(item) == 7):
        print(f"    {item}                {item_qty}            {float(restaurant_menu[item]):.2f}")
    elif (len(item) == 5):
        print(f"    {item}                  {item_qty}            {float(restaurant_menu[item]):.2f}")
    elif (len(item) == 10):
        print(f"    {item}             {item_qty}            {float(restaurant_menu[item]):.2f}")
    elif (len(item) == 13):
        print(f"    {item}          {item_qty}            {float(restaurant_menu[item]):.2f}")

print("   ", dashes_line * 43)
print(f"    Total Qty:                          {quantity}")
print(f"    Total Price:                        {float(total_cost):.2f}")
print(f"    Discount:                           {discount}%")
print("   ", dashes_line * 43)
print(f"    Final Amount:                       {float(final_amount):.2f}\n\n\n\n\n")
