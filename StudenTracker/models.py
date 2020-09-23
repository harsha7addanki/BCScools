from django.db import models

# Create your models here.

class Assignment(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    duedate = models.TimeField()

    def __str__(self):
        return f"{self.name}: due: {self.duedate}"

class Student(models.Model):
    name = models.CharField(max_length=40)
    firedrillnumber = models.IntegerField()
    work = models.ManyToManyField(Assignment,blank=True,null=True)
    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name

class Classroom(models.Model):
    roomNumber = models.CharField(primary_key=True,max_length=4)
    students = models.ManyToManyField(Student)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.roomNumber} {self.teacher.name}"


