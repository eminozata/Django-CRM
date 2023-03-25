from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record, Actions

# Create your views here.
def home(request):
    records = Record.objects.all()

    name_query = request.GET.get('name')
    city_query = request.GET.get('city')
    experience_query = request.GET.get('experience')
    skills_query = request.GET.get('skills')

    if is_valid_queryparam(name_query):
        records = records.filter(firstName__icontains=name_query)
    if is_valid_queryparam(city_query):
        records = records.filter(city__icontains=city_query)
    if is_valid_queryparam(experience_query):
        records = records.filter(experience__icontains=experience_query)
    if is_valid_queryparam(skills_query):
        records = records.filter(skills__icontains=skills_query)




    # check login
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in')
            return redirect('home')
        else:
            messages.error(request, 'Error logging in')
            return redirect('home')
        
    else:
        return render(request, 'home.html', {'records': records})
    

def is_valid_queryparam(param):
    return param != '' and param is not None
    

def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have successfully registered! ' + username)
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    
    return render(request, 'register.html', {'form': form})


def customer_record(request, pk):

    username = request.user.username
    action = 'VIEWED'
    action = Actions(username=username, action=action)
    action.save()


    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'record': record})
    else:
        messages.error(request, 'You must be logged in to view this page')
        return redirect('home')


def delete_record(request, pk):

    username = request.user.username
    action = 'DELETED'
    action = Actions(username=username, action=action)
    action.save()

    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        record.delete()
        messages.success(request, 'Record deleted')
        return redirect('home')
    else:
        messages.error(request, 'You must be logged in to view this page')
        return redirect('home')
    
def add_record(request):

    username = request.user.username
    action = 'ADDED'
    action = Actions(username=username, action=action)
    action.save()

    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, 'Record added')
                return redirect('home')
        return render(request, 'add.html', {'form': form})
    else:
        messages.error(request, 'You must be logged in to view this page')
        return redirect('home')
    

def update_record(request, pk):

    username = request.user.username
    action = 'UPDATED'
    action = Actions(username=username, action=action)
    action.save()
    
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=record)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Record updated')
                return redirect('home')
        return render(request, 'update.html', {'form': form})
    else:
        messages.error(request, 'You must be logged in to view this page')
        return redirect('home')
    

