import datetime
class Person (object):
    def __init__(self, name):
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]
    def getLastName(self):
        """Return self's last name"""
        return self.lastName
    def __str__(self):
        """Return self's name"""
        return self.name
    def setBirthday(self, month, day, year):
        """Set's self's birthday to birthDate"""
        self.birthday = datetime.date(year,month,day)
    def getAge(self):
        """returns self age in days"""
        if self.birthday == None:
            raise ValueError
        else:
            return (datetime.date.today() - self.birthday).days
    def __lt__(self, other):
        """return true if preceding other alphabetically"""
        if self.lastName == other.lastName:
            return self.name < other.Name
        else:
            return self.lastName < other.lastName
    def speak(self,utterance):
        return self.name + " says: " + utterance

class Student(Person):
    nextID = 0
    def __init__(self, name):
        Person.__init__(self, name)
        self.numID = Student.nextID
        Student.nextID += 1
    def speak(self, utterance):
        return Person.speak(self,utterance)
    def __lt__(self, other):
        return self.numID < other.numID


class UG(Student):
    def __init__(self, name, year):
        Student.__init__(self, name)
        self.year = year
    def getClass(self):
        return self.year
    def speak(self, utterance):
        return Student.speak("Yo, " + utterance)

def isStudent(obj):
    if isinstance(obj,Student):
        return True
    return False

class Professor(Person):
    def __init__(self, name, department='None'):
        Person.__init__(self,name)
        self.department = department
    def getDepartment(self):
        return self.department
    def speak(self, utterance):
        newUtterance = "In the " + self.getDepartment()+ " department, we say that "
        return Person.speak(self, newUtterance + utterance)
    def lecture(self, utterance, topic):
        return self.speak(self, utterance) + " and it is obvious that " + topic

UG1 = UG("HEHE", 2020)
S1 = Student("My guy")
S2 = Student("His guy")


classList = [S1,UG1, S2]
for e in classList:
    print(e)
for e in sorted(classList):
    print(e)


#New student subclass --> Unique ID numbers, and SPEAK function, new sorting method (using ID)
#New Undergrad subclass of student --> new speak function, classYear attribute, and year getter method
#IsStudent checking function --> return true or false
#New MIT Professor --> department attribute, unique speak method that includes the department name, and a lecture method that uses the speak method