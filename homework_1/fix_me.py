# pylint: disable=missing-module-docstring, missing-function-docstring
def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average


nums = [10, 15, 20]
result = calculate_average(nums)
print("The average is:", result)
