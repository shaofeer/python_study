class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tostring(self):
        return {"name": self.name, "age": self.age}
