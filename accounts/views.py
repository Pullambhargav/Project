from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.http import JsonResponse
from .models import Order
from django.views.decorators.csrf import csrf_exempt  # Ensure this import is present

# View for the index page (login)
def index(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    
    return render(request, 'index.html', {'form': form})

# View for user registration
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})

# View for the home page
def home(request):
    return render(request, 'home.html')
def order_food(request):
    return render(request,'order_food.html')

# View for the order page
@csrf_exempt  # Only for development; remove in production for security
def order_food(request):
    if request.method == 'POST':
        food_name = request.POST.get('food_name')
        table_number = request.POST.get('table_number')
        person_name = request.POST.get('person_name')

        # Validate input
        if not food_name or not table_number or not person_name:
            return JsonResponse({'error': 'Please provide all fields.'}, status=400)

        # Save order to the database
        order = Order(food_name=food_name, table_number=table_number, person_name=person_name)
        order.save()
        return JsonResponse({'message': 'Order placed successfully!'})

    return JsonResponse({'error': 'Invalid request method.'}, status=400)