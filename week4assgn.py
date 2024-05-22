class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, I'm {self.name}, {self.age} years old, and my gender is {self.gender}.")

# Create an instance of the Person class
person = Person("Java", 30, "Male")

# Call the introduce method to display the person's information
person.introduce()