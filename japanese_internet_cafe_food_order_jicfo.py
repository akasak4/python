input("Lists Menu (Press Enter)")

foods = ['1. Takoyaki (たこ焼き)', '2. Tonkotsu Ramen (豚骨/とんこつ)', '3. Yakitori (焼き鳥)', '4. Okonomiyaki (お好み焼き)', '5. Curry over rice (カレーライス)' ]

for food in foods:
    print(food)

x = int(input("Enter the number of food you want to order: "))

if x == 1:
    y = foods[0]
    print(f"\nThank you for order {y}")
elif x == 2:
    y = foods[1]
    print(f"\nThank you for order {y}")
elif x == 3:
    y = foods[2]
    print(f"\nThank you for order {y}")
elif x == 4:
    y = foods[3]
    print(f"\nThank you for order {y}")
elif x == 5:
    y = foods[4]
    print(f"\nThank you for order {y}")
else :
    print("Sorry, but your order is not on the List!")

