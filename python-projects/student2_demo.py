from student2 import Student

s1 = Student("Jessica", "Kotlarek", 4, 9)
s2 = Student("Lana", "Carboni", 8)
print(s1)
print(s2)

s1.greeting()
s2.greeting()

print(s1.get_energy_level())
s1.take_exam()
print(s1.get_energy_level())
