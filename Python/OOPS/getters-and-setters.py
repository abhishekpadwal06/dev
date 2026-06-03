class User: 
    def __init__(self, name, email, password):
        self.name =  name
        self.email = email
        self.password = password

    def greet(self, user):
        print(f"Saying HI to {user.name}: Hi {user.name}, it's {self.name}!")

user1 = User("Lewis", "lewis44@gmail.com", "abc123")
user2 = User("Max", "max33@gmail.com", "def456")

user1.greet(user2)      # User1 = self()         AND        User2 = user() 
user2.greet(user1)      # User1 = user()         AND        User2 = self()


# Now the problem is that for email we can write anything we want, as there are no rules set up!
# In order to control this, we will make use of getters and setters


class User: 
    def __init__(self, name, email, password):
        self.name =  name
        self._email = email         # A variable is protected by prefixing it with an underscore
        self.password = password
    
    def clean_email(self):
        return self._email.lower().strip()

user1 = User("Lewis", "   LeWiS44@gmail.com   ", "abc123")

print(user1._email)
print(user1.clean_email())


# Since the email field is now protected we should not just modify the email value as we do normally, THAT's WRONG! 

user1._email = "asdlnanf"       # WRONG! NOT ALLOWED THE CODE WILL WORK BUT IT IS WRONG PRACTICE TO DO THIS !! 
print(user1._email)

#  "Developers are trusted to respect the convention of not accessing the underscore prefixed attributes or methods. 
#   Access is not strictly prevented as Python assumes that the developers will act responsibly and won't misuse or accept protected members 
#   unless it's absolutely necessary" - "Adults Consenting" Philosophy by Guildo Van Rossum (Creator of Python)





# Still if we want to make it private, we can do it using double underscore 
# and now it becomes absolutely impossible to access email outside of the class! 





# So what's the difference between _email (protected variable) and __email (private variable / name mangled variable) ?? 
# 1. Both can be acccessed inside the class
# 2. Only protected can be accessed outside the class but as a good python developer we should respect the rule and not access it 





# So what if I have made a variable protected and I want to access or modify that variable outside of the class? 
# For that purpose we will be using getter and setter methods




class User:
    profession = "Formula 1"
    def __init__(self, name, email, password):
        self.name = name
        self._email = email
        self.password = password
    
    def greet(self, user):
        print(f"Hi {user.name}! It's {self.name}")

    def clean_email(self):
        self._email = self._email.lower().strip()
    
    def getMail(self):
        return self._email

    def setMail(self, email):
        self._email = email


user1 = User("Lewis", "   LeWis44@gmail.com   ", "lewis44")
user2 = User("Max", "   MaX33@gmail.com   ", "max33")
user1.clean_email()
user2.clean_email()

user1.greet(user2)
user2.greet(user1)

print(user1.profession)
print(user2.profession)

print(user1.getMail())
user1.setMail("lewishamilton44@gmail.com")
print(user1.getMail())

print(user2.getMail())
user2.setMail("maxverstappen33@gmail.com")
print(user2.getMail())