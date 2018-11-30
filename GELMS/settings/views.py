from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect, HttpResponseRedirect

# Create your views here.
class SettingsView(generic.View):

        def user_settings(request):

            if request.method == 'POST':
                form = PasswordChangeForm(request.user, request.POST)
                if form.is_valid():
                    user = form.save()
                    update_session_auth_hash(request, user)  # Important!
                    messages.success(request, 'Your password was successfully updated!')
                    return redirect('settings')
                else:
                    messages.error(request, 'Error creating new password, try again.')
            else:
                form = PasswordChangeForm(request.user)
            
            form.fields['old_password'].widget.attrs = {'class':'form-control'}
            form.fields['new_password1'].widget.attrs = {'class':'form-control'}
            form.fields['new_password2'].widget.attrs = {'class':'form-control'}

            return render(request, 'settings.html', {'form':form})
