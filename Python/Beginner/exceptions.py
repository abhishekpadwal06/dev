# Simple exception execution
try:
    print(2 / 0)
except ZeroDivisionError:
    print("Cannot divide by Zero!")
finally:
    print(1)



# Raising an exception
# We can raise our own exception (Basically print whatever we want in the terminal when an error occurs)
raise Exception("An error!")



# But if we don't want our program to crash out but also want to raise an exception, we can do this - 
try: 
    raise Exception('An error!')        # Remember only single quotes allowed
except Exception as error:
    print(error)