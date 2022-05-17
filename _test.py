from company import Company
from file import File
from parser import Parser
from person import Person

import unittest

class TestStringMethods(unittest.TestCase):

    def test_payEmployeeRENE(self):
        test={'RENE': {'MO': '10:00-12:00', 'TU': '10:00-12:00', 'TH': '01:00-03:00', 'SA': '14:00-18:00', 'SU': '20:00-21:00'}}
        person=Person(list(test.keys())[0])
        company=Company()    
        self.assertTrue(company.payEmployee(person,test[person.getName()]) == 215)

    def test_payEmployeeASTRID(self):
        test={'ASTRID': {'MO': '10:00-12:00', 'TH': '12:00-14:00', 'SU': '20:00-21:00'}}
        person=Person(list(test.keys())[0])
        company=Company()    
        self.assertTrue(company.payEmployee(person,test[person.getName()]) == 85)


if __name__ == '__main__':
    unittest.main()
