from tkinter import scrolledtext


class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, track, score):
        self.name = name
        self.age = int(age)
        self.track = list(track) 
        self.score = float(score)
        pass
    def change_name(self, name):
        self.name = name
    def change_age(self, age):
        self.age = int(age)        
    def add_track(self, track):
        self.track.append(track)
    def get_score(self):
        return self.score

Bob = Student(name="Bob", age=26, track=["FE","BE"], score=20.90)

print(Bob.age)
print(Bob.score)
print(Bob.track)
print(Bob.score)

# Expected methods
Bob.change_name("Peter")
print(Bob.name)
Bob.change_age(34)
print(Bob.age)
Bob.add_track("UI/UX")
print(Bob.track)
Bob.get_score()
print(Bob.score)