from django.shortcuts import render

# Create your views here.

def ViewStudentScores(request,test="sample"):
    return render(request,"fct_std_Scores.html")

def AddTestScore(request):
    return render(request,"fct_home.html")