from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework import status
from django.contrib import messages

from estates.models import Estate
from rentalAgreements.models import RentalAgreement
from .models import User
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .serializers import UserSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from .serializers import UserSerializer 

class RegisterView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()  
            user.password = make_password(serializer.validated_data['password'])  
            user.save()
            
            return redirect("login_page")
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return render(request, 'auth/login.html')

    def post(self, request):
        username = request.POST.get('username')  
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
            print("User found in DB: ", user)
        except User.DoesNotExist:
            user = None
            print("User does not exist in DB.")
        
        if user is not None:
            user = authenticate(request, username=username, password=password)
            print("Here is the authenticated user: ", user)
            if user is not None:
                login(request, user)
      
                refresh = RefreshToken.for_user(user)
                
                response = redirect('dashboard')
                response.set_cookie(key='access_token', value=str(refresh.access_token), httponly=True)
                response.set_cookie(key='refresh_token', value=str(refresh), httponly=True)
                
                return response
            else:
                print("Authentication failed.")
                return render(request, 'auth/login.html', {'error': 'Invalid credentials'})
        else:
            return render(request, 'auth/login.html', {'error': 'User does not exist'})


def logout_view(request):
    logout(request)
    return redirect('login_page')


def custom_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login_page')
        return view_func(request, *args, **kwargs)
    return wrapper



@login_required
def dashboard_view(request):
    if request.user.role == 'admin':
        # Get admin's estates and agreements
        estates = Estate.objects.filter(owner=request.user)
        agreements = RentalAgreement.objects.filter(owner=request.user)
        
        # Calculate available and rented estates
        available_estates = [estate for estate in estates if estate.is_available]
        rented_estates = [estate for estate in estates if not estate.is_available]

        context = {
            # Estate statistics
            'total_estates': estates.count(),
            'available_estates': len(available_estates),
            'rented_estates': len(rented_estates),

            # Agreement statistics
            'total_agreements': agreements.count(),
            'active_agreements': agreements.filter(status='active').count(),
            'pending_agreements': agreements.filter(status='pending').count(),
            'terminated_agreements': agreements.filter(status='terminated').count(),
            'expired_agreements': agreements.filter(status='expired').count(),

            # Recent items (ordered by id since created_at doesn't exist)
            'recent_estates': estates.order_by('-id')[:5],
            'recent_agreements': agreements.order_by('-start_date')[:5],  # Using start_date instead of created_at
            'is_admin': True
        }
    
    elif request.user.role == 'client':
        # Get client's agreements and related estates
        agreements = RentalAgreement.objects.filter(tenant=request.user)
        
        context = {
            # Agreement statistics
            'total_agreements': agreements.count(),
            'active_agreements': agreements.filter(status='active').count(),
            'pending_agreements': agreements.filter(status='pending').count(),
            'terminated_agreements': agreements.filter(status='terminated').count(),
            'expired_agreements': agreements.filter(status='expired').count(),
            
            # Recent agreements (ordered by start_date)
            'recent_agreements': agreements.order_by('-start_date')[:5],
            'is_admin': False
        }
    
    else:
        messages.error(request, "You don't have permission to access the dashboard.")
        return redirect('login_page')

    return render(request, 'dashboard.html', context)

def login_page(request):
    return render(request, 'auth/login.html')


def register_page(request):
    return render(request, 'auth/register.html')

