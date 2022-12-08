from django.shortcuts import render, redirect

# Create your views here.
def AdminAddBranch(request):
    message=None
    error=None
    try:
        error=None
        message=None
        if(request.method=="POST"):
            print("post req")
            branch=request.POST['branch']
            curser=""
            alrdreg = curser.execute("check branch was laready registered or not")
            if(alrdreg==None):
                try:
                    c = curser.execute("add new branch ")
                    message="New Branch Added Successfully"
                except:
                    error="Some error occurred Please try After some time"
            else:
                error="Branch was already Exist"
        
        curser=""
        allbranch=curser.execute("get all branches information")
        if(allbranch==None):
            return render(request,"add_branch.html",{"error": error,"message":message})
        else:
            return render(request,"add_branch.html",{"allbranches": allbranch,"error": error,"message":message})
        
    except:
        return render(request,"add_branch.html",{"error": error,"message":message})

def AddSubject(request):
    error=None
    message=None
    try:
        error=None
        message=None
        if(request.method=="POST"):
            subject=request.POS['subject']
            branch=request.POST['branch']
            curser=""
            checksub=curser.execute("check subject already exist in that branch or not ?")
            if(checksub==None):
                print("add subject")
                curser.execute("Add new subject to the above branch")
                message="Subject Added Successfully"
                
            else:
                return render(request,"add_subject.html",{"error": "Subject laready exist in the branch"})
        allsubjects=curser.execute("get all subjects")
        if(allsubjects==None):
            return render(request,"add_subject.html",{"error": error,"message":message})
        else:
            return render(request,"add_subject.html",{"allsubjects": allsubjects,"error": error,"message":message})
    except:
        print("Add Subject Error");
        return render(request,"add_subject.html",{"error": error,"message":message})

def ViewFacultyDetails(request):
    try:
        print()
        curser=""
        getfacdet = curser.execute("get all faculty details")
        if(getfacdet==None):
            return render(request,"faculty_details.html")
        else:
            return render(request,"faculty_details.html",{"faculty_details": getfacdet})
    except:
        print("error in view faculty")
    return render(request,"faculty_details.html")

def AssignNewFaculty(request):
    message = None
    error = None
    try:
        error=None
        message=None
        if(request.method=="POST"):
            print("assign faculty")
            subject=request.POST['subject']
            assign=request.POST["assign"]
            if(assign=="True"):
                id=request.POST.get("savedetails")
                print(id)
                curser=""
                mes=curser.execute("update the assign in faculty details to True")
                message="Faculty Assigned Successfuly"
        
        print("get fac")
        curser=""
        fac_det=curser.execute("get faculty where assign=false")
        if(fac_det==None):
            return render(request,"new_faculty.html",{"error": error,"message":message})
        else:
            faculty_details=[]
            for i in fac_det:
                all_subjects=curser.execute("get all subjects of i.branch")
                faculty_details.append({
                    "id": i.id,
                    "email":i.email,
                    "username": i.username,
                    "branch":i.branch,
                    "subjects": all_subjects  
                })
            return render(request,"new_faculty.html",{"new_faculty": faculty_details,"error": error,"message":message})
    except:
        print("Error in assign new faculty")
    return render(request,"new_faculty.html",{"error": "Error in assign new faculty","message":message})