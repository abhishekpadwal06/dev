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