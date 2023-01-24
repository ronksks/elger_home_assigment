# Recursive Digit “Summer”
# Write a function to find the sum of all digits in a given arbitrary number.
# ● ✅Please use recursion for the solution 👍
# ● 🚫No conversion to strings, loops or other old fashioned stuff 👎
# Example:
# input: 2347623
# output: 27 (=2+3+4+7+6+2+3)

# def recursive_digit_summer(num, sum):
#     if num < 1:
#         return num
#     return (sum = sum + recursive_digit_summer(num / 10))
# --------------------------------------------------------------
def recursive_digit_summer(num):
    if num:
        sum = num % 10 + recursive_digit_summer(int(num / 10))
    else:
        sum = 0
    return sum


print(recursive_digit_summer(2347623))
