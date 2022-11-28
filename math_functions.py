def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    return a / b

def power(a, b):
    return a**b

def modulus(a, b):
    return a % b

if __name__ == "__main__":
    print ("Adding:", add_numbers(2, 4))
    print ("subtracting:", subtract_numbers(9, 2))
    print ("Multiplying:", multiply_numbers(2, 3))
    print ("Dividing:", divide_numbers(10, 2))
    print ("Power:", power(2,3))
    print("Mod:", modulus(7,5))
