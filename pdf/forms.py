from django import forms
from pdf.models import AccessCode
from django.utils import timezone

class AccessCodeForm(forms.Form):
    access_code = forms.CharField(label='Access Code', max_length=100)


    def is_valid(self):
        valid = super(AccessCodeForm, self).is_valid()

        if not valid:
            return valid

        try:
            code = AccessCode.objects.get(code=self.cleaned_data['access_code'].upper())
            if(code.date_of_release > timezone.now()):
                self._errors['access_code'] = ['Access code not available at this time']
                return False
            
        except AccessCode.DoesNotExist:
            self._errors['access_code'] = ['Invalid access code']
            return False

        return True
 
    def get_access_code(self):
        return self.cleaned_data['access_code']
