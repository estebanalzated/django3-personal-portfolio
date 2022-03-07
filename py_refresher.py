class Dog:

    def __init__(self, name="", age=0, furcolor=""):
        self.name = name
        self.age = age
        self.furcolor = furcolor

    def bark(self):
        print("BARK!")


mydog = Dog("Latte", 13, "White")

print(mydog.age)
