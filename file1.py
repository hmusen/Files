try:
    num = int(input("Enter a number: "))  # try converting input to int

    print(f"\nMultiplication Table of {num}") # concatenate input num as {num}
    for i in range(1, 11):  # loop from 1 to 10
        print(f"{num} x {i} = {num * i} ✅")

except ValueError:
    print("❌ Invalid input! Please enter a valid number.")