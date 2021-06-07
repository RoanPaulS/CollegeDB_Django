from django.shortcuts import render
from django.http import HttpResponse
from collegeApp.models import CollegeStudent

# Create your views here.

def display_data(request):
    collegeName = "Univeral College Of Engineering & Technology"
    collegeData = CollegeStudent.objects.all()

    display_data = {"college":collegeName , "college_list":collegeData}
    return render(request , 'college.html' , context = display_data)