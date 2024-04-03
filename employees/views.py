from django.shortcuts import render

# Create your views here.
def dashboard(request):
  context = {
    'segment': 'dashboard'
  }
  return render(request, 'dashboard.html', context)