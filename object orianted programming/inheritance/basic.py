# single inheritance
class Person:
    def walk(self):
        print("person is walking")
    def read(self):
        print("person is reading")
class Student(Person):
    def exam(self):
        print("student is attending exam")
pe=Person()
pe.walk()
pe.read()
st=Student()
st.exam()
st.read()
st.walk()


