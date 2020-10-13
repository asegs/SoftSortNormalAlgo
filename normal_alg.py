import math

"""
Works great for midrange numbers and even 5 digit, breaks down around zero because the standard deviations become close to 0.
Currently have a janky fix for it.
"""

def getNormalZ2O(expected_value,actual_value,harshness=3,test=False):
    standard_dev = expected_value/harshness
    if standard_dev<1 and standard_dev>-1:
        standard_dev = 1
    if harshness==0:
        harshness = 0.1
    if test:
        result = 1/(standard_dev*math.sqrt(2*math.pi))
        if result==0:
            return 0.0001
        return result
    first_term = 1/(standard_dev*math.sqrt(2*math.pi))
    second_term = -math.pow((actual_value-expected_value),2)/(2*math.pow(standard_dev,2))
    multiplier = 1/(getNormalZ2O(expected_value,expected_value,harshness,True))
    return multiplier*first_term*math.exp(second_term)

print(getNormalZ2O(10,10,3))

print(getNormalZ2O(0,1,5))
