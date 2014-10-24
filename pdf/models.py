from django.db import models
from django.contrib.auth.models import User

class AccessCode(models.Model):
    code = models.CharField(max_length=30)
    user = models.ForeignKey(User, unique=False)
    date_of_release = models.DateTimeField(null=True)
    
    def __str__(self):
            return '%s' % (self.code)
            
    def save(self, *args, **kwargs):
            for field_name in ['code']:
                val = getattr(self, field_name, False)
                if val:
                    setattr(self, field_name, val.upper())
            super(AccessCode, self).save(*args, **kwargs)

class AccessCodeTracking(models.Model):
    access_code = models.ForeignKey(AccessCode, unique=False)
    date_accessed = models.DateTimeField(auto_now=True, null=True)
    action = models.CharField(max_length=30, null=True)