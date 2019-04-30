from django.shortcuts import render
#from django.http import HttpResponse
from .models import Academic_dept, Academic_class, Upload
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

from .forms import UploadForm
from .models import Upload
from watson import search as watson




def index(request):
    dept_list = Academic_dept.objects.order_by('-dept_code')
    context = {'dept_list': dept_list}
    return render(request, 'wpFiles/index.html', context)
          
def classInDept(request, dept_id):
    dept = get_object_or_404(Academic_dept, pk=dept_id)
    return render(request, 'wpFiles/classInDept.html', {'dept': dept})
    
def uploads(request, class_id):
    academic_class = get_object_or_404(Academic_class, pk=class_id)
    return render(request, 'wpFiles/uploads.html', {'academic_class': academic_class})
    
def uploadFile(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/wpFiles')
    else:
        form = UploadForm()
    return render(request, 'wpFiles/upload.html', {'form': form})

def search(request):
    criteria = request.GET.get('criteria')
    length = len(watson.search(str(request.GET.get('q'))))
    #if length == 0:
    #    return
    if criteria == 'up':
        search_results = watson.filter(Upload, str(request.GET.get('q')))
        return render(request, 'wpFiles/search.html', {'search_results':search_results}) 
    elif criteria == 'de':   
        search_results = watson.filter(Academic_dept, str(request.GET.get('q')))
        return render(request, 'wpFiles/searchDept.html', {'search_results':search_results}) 
    elif criteria == 'co':
        search_results = watson.filter(Academic_class, str(request.GET.get('q')))
        return render(request, 'wpFiles/searchClass.html', {'search_results':search_results}) 
   
    
  
           
        



