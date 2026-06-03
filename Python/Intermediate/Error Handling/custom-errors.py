a = int(input("Enter any value between 1 and 10: "))

if(a<1 or a>10):
    raise ValueError("Value should be between 1 and 10")