from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from datetime import date
# Create your models here.
levels = (
    ('R', 'Red'),  #
    ('G', 'Green'),
    ('B', 'Blue'),  # client
)

dapertments = (
    ("M","Managment"),
    ("D","Designers"),
    ("P","machines")
)

design_type = (
    ("A","Attached Design"),
    ("O","Office Design")
)

state = (
    ("D","Ideal"),
    ("I","in Progress"),
    ("F","Finished")
)

class Users(models.Model) :
    id = models.AutoField(primary_key=True , auto_created=True)
    user =models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=255 , null= False)
    department=models.CharField(max_length=1 ,  choices=dapertments , null= False)

    def __str__(self):
        return self.name

class clients(models.Model):
    id = models.AutoField(primary_key=True , auto_created=True)
    name = models.CharField(max_length=255 , default= None)
    phone_number = models.CharField(max_length=255 , default= None)
    notes = models.CharField(max_length=255 , default= None ,  null=True)
    clientlevel = models.CharField(max_length=1 ,  choices=levels ,default='B')
    def __str__(self):
        return self.name

class orders(models.Model):
    order_id = models.AutoField(primary_key=True , auto_created=True)
    user_id = models.ForeignKey(Users ,  on_delete=models.CASCADE)
    client_id = models.ForeignKey(clients , on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    recived_date = models.DateField()
    '''
    use of date 
    # datetime.date
    d = datetime.date(1997, 10, 19)
    '''
    delivery_date = models.DateField()
    # attatched or office
    design_types = models.CharField(max_length=1 , choices=design_type ,null= False)
    # E://test
    design_path = models.CharField(max_length=255 , null=True)
    # list of designs ex -> logo , bussiness card , etc .
    design_category = models.JSONField(blank =True , default=list )
    # indoor , out door
    printing_type = models.JSONField(blank =True , default=list)
    size_width = models.FloatField(null=True)
    size_high = models.FloatField(null=True)
    materials = models.CharField(max_length=255 ,null= True )
    color = models.CharField(max_length=255 ,null= True )
    thickness = models.FloatField(null=True)
    Post_print_services = models.JSONField(blank =True , default=list)
    state = models.CharField(max_length=1 , choices=state ,null=False , default= "D")
    notes = models.CharField(max_length=255, default="" , null= True)
    def __str__(self):
        return str(self.order_id)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
