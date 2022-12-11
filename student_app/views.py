from django.shortcuts import render, redirect
import requests
import json

# Create your views here.

def Subject_List(request):
    try:
        branch=request.session['branch']
        if(branch==None):
            return redirect("login")

        resp_data=requests.get("http://localhost:3000/subject/branchSubjects/"+branch)
        print(resp_data.text)
        resp_data_json=json.loads(resp_data.text)
        subjects_List=resp_data_json['message']
        if(subjects_List=="Error"):
            subjects_List=[]
        
        return render(request,"std_home.html",{"subjects": subjects_List})
    except:
        print("Error occurred in get Subject List")
    return render(request,"std_home.html")

def Student_Subject_Score(request,subject,test="sample"):
    print(subject,test)
    return render(request,"std_subject_score.html")