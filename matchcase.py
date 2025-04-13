print("Match Case")
try:
    day=int(input("Enter the number between 1-7:"))
    match day:
        case 1:
            print(f"{day}st input is Monday")
        case 2:
            print(f"{day}nd input is Tuesday")
        case 3:
            print(f"{day}rd input is Wednesday")
        case 4:
            print(f"{day}th input is Thursday")
        case 5:
            print(f"{day}th input is Friday")
        case 6:
            print(f"{day}th input is Saturday")
        case 7:
            print(f"{day}th input is Sunday")
        case _:
            print("Invalid input,expected inputs are between 1-7!")
    print("-------------------------------")
    print("Program has been ended!")
except ValueError:
    print("Only int values are accepted!")

