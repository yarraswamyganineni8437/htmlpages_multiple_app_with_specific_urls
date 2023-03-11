from django.shortcuts import render

# Create your views here.
def sample(request):
    return render(request,'app2sample1.html')

def sample2(request):
    return render(request,'app2sampl2.html')
