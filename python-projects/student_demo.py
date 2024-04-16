from student import Student

student1 = Student("Jess", "Kotlarek", 10)
print(student1)

student1.greeting()

print(student1.get_energy_level())
student1.take_exam()
print(student1.get_energy_level())
