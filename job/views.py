from django.shortcuts import render


def main(request):
    return render(request, 'job/main.html')


def projects(request, project_id):
    return render(request, f'job/projects/{project_id}.html')


def education(request):
    return render(request, 'job/education.html')