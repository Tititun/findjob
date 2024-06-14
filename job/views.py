from django.shortcuts import render


def main(request):
    print(request.headers)
    return render(request, 'job/main.html')