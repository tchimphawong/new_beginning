weight = input("Weight: ")
convert = input("(L)bs or (K)g: ")
if convert.lower() == "k":
    print(f"You are {int(weight) // 0.45} pounds")
elif convert.lower() == "l":
    print(f"You are {int(weight) * 0.45} kilograms")
