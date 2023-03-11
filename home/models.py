from django.db import models

# Create your models here.
class department(models.Model):

    def __str__(self):
        return self.dep_name
        
    dep_name=models.CharField(max_length=50)
    desc=models.TextField()


class doctors(models.Model):
    def __str__(self):
            return self.doc_name + '('+ self.doc_spec +')'

    doc_name=models.CharField(max_length=100) 
    doc_spec=models.CharField(max_length=100)
    dep_name=models.ForeignKey(department,on_delete=models.CASCADE)
    doc_image=models.ImageField(upload_to='doctors')


class booking(models.Model):
    
    def __str__(self):
         return self.p_name
         
    p_name=models.CharField(max_length=100)
    p_age=models.IntegerField()
    p_phone=models.CharField(max_length=10)
    p_email=models.EmailField()
    doc_name=models.ForeignKey(doctors,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)
        
