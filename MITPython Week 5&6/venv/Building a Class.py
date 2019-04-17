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


#New student subclass --> Unique ID numbers, and SPEAK function, new sorting method (using ID)
#New Undergrad subclass of student --> new speak function, classYear attribute, and year getter method
#IsStudent checking function --> return true or false
#New MIT Professor --> department attribute, unique speak method that includes the department name, and a lecture method that uses the speak method