from django.shortcuts import render,redirect
from .models import Member
from .forms import MemberForm
from django.contrib import messages

def home(request):
    all_members = Member.objects.all
    return render(request,'home.html',{'all': all_members})

def join(request):
    if request.method == 'POST':
        form = MemberForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            password = request.POST['password']
            age = request.POST['age']
            messages.success(request,("There was an error in your form!! Please try again..."))
            #return redirect('join')
            return render(request,'join.html', {'fname' : fname,
                                                'lname' : lname,
                                                'email': email,
                                                'password' : password,
                                                'age': age})

        messages.success(request,("Your responses have been submitted successfully"))
        return redirect('home')

    else:
        return render(request, 'join.html', {})