
from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name = "apiOverview"),
    path('announcement-list/', views.announcementList, name = "announcementList"),
    path('assignment-list/', views.assignmentList, name = "assignmentList"),
    path('class_test-list/', views.classtestsList, name = "classtestsList"),

    path('announcement-create/', views.announcementCreate, name = "announcementCreate"),
    path('class_test-create/', views.classtestCreate, name = "classtestCreate"),
    path('assignment-create/', views.assignmentCreate, name = "assignmentCreate"),

    path('announcement-update/<str:pk>/', views.announcementUpdate, name = "announcementUpdate"),
    path('assignment-update/<str:pk>/', views.assignmentUpdate, name = "assignmentUpdate"),
    path('class_test-update/<str:pk>/', views.classtestUpdate, name = "classtestUpdate"),

    path('announcement-delete/<str:pk>/', views.announcementDelete, name = "announcementDelete"),
    path('assignment-delete/<str:pk>/', views.assignmentDelete, name = "assignmentDelete"),
    path('class_test-delete/<str:pk>/', views.classtestDelete, name = "classtestDelete"),

#     path('demo-list/', views.DemoList, name = "DemoList"),
#     path('demo-create/', views.DemoCreate, name = "DemoCreate"),
#     path('demo-update/<str:pk>/', views.DemoUpdate, name = "DemoUpdate"),
#     path('demo-delete/<str:pk>/', views.DemoDelete, name = "DemoDelete"),
]