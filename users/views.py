from django.shortcuts import redirect, render
from django.http import request
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm,UserEditForm
# Create your views here.

@login_required
def dashboard(request):
	context = {
		"welcome":"welcome to your dashboard"
	}
	return render(request, 'asset/index.html',context=context)

def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST or None)
		if form.is_valid():
			new_user = form.save(commit=False)
			new_user.set_password(form.cleaned_data.get('password'))
			new_user.save()
			return render(request,'usersapp/register_done.html')

	else:
		form = UserRegistrationForm()

	context = {
		'form':form
		}

	return render(request,'asset/register.html',context = context)

@login_required
def edit(request):
	if request.method == 'POST':
		user_form = UserEditForm(instance=request.user,data=request.POST)
		if user_form.is_valid():
			user_form.save()
			return redirect('dashboard')
	else:
		user_form = UserEditForm(instance=request.user)
		context = {
		'form':user_form,
		}

		return render(request,'asset/profile.html',context = context)
