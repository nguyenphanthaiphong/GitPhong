from django.shortcuts import render, redirect
from .models import Property, Image
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm, PropertyForm, ImageForm, PropertyImageForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.db import transaction

# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'register.html', {'form': form})
#
# def home(request):
#     return render(request, 'home.html')
#
#
# def role_required(role):
#     def decorator(view_func):
#         def _wrapped_view_func(request, *args, **kwargs):
#             if request.user.role == role:
#                 return view_func(request, *args, **kwargs)
#             else:
#                 return HttpResponse('Unauthorized', status=401)
#         return _wrapped_view_func
#     return decorator
#
# @login_required
# @role_required('admin')
# def admin_dashboard(request):
#     return HttpResponse('Welcome admin!')
#
# @login_required
# @role_required('seller')
# def landlord_dashboard(request):
#     return HttpResponse('Welcome Chu Thue Tro!')
#
# @login_required
# @role_required('buyer')
# def tenant_dashboard(request):
#     return HttpResponse('Welcome Nguoi Dung!')
#
# def create_property(request):
#     if request.method == 'POST':
#         property_form = PropertyForm(request.POST)
#         image_form = PropertyImageForm(request.POST, request.FILES)
#         files = request.FILES.getlist('images')
#         if property_form.is_valid():
#             with transaction.atomic():
#                 property_instance = property_form.save()
#                 for file in files:
#                     # Assuming you have a way to handle the file and get URL
#                     image_instance = Image.objects.create(property=property_instance, image_url=file.url)
#                     property_instance.images.add(image_instance)
#                 property_instance.save()
#             return redirect('property_list')
#     else:
#         property_form = PropertyForm()
#         image_form = PropertyImageForm()
#     return render(request, 'create_property.html', {'property_form': property_form, 'image_form': image_form})
#
# def property_list(request):
#     properties = Property.objects.all()
#     return render(request, 'property_list.html', {'properties': properties})