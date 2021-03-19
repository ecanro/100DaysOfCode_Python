class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

    def swin(self):
         print("splash!")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        super().swin()
        print("moving in water.")


nemo = Fish()
nemo.breathe()
nemo.swin()