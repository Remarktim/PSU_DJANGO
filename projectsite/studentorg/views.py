from django.shortcuts import render
from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Q

from django.views.generic.list import ListView

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization, OrgMember, Student, College, Program
from studentorg.forms import OrganizationForm, StudentForm, OrgMemberForm, CollegeForm, ProgramForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch')
class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = 'home.html'

class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = 'organization/org_list.html'
    paginate_by = 5
    
    def get_queryset(self, *args, **kwargs):
         qs = super(OrganizationList, self).get_queryset(*args, **kwargs)
         if self.request.GET.get("q") != None:
             query = self.request.GET.get('q')
             qs = qs.filter(Q(name__icontains=query) |
                            Q(description__icontains=query) |
                            Q(college__college_name__icontains=query))
         return qs
    
class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'organization/org_add.html'
    success_url = reverse_lazy('organization-list')
    
class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'organization/org_edit.html'
    success_url = reverse_lazy('organization-list')
    
class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'organization/org_del.html'
    success_url = reverse_lazy('organization-list')

#####################################################################################
class Org_Member(ListView):
    model = OrgMember
    context_object_name = 'student'
    template_name = 'org_member/org_member.html'
    paginate_by = 5
    
    def get_queryset(self, *args, **kwargs):
        qs = super(Org_Member, self).get_queryset(*args, **kwargs)
        if self.request.GET.get("q") != None:
            query = self.request.GET.get('q')
            qs = qs.filter(Q(student__lastname__icontains=query) |
            Q(student__firstname__icontains=query) | 
            Q(date_joined__icontains=query) | Q(organization__name__icontains=query))
        return qs
    
    
class Org_MemberCreateView(CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'org_member/org_member_add.html'
    success_url = reverse_lazy('orgmember-list')
    
class Org_MemberUpdateView(UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'org_member/org_member_edit.html'
    success_url = reverse_lazy('orgmember-list')
    
class Org_MemberDeleteView(DeleteView):
    model = OrgMember
    template_name = 'org_member/org_member_del.html'
    success_url = reverse_lazy('orgmember-list')
    
#############################################################################
    

class Student_List(ListView):
    model = Student
    context_object_name = 'member'
    template_name = 'student/students.html'
    paginate_by = 5
    
    def get_queryset(self, *args, **kwargs):
        qs = super(Student_List, self).get_queryset(*args, **kwargs)
        if self.request.GET.get("q") != None:
            query = self.request.GET.get('q')
            qs = qs.filter(Q(student_id__icontains=query) |
            Q(lastname__icontains=query) | Q(firstname__icontains=query) | 
            Q(middlename__icontains=query) | Q(program__prog_name__icontains=query) )
        return qs
    
    
class Student_ListCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student/student_add.html'
    success_url = reverse_lazy('student-list')
    
class Student_ListUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student/student_edit.html'
    success_url = reverse_lazy('student-list')
    
class Student_ListDeleteView(DeleteView):
    model = Student
    template_name = 'student/student_del.html'
    success_url = reverse_lazy('student-list')
    
#############################################################################
    

class College_List(ListView):
    model = College
    context_object_name = 'college'
    template_name = 'college/colleges.html'
    paginate_by = 5
    
    def get_queryset(self, *args, **kwargs):
        qs = super(College_List, self).get_queryset(*args, **kwargs)
        if self.request.GET.get("q") != None:
            query = self.request.GET.get('q')
            qs = qs.filter(Q(college_name__icontains=query))
        return qs
    
    
class College_ListCreateView(CreateView):
    model = College
    form_class = CollegeForm
    template_name = 'college/colleges_add.html'
    success_url = reverse_lazy('college-list')
    
class College_ListUpdateView(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = 'college/colleges_edit.html'
    success_url = reverse_lazy('college-list')
    
class College_ListDeleteView(DeleteView):
    model = College
    template_name = 'college/colleges_del.html'
    success_url = reverse_lazy('college-list')
    
#############################################################################
    
class Program_List(ListView):
    model = Program
    context_object_name = 'program'
    template_name = 'program/programs.html'
    paginate_by = 5
    
    def get_queryset(self, *args, **kwargs):
        qs = super(Program_List, self).get_queryset(*args, **kwargs)
        if self.request.GET.get("q") != None:
            query = self.request.GET.get('q')
            qs = qs.filter(Q(prog_name__icontains=query) |
            Q(college__college_name__icontains=query))
        return qs
    
    
class Program_ListCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program/programs_add.html'
    success_url = reverse_lazy('program-list')
    
class Program_ListUpdateView(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program/programs_edit.html'
    success_url = reverse_lazy('program-list')
    
class Program_ListDeleteView(DeleteView):
    model = Program
    template_name = 'program/programs_del.html'
    success_url = reverse_lazy('program-list')
    
    
#############################################################################