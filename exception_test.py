""" exeception_test.py:  test the try/catch type code """

try:
    a= 5
    b = 99
    ave = a/b;
    

except ZeroDivisionError:
    print("divide zero error ")
else:
    print(f"ave = {ave}") 