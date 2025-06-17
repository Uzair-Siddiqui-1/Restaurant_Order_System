from datetime import datetime, time

time_now = datetime.now().time()
formatted_date = datetime.now().strftime("%d-%B-%Y")
formatted_time = time_now.strftime("%H:%M")
start_time = time(12, 0)   # 12:00 PM
end_time = time(18, 0)     # 6:00 PM

# menu_heading = "\nThis is a Menu:"
# line = '-'

# restaurant_menu = {
#     "Chicken Karahi": 800,
#     "Beef Karahi": 1000,
#     "Chicken Biryani": 900,
#     "Beef Biryani": 1500,
#     "Chapati": 50,
#     "Paratha": 100,
#     "Raita": 150,
#     "Pepsi": 300,
#     "Water": 200
# }

# print("\n--- Welcome to the Restaurant! ---")
# # print("Menu")
# # menu_keyword = "Menu"

# while True:
#     menu_input = input("\n'Menu' type kren: ").capitalize()

#     if menu_input == "Menu":
#         print(menu_heading)
#         print(line * 35)

#         for meal, price in restaurant_menu.items():
#             print(f"{meal}: {price} Rs.")
#         break
#     else:
#         print("\nSyntax Error! Please type (Menu)")

# meal_choice = input("\nAp konsa meal lena pasand karenge?: ").title()

# if meal_choice in restaurant_menu:
#     quantity_meal_1 = int(input(f"\nAp ko kitne {meal_choice}s chahiyen? "))

#     total_cost = restaurant_menu[meal_choice] * quantity_meal_1

#     current_time = datetime.now()
#     time_of_day = current_time.strftime("%H:%M")

#     discount = 0
#     if total_cost > 2000:
#         discount += 10

#     if "13:00" <= time_of_day <= "16:00":
#         discount += 5

#     final_amount = total_cost - (total_cost * discount / 100) # ye discount nikalne ka formula hai

#     print(f"\nTotal Cost: Rs {float(total_cost):.2f}")
#     print(f"\nDiscount: {discount}%")
#     print(f"\nFinal Price: Rs {final_amount:.2f}")
# else:
#     print("\nmaaf kijeye, aapka select kiya gaya meal menu mein nahi hai!")

# user_meal_items_qty = {}
# meal_choice = input("\nAap konsa meal lena pasand karenge?: ").title()
# quantity_of_meal_choice = int(input(f"\nAap ko kitni {meal_choice} ki Bottle chahiyen? "))
# user_meal_items_qty.update({meal_choice: quantity_of_meal_choice,})
# while True:
#     another_meal_choice = input("\nAap dobara konsa meal lena pasand karenge? agar meal dobara lena hai, to 'Meal' choose karke type karein warna 'No' type karein: ").title()
#     quantity_of_another_meal_choice = int(input(f"\nAap ko kitni {another_meal_choice} chahiyen? "))

#     user_meal_items_qty.update({another_meal_choice: quantity_of_another_meal_choice})

#     print(user_meal_items_qty)

#     if another_meal_choice == "No":
#         break

a = "Chicken Kabab"
print(len(a))