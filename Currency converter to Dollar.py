inputer = int(input('Amount:'))
method = input("choose is it (p)ound, (E)uro, (B)irr, (R)enminbi: ").upper()
if method == "B":
    converted = inputer / 34.40
    print(f"It is ${converted} ")
elif method == "P":
    converted = inputer * 2.31
    print(f"It is ${converted} ")
elif method == "E":
    converted = inputer * 1.18
    print(f"It is ${converted} ")
elif method == "R":
    converted = inputer / 6.98
    print(f"It is ${converted}")
else:
    print("Sorry, i can't uderstand that")
