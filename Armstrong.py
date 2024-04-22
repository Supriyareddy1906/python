def is_armstrong_number(num):
    return num == sum(int(digit) ** len(str(num)) for digit in str(num))


number = int(input("Enter a number: "))
print(f"{number} is an Armstrong number." if is_armstrong_number(number) else f"{number} is not an Armstrong number.")
