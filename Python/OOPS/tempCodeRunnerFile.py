class Uni: 
    def __init__(self, name, dept, div):
        self.__name = name      # Private variable
        self._dept = dept       # Protected variable
        self.div = div
    
    def get_name(self):         # Getter method
        return self.__name
            
    def set_name(self, name):         # Setter method
        self.__name = name

stud1 = Uni("Abhishek", "IT", "D")

print(stud1.get_name())         # Getting value
stud1.set_name("Lewis")         # Setting value

print(stud1.get_name())           # Getting new value