from django.shortcuts import render


def main(request):
    return render(request, 'job/main.html')