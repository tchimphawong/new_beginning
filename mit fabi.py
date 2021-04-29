weight = input("Weight: ")
convert = input("(L)bs or (K)g: ").lower()
if convert == "k":
    convert_weight = int(weight) // 0.45
    print(f"You are {convert_weight} pounds")
elif convert == "l":
    convert_weight = int(weight) * 0.45
    print(f"You are {convert_weight} kilograms")
else:
    print("Wrong unit!")