class Person:
    def __init__(self, name):
        self.name = name

    def sayhello(self, to):
        print(f"hello, {to}. I am {self.name}")


rtan = Person("르탄")
rtan.sayhello("병관")