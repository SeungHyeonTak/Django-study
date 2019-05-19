from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic.list import ListView


class UserList(ListView):
    User = get_user_model()
    template_name = 'accounts/user_list.html'

from .forms import SignUpForm
def signup(request):
    if request.method == "POST":
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            user_instance = signup_form.save(commit = False)
            user_instance.set_password(signup_form.cleaned_data['password'])
            user_instance.save()

            return render(request, 'accounts/signup_complete.html', {'username':user_instance.username})
    else:
        signup_form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form':signup_form})