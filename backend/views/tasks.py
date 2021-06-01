from django.http import HttpResponse
from backend.tasks import send_email, long_work
from django.shortcuts import render


def send_email_task(request):
    email_task_id = send_email.apply_async(queue='email', args=(['some_email@gmail.com'],))
    return HttpResponse(f'The jobs for sending email in progress. Wait for finish. Task id {email_task_id}')


def run_long_task(request):
    ml_task_id = long_work.apply_async(queue='long_task', args=(5,))
    return HttpResponse(f'The job id are: {ml_task_id}')


def list_finished_tasks(request):
    return render(request, 'list.html')