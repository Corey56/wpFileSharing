

from django.test import TestCase
from wpFiles.models import Academic_dept, Academic_class, Upload
# Create your tests here.

class Academic_deptTests(TestCase):
    def test_is_dep(self):
        Academic_dept.objects.create(dept_code="EECS", dept_name="Electrical Engineering and Computer Sciences")
        aca_dep = Academic_dept(dept_code="EECS")
        self.assertIs(str(aca_dep), "EECS") #1st
        self.assertFalse(Academic_dept.objects.get(dept_code="XYZ")) #second test

# the above tests create a department and confirms that it either is or is not an actual academic department
#EECS should pass and XYZ should fail


class Academic_classTest(TestCase):
    def test_is_class(self):
        Academic_class.objects.create(class_code="IT341",dept_code="EECS",
                              class_name="Social Engineering")
        aca_class = Academic_class(class_code="IT341")
        self.assertTrue(aca_class) #third test

#the above test similarly creates a class and verifies that it is actually a class object
