from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.views.decorators.csrf import csrf_exempt
from .forms import ReaderModeForm

from django.shortcuts import render, redirect, HttpResponseRedirect

# Create your views here.
class SettingsView(generic.View):
        @csrf_exempt
        def user_settings(request):

            if request.method == 'POST':
                form = PasswordChangeForm(request.user, request.POST)
                #form2 = ReaderModeForm(initial={'reader_mode':request.user.custom_user.reader_mode})
                if form.is_valid():
                    user = form.save()
                    update_session_auth_hash(request, user)  # Important!
                    messages.success(request, 'Your password was successfully updated!')
                    return redirect('settings')
                else:
                    messages.error(request, 'Error creating new password, try again.')
            else:
                form = PasswordChangeForm(request.user)
                #form2 = ReaderModeForm(initial={'reader_mode':request.user.custom_user.reader_mode})
            
            form.fields['old_password'].widget.attrs = {'class':'form-control'}
            form.fields['new_password1'].widget.attrs = {'class':'form-control'}
            form.fields['new_password2'].widget.attrs = {'class':'form-control'}
            #form2.fields['reader_mode'].widget.attrs = {'class':'custom-control-input','onclick':'this.form.submit()'}
            return render(request, 'settings.html', {'form':form})

        
        @csrf_exempt
        def reader_mode(request):

            current_user = request.user.custom_user
            if current_user.reader_mode == False:
                current_user.reader_mode = True
                current_user.save()
            else:
                current_user.reader_mode = False
                current_user.save()
            
            print("HELLO THIS CHECKBOX WAS CLICKED")
            print(current_user.reader_mode)

            return redirect('settings')