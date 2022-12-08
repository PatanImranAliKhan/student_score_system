from django.shortcuts import render, redirect

# Create your views here.

def Subject_List(request):
    try:
        print
        branch=request.session['branch']
        if(branch==None):
            return redirect("login")
        curser=""
        subjects_list=curser.execute("get all subjects of the above branch")
        if(subjects_list==None):
            return render(request,"std_home.html")
        return render(request,"std_home.html",{"subjects_list": subjects_list})
    except:
        print("Error occurred in get Subject List")
    return render(request,"std_home.html")

def Student_Subject_Score(request,subject,test="sample"):
    print(subject,test)
    return render(request,"std_subject_score.html")