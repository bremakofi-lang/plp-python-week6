while True:
    user_input = input("Enter a number: ")
    try:
        number = int(user_input)
        print(f"Thank you! You entered:Your number squared is {number ** 2}")
        break
    except ValueError:
        print("that is not a valid number. Please try again.")
        