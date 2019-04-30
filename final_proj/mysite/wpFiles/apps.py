from django.apps import AppConfig
from watson import search as watson


class WpfilesConfig(AppConfig):
    name = 'wpFiles'
    def ready(self):
        Upload = self.get_model("Upload")
        Dept = self.get_model("Academic_dept")
        Course = self.get_model("Academic_class")
        watson.register(Upload)
        watson.register(Dept)
        watson.register(Course)
        
