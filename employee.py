def calculate_bonus(present_days):
    if present_days >= 26:
        return 5000
    elif present_days >= 20:
        return 3000
    elif present_days >= 15:
        return 1500
    else:
        return 0


if __name__ == "__main__":
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    present_days = int(input("Enter Days Present: "))

    bonus = calculate_bonus(present_days)

    print("\nEmployee Details")
    print("----------------")
    print("ID:", emp_id)
    print("Name:", name)
    print("Present Days:", present_days)
    print("Bonus Amount: ₹", bonus)
