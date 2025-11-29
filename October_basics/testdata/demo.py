# Program to check if a number is prime with input validation

num_input = input("Enter a number: ")

# Validation: check if input contains only digits
if not num_input.isdigit():
    print("❌ Invalid input! Please enter only numeric values (no letters or special characters).")
else:
    num = int(num_input)

    if num <= 1:
        print("Not a prime number")
    else:
        for i in range(2, num):
            if num % i == 0:
                print("Not prime")
                break
        else:
            print("Prime")
