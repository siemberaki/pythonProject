class pet :
    def __init__ (self,name,age):
        self.name = name
        self.age = age


class dog(pet):
    def speak(self):
        print("woowwww")


class cat(pet):
    def speak(self):
        print("bark")