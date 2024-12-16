from rest_framework import serializers
from . import models

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
       model=models.Teacher
       fields=['id','full_name','email','password','qualification','mobile_no','skills']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
       model=models.CourseCategory
       fields=['id','title','description']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
       model=models.Course
       #fields = '_all_' 
       fields=['id','category','teacher','title','description','featured_img','techs']
       extra_kwargs = {
           'featured_img': {'required': False}  # Make 'image' optional
        }

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
       model=models.Chapter
       #fields = '_all_' 
       fields=['id','course','title','description','video','remarks']
       extra_kwargs = {
            'video': {'required': False}  # Make 'video' optional
        }