from django.db import models

class SearchTerm(models.Model):
    q = models.CharField(max_length=50)
    search_date = models.DateTimeField(auto_now_add=True)
    ip_address = models.IPAddressField()
    #user = models.ForeignKey(User, null=True)
    def __unicode__(self):
        return self.q
# Create your models here.
