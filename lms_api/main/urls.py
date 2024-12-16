from django.urls import path
from . import views
urlpatterns=[
    path('teacher/',views.TeacherList.as_view()),
    path('teacher/<int:pk>/',views.TeacherDetails.as_view()),
    path('teacher-login',views.teacher_login),

    path('category/',views.CategoryList.as_view()),

    path('course/',views.CourseList.as_view()),

     # Add this pattern for creating and listing chapters
    path('chapter/', views.ChapterList.as_view()),  
    # specific chapter
    # For retrieving, updating, or deleting a specific chapter
    path('chapter/<int:pk>', views.ChapterDetailView.as_view()),
    
    # path('chapter/<int:pk>',views.ChapterDetailView.as_view()),
    # specific course chapter
    path('course-chapter/<int:course_id>',views.CourseChapterList.as_view()),
    # teacher courses
    path('tmycourses/<int:teacher_id>',views.TeacherCourseList.as_view()),
    # course detail
    path('tmycourses-detail/<int:pk>',views.TeacherCourseDetail.as_view())


]