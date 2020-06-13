from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def home(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pass')
        context = {
            'user': username,
            'pass': password,
                   }
        print(username)
        print(password)
        return render(request, 'login/log.html', context)
    return render(request, 'login/index.html')