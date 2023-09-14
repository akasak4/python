input("Lists Menu (Press Enter)")

foods = ['Takoyaki', 'Tonkotsu Ramen', 'Yakitori', 'Okonomiyaki', 'Curry over rice (カレーライス)' ]

for index, food in enumerate(foods, start=1):
    print(f"{index}. {food}")

order = input("Enter the number of food you want to order: ")
foods.append(order)

print(f"Thank you for ordering {order}, Have a nice day! Itadakimasu!")