from project_multiple_inheritence.employee import Employee
from project_multiple_inheritence.person import Person


class Teacher(Person, Employee):

    def teach(self):
        return 'teaching...'
