from django.db import models

# Create your models here.
#Teacher Model
class Teacher(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100,blank=True,null=True)
    qualification=models.CharField(max_length=100)
    mobile_no=models.CharField(max_length=100)
    skills=models.TextField()
    class Meta:
        verbose_name_plural="1. Teachers"

#Course Category Model
class CourseCategory(models.Model):
    title=models.CharField(max_length=150)
    description=models.TextField()
    class Meta:
        verbose_name_plural="2. CourseCategories"
    def __str__(self):
        return self.title
    
# #Course Model 
class Course(models.Model):
    category=models.ForeignKey(CourseCategory,on_delete=models.CASCADE)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    description=models.TextField()
    featured_img=models.ImageField(upload_to='course_imgs/',blank=True,null=True)
    techs=models.TextField()
    class Meta:
        verbose_name_plural="3. Courses"

 #Chapter Model 
class Chapter(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    description=models.TextField()
    video=models.FileField(upload_to='chapter_videos/', blank=True, null=True)
    remarks=models.TextField()
    class Meta:
        verbose_name_plural="4. Chapters"

# #Student Model
class Student(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)
    mobile_no=models.CharField(max_length=100)
    address=models.TextField()
    intrested_categories=models.TextField()
    class Meta:
        verbose_name_plural=".5 Students"