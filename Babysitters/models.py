from django.db import models


class Available(models.Model):
    Name = models.CharField(max_length=25)
    Picture = models.ImageField(upload_to='profiles', null=False, blank=False)
    Age = models.IntegerField()
    Number = models.IntegerField()
    Date = models.DateField(auto_now_add=True)
    Description = models.CharField(max_length=300)
    Availability = models.CharField(max_length=200)
    Address = models.CharField(max_length=90)
    Skills = models.CharField(max_length=200)
    Education = models.CharField(max_length=100)
    Email = models.EmailField()





class AvailableMultan(models.Model):
    Name = models.CharField(max_length=25)
    Picture = models.ImageField(upload_to='profiles', null=False, blank=False)
    Age = models.IntegerField()
    Number = models.IntegerField()
    Date = models.DateField(auto_now_add=True)
    Description = models.CharField(max_length=300)
    Availability = models.CharField(max_length=200)
    Address = models.CharField(max_length=90)
    Skills = models.CharField(max_length=200)
    Education = models.CharField(max_length=100)
    Email = models.EmailField()





class AvailableIslamabad(models.Model):
    Name = models.CharField(max_length=25)
    Picture = models.ImageField(upload_to='profiles', null=False, blank=False)
    Age = models.IntegerField()
    Number = models.IntegerField()
    Date = models.DateField(auto_now_add=True)
    Description = models.CharField(max_length=300)
    Availability = models.CharField(max_length=200)
    Address = models.CharField(max_length=90)
    Skills = models.CharField(max_length=200)
    Education = models.CharField(max_length=100)
    Email = models.EmailField()





class AvailableGujranwala(models.Model):
    Name = models.CharField(max_length=25)
    Picture = models.ImageField(upload_to='profiles', null=False, blank=False)
    Age = models.IntegerField()
    Number = models.IntegerField()
    Date = models.DateField(auto_now_add=True)
    Description = models.CharField(max_length=300)
    Availability = models.CharField(max_length=200)
    Address = models.CharField(max_length=90)
    Skills = models.CharField(max_length=200)
    Education = models.CharField(max_length=100)
    Email = models.EmailField()





class AvailableKarachi(models.Model):
    Name = models.CharField(max_length=25)
    Picture = models.ImageField(upload_to='profiles', null=False, blank=False)
    Age = models.IntegerField()
    Number = models.IntegerField()
    Date = models.DateField(auto_now_add=True)
    Description = models.CharField(max_length=300)
    Availability = models.CharField(max_length=200)
    Address = models.CharField(max_length=90)
    Skills = models.CharField(max_length=200)
    Education = models.CharField(max_length=100)
    Email = models.EmailField()





class AvailableSialkot(models.Model):
    Name = models.CharField(max_length=25)
    Picture = models.ImageField(upload_to='profiles', null=False, blank=False)
    Age = models.IntegerField()
    Number = models.IntegerField()
    Date = models.DateField(auto_now_add=True)
    Description = models.CharField(max_length=300)
    Availability = models.CharField(max_length=200)
    Address = models.CharField(max_length=90)
    Skills = models.CharField(max_length=200)
    Education = models.CharField(max_length=100)
    Email = models.EmailField()





class AvailablePeshawar(models.Model):
    Name = models.CharField(max_length=25)
    Picture = models.ImageField(upload_to='profiles', null=False, blank=False)
    Age = models.IntegerField()
    Number = models.IntegerField()
    Date = models.DateField(auto_now_add=True)
    Description = models.CharField(max_length=300)
    Availability = models.CharField(max_length=200)
    Address = models.CharField(max_length=90)
    Skills = models.CharField(max_length=200)
    Education = models.CharField(max_length=100)
    Email = models.EmailField()




class AvailableGujrat(models.Model):
    Name = models.CharField(max_length=25)
    Picture = models.ImageField(upload_to='profiles', null=False, blank=False)
    Age = models.IntegerField()
    Number = models.IntegerField()
    Date = models.DateField(auto_now_add=True)
    Description = models.CharField(max_length=300)
    Availability = models.CharField(max_length=200)
    Address = models.CharField(max_length=90)
    Skills = models.CharField(max_length=200)
    Education = models.CharField(max_length=100)
    Email = models.EmailField()


class Register(models.Model):
    Name = models.CharField(max_length=100)
    CNIC = models.IntegerField()
    Address = models.CharField(max_length=100)
    Phone = models.IntegerField()
    Email = models.EmailField()
    Childage = models.CharField(max_length=100)
    Hours = models.CharField(max_length=100)

    
