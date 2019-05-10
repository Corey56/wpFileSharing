from django.test import TestCase
from wpFiles.models import Academic_dept, Academic_class, Upload
# Create your tests here.

class Academic_deptTests(TestCase):
    def test_is_dep(self):
        dep_real = Academic_dept.objects.get(dept_code="EECS")
        self.assertIs(dep_real, True)
        dep_fake = Academic_dept(dept_code="DEL")
        self.assertIs(Academic_dept.objects.get(dept_code="DPE"), False)
