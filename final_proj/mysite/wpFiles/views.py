from django.shortcuts import render
from django.http import HttpResponse
from .models import Academic_dept, Academic_class, Upload
# Create your views here.

def index(request):
    dept_list = Academic_dept.objects.order_by('-dept_code')
    output = "\n".join([d.dept_code for d in dept_list])
    return HttpResponse(output)
    
def classInDept(request, dept_code):
    class_list = []
    for each in Academic_class.objects:
        if each.dept_code == dept_code:
            class_list.append(each)
    template = loader.get_template('wpFiles/index.html')
    context = {
        'class_list': class_list,
    }
    #output = "\n".join([c.class_code for c in class_list])
    return HttpResponse(template.render(context, request))
    
def detail(request, upload_id):
    return HttpResponse("youre looking at %." % upload_id)
    
    #latest_upload_list = Upload.objects.order_by('-upload_date')
    #output = ', '.join([u.alias for u in latest_upload_list])
    #return HttpResponse(output)
