from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm, CreateForm
from .models import Form
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.conf import settings
import random
import string

def generate_form_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))

def main_page(request):
    user_forms = Form.objects.filter(user=request.user)
    if user_forms:
        return render(request, 'main_page.html', {'user_forms': user_forms})
    else:
        return redirect('login')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('create_form')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('create_form')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def create_form(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.form_id = generate_form_id() 
            new_form.save()
            return redirect('form_detail', form_id=new_form.form_id)
    else:
        form_id = generate_form_id() 
        form = CreateForm()
    return render(request, 'create_form.html', {'form': form, 'form_id': form_id})

def form_detail(request, form_id):
    form = Form.objects.get(form_id=form_id)
    return render(request, 'form_detail.html', {'form': form, "request": request})

@csrf_exempt
def handle_form_submission(request, form_id):
    if request.method == 'POST':
        try:
            form = Form.objects.get(form_id=form_id)
        except Form.DoesNotExist:
            return JsonResponse({'error': 'Invalid form ID'}, status=404)

        try:
            email_subject = f'New submission for form {form_id}'
            email_body = 'Data submitted:\n' + '\n'.join([f'{key}: {value}' for key, value in request.POST.items()])
            send_mail(email_subject, email_body, settings.EMAIL_HOST_USER, [form.email])
            return JsonResponse({'message': 'Form submission successful'})
        except Exception as e:
            return JsonResponse({'error': f'Error sending email: {e}'}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)