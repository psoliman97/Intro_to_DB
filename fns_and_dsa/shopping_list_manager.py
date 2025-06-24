def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main ():
    shopping_list = []
    while True:
        display_menu()
        choice = input('Enter your choice number: ').strip()

        if choice == '1':
            item = input('Enter the item to add : ')
            shopping_list.append(item)
            print(f"'{item}' has been added to your shopping list.")

        elif choice == '2':
            choice = input('remove your Item: ').strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed to your shopping list.")
            else :
                print(f"Item '{item}' is not found in the list ")

        elif choice == '3':
            if shopping_list:
                print("\nYour Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else :
                print('Your shoppoing list is empty. ')

        elif choice == '4':
            print('Goodbye')
            break
        
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
