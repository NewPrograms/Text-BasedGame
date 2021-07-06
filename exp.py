# Python3 code to demonstrate working of
# Convert Tuple to integer
# Using reduce() + lambda
import functools

# initialize tuple
test_tuple = (9,10, 10)

# printing original tuple
print("The original tuple : " + str(test_tuple))

# Convert Tuple to integer
# Using reduce() + lambda
res = functools.reduce(lambda sub, ele: sub * 10 + ele, test_tuple)

# printing result
print("Tuple to integer conversion : " + str(res))
