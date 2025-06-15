number = int(input("Enter a number to see its multiplication table:"))
for item in range(1, 11):
    result = number * item
    print(f"{number} * {item} = {result}")