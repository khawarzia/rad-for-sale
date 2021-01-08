from django.shortcuts import render,redirect
from users.models import User
from django.contrib import auth
from django.core.mail import EmailMessage
from .models import profile
from django.http import Http404
from random import randint
from django.core.files.storage import FileSystemStorage

def home(request):
    if not request.user.is_authenticated:
        return redirect('/signup')
    else:
        return redirect('/home')

def signup(request):
    template = 'login_app/signup2.html'
    context = {}
    if request.method == 'POST':
        objs = User.objects.filter(email=request.POST['email'])
        if len(objs) > 0:
            context['message'] = 'There is already an account registered with this email.'
            return render(request,template,context)
        if request.POST['email'] == '':
            context['message'] = 'Please enter a valid email address.'
            return render(request,template,context)
        obj = User()
        obj.email = request.POST['email']
        obj.username = request.POST['email'].split('@')[0]
        obj.first_name = request.POST['name']
        obj.save()
        obj.set_password(request.POST['pass'])
        obj.save()
        auth.login(request,obj)
        objp = profile()
        objp.user = obj
        objp.save()
        try:
            objp.card_holder = request.POST['holder']
            objp.save()
            objp.card_number = request.POST['number']
            objp.save()
            objp.cvc = request.POST['cvc']
            objp.save()
            objp.expiration_month = request.POST['month']
            objp.save()
            objp.expiration_year = request.POST['year']
            objp.save()
        except:
            pass
        return redirect('/profile')
    return render(request,template,context)

def login(request):
    template = 'login_app/login2.html'
    context = {}
    if request.method == 'POST':
        objs = User.objects.filter(email=request.POST['email'])
        if len(objs) == 0:
            context['message'] = 'No account exists with that email address.'
            return render(request,template,context)
        obj = objs[0]
        if obj.check_password(request.POST['pass']):
            auth.login(request,obj)
            return redirect('/profile')
        else:
            context['message'] = 'Your Password is incorrect.'
            return render(request,template,context)
    return render(request,template,context)

def logout(request):
    auth.logout(request)
    return redirect('/')

def reset_password_first(request):
    template = 'login_app/reset1.html'
    context = {}
    if request.method == 'POST':
        objs = User.objects.filter(email=request.POST['email'])
        if len(objs) == 0:
            context['message'] = 'There is no account with this Email Address.'
            return render(request,template,context)
        obj = objs[0]
        objp = profile.objects.get(user=obj)
        key = ''
        for i in range(16):
            key = key + str(randint(0,20))
        objp.password_key = key
        objp.save()
        obje = EmailMessage(
            subject='Reset your password.',
            body='http://' + str(request.get_host()) + '/new-password/'+key,
            to=[obj.email]
        )
        obje.send()
        context['success'] = 'An email has been sent to your Email Address.'
        return render(request,template,context)
    return render(request,template,context)

def reset_password_second(request,key):
    template = 'login_app/reset2.html'
    context = {}
    if request.method == 'POST':
        try:
            objp = profile.objects.get(password_key=key)
            obj = objp.user
            obj.set_password(request.POST['pass'])
            obj.save()
            objp.password_key = '51523423'
            objp.save()
        except:
            return Http404
        return redirect('/signin')
    return render(request,template,context)

def profile_page(request):
    if not request.user.is_authenticated:
        return redirect('/signin')
    template = 'login_app/profile.html'
    context = {}
    obj = profile.objects.get(user=request.user)
    if request.method == 'POST':
        try:
            image = request.FILES['pic']
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            obj.picture = fs.url(filename)
            obj.save()
        except:
            pass
    context['profile'] = obj
    return render(request,template,context)

def save_profile(request):
    obj = request.user
    objp = profile.objects.get(user=obj)
    try:
        obj.first_name = request.POST['name']
        obj.save()
    except:
        pass
    try:
        obj.email = request.POST['email']
        obj.save()
    except:
        pass
    try:
        objp.phone = request.POST['phone']
        objp.save()
    except:
        pass
    try:
        objp.address = request.POST['address']
        objp.save()
    except:
        pass
    try:
        objp.zip_code = request.POST['zipcode']
        objp.save()
    except:
        pass
    try:
        objp.country = request.POST['country']
        objp.save()
    except:
        pass
    try:
        objp.card_holder = request.POST['holder']
        objp.save()
    except:
        pass
    try:
        objp.card_number = request.POST['number']
        objp.save()
    except:
        pass
    try:
        objp.cvc = request.POST['cvc']
        objp.save()
    except:
        pass
    try:
        objp.expiration_month = request.POST['month']
        objp.save()
    except:
        pass
    try:
        objp.expiration_year = request.POST['year']
        objp.save()
    except:
        pass
    return redirect('/profile')