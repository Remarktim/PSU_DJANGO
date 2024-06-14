"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from studentorg.views import *
from studentorg import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
    path('chart/', views.chart_view, name='chart'),
    path('organization_list', OrganizationList.as_view(), name='organization-list'),
    path('organization_list/add', OrganizationCreateView.as_view(), name='organization-add'),
    path('organization_list/<pk>', OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization_list/<pk>/delete', OrganizationDeleteView.as_view(), name='organization-delete'),
    
    path('orgmember-list', Org_Member.as_view(), name='orgmember-list'),
    path('orgmember-list/add', Org_MemberCreateView.as_view(), name='orgmember-add'),
    path('orgmember-list/<pk>', Org_MemberUpdateView.as_view(), name='orgmember-update'),
    path('orgmember-list/<pk>/delete', Org_MemberDeleteView.as_view(), name='orgmember-delete'),
    
    path('student-list', Student_List.as_view(), name='student-list'),
    path('student-list/add', Student_ListCreateView.as_view(), name='student-add'),
    path('student-list/<pk>', Student_ListUpdateView.as_view(), name='student-update'),
    path('student-list/<pk>/delete', Student_ListDeleteView.as_view(), name='student-delete'),
    
    path('college-list', College_List.as_view(), name='college-list'),
    path('college-list/add', College_ListCreateView.as_view(), name='college-add'),
    path('college-list/<pk>', College_ListUpdateView.as_view(), name='college-update'),
    path('college-list/<pk>/delete', College_ListDeleteView.as_view(), name='college-delete'),
    
    path('program-list', Program_List.as_view(), name='program-list'),
    path('program-list/add', Program_ListCreateView.as_view(), name='program-add'),
    path('program-list/<pk>', Program_ListUpdateView.as_view(), name='program-update'),
    path('program-list/<pk>/delete', Program_ListDeleteView.as_view(), name='program-delete'),
    
    re_path(r'^login/$', auth_views.LoginView.as_view(
        template_name='login.html'), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

]
