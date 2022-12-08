from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

def CheckData(request):
    try:
        a=request.session['id']
        print(a)
        if a is None:
            return None
        else:
            pro=request.session['profession']
            if(pro=="studnet"):
                return redirect("")
            elif pro=="faculty":
                return redirect("")
            return pro
    except:
        return None

def HomePage(request):
    try:
        CheckData(request)
    except:
        return render(request,'home.html')
    return render(request,'home.html')

def RegisterPage(request):
    return render(request,'register.html')

def LoginPage(request):
    if request.method=="POST":
        id=request.POST['id']
        password=request.POST['password']
        if id=="admin@gmail.com" and password=="admin":
            return redirect("add_branch")
        category=request.POST['category']
        if(category==None):
            return render(request,'login.html',{'error':'Please select the category'})
        if category=="student":
            try:
                std=object
                print("hello student")
                print(std)
                if std.length!=0:
                    # AddSession(request, u)
                    request.session['profession']='student'
                    return redirect('subjectlist')
                else:
                    return render(request,'login.html',{'error':'invalid email or password'})
            except:
                return render(request,'login.html',{'error':'invalid email or password'})
        else:
            try:
                faclt=object
                print(faclt)
                print("faculty")
                if faclt!=None:
                    if faclt.assign=="True":
                        # AddSession(request, a)
                        request.session['profession']='faculty'
                        return redirect('appr_home')
                    else:
                        return render(request, 'invaliduser.html')
                else:
                    return render(request,'login.html',{'error':'invalid password'})
            except:
                return render(request,'login.html',{'error':'invalid email or password'})
        return render(request,'login.html')

    return render(request,"login.html")

def StudentRegister(request):
    if(request.method=="POST"):
        try:
            print("student req, POST")
            id=request.POST['id']
            email=request.POST['email']
            username=request.POST['username']
            branch=request.POST['branch']
            password=request.POST['password']
            curser=""
            a=curser.execute("")
            if(a==None):
                print("new user")
                curser.execute("add new user")
                curser.execute("increament student count to 1 for the above branch")
                return redirect("login")
            else:
                print("old user")
                return render(request,'studentRegister.html',{'error':'This Id was already registered'})
        except:
            return render(request,"studentRegister.html")
    CheckData(request)
    return render(request,"studentRegister.html")

def FacultyRegister(request):
    if(request.method=="POST"):
        try:
            print("student req, POST")
            id=request.POST['id']
            email=request.POST['email']
            username=request.POST['username']
            branch=request.POST['branch']
            password=request.POST['password']
            curser=""
            a=curser.execute("")
            if(a==None):
                print("new user")
                curser.execute("ad new faculty")
                curser.execute("increament student count to 1 for the above branch")
                return redirect("login")
            else:
                print("old user")
                return render(request,'facultyregister.html',{'error':'This Id was already registered!!'})
        except:
            return render(request,"facultyregister.html")
    CheckData(request)
    return render(request,"facultyregister.html")

def AddSession(request,detail):
    request.session['username']=detail.username
    request.session['email']=detail.email
    request.session['id']=detail.id
    request.session['branch']=detail.branch