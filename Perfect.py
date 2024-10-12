import math

def isPerfectSquare(num):
    # Find the square root of the number
    sqrt_num = math.isqrt(num)
    
    # If the square of sqrt_num equals num, it is a perfect square
    return sqrt_num * sqrt_num == num

# Example usage
num = 16
if isPerfectSquare(num):
    print(f"{num} is a perfect square.")
else:
    print(f"{num} is not a perfect square.")
