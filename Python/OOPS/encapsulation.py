class Player:
    def __init__(self, name, email, password):
        self.name = name
        self._email = email         # email is PROTECTED
        self.__pwd = password   # password is PRIVATE

    def getEmail(self):
        return self._email
    
    def getPwd(self):
        return self.__pwd
    
    def setEmail(self, email):
        self._email = email

    def setPwd(self, password):
        self.__pwd = password
    

p1 = Player("Abhishek", "abhishek@gmail.com", "abhishek123")
# print(p1.name)      Output Printed!       # Correct! No error
# print(p1._email)    Output Printed! BUT THIS IS NOT RIGHT AS THE EMAIL WAS PROTECTED. SHOULD've ACCESSED THROUGH GETTER function
# print(p1.__pwd)   WRONG -> OUTPUT NOT PRINTED -> AS IT IS A PRIVATE MEMBER. CAN ONLY BE ACCESSED WITHIN THE CLASS AND ITS METHODS


print(p1.getEmail())
p1.setEmail("abhishekpadwal06@gmail.com")
print(p1.getEmail())

print(p1.getPwd())
p1.setPwd("Abhishek@0610")
print(p1.getPwd())