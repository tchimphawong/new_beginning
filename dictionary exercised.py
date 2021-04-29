phone = input("Phone: ")
phone_numbers = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for character in phone:
    output += phone_numbers.get(character, "!") + " "
