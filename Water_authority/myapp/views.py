import smtplib

from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from myapp.models import *
from datetime import datetime

# Create your views here.
def login(request):
    return render(request,'login_index.html')

def login_post(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    res=Login.objects.filter(Username=username,Password=password)

    if res.exists():
        res2=Login.objects.get(Username=username,Password=password)
        request.session['lin']='in'
        request.session['lid']=res2.id
        if res2.Type=="admin":
            return HttpResponse('''<Script>alert("Login Sucessfull");window.location="/myapp/adminhome/";</Script>''')
        elif res2.Type == "user":
            return HttpResponse('''<Script>alert("Login Sucessfull");window.location="/myapp/userhome/";</Script>''')
        elif res2.Type == "meterreader":
            return HttpResponse('''<Script>alert("Login Sucessfull");window.location="/myapp/readerhome/";</Script>''')
        elif res2.Type == "Disabled":
            return HttpResponse('''<Script>alert("Your connection has been deactivated. Please ");window.location="/myapp/new_bill_pay/";</Script>''')
        else:
            return  HttpResponse('''<script>alert("Invalid User");window.location="/myapp/login/"</script> ''')
    else:
        return HttpResponse('''<script>alert("invalid Username or Password");window.location="/myapp/login/"</script> ''')



def mainhome(request):
    return render(request,'mainhome.html')



#__________ADMIN_____________________________________________________________________________________________________________________________________________________

#-----------ADMIN HOME ------------------------------------------------------------------------------------------------------------------------------------

def adminhome(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    return render(request,'ADMIN/admin_home_index.html')

def logout(request):
    request.session['lid'] = ''
    request.session['lin'] = 'out'
    return redirect('/myapp/login/')



#ADMIN ADD,VIEW,EDIT METER READER ----------------------------------------------------------------------------------------------------------------------------------------------

def view_public_complaint(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    data=Public.objects.all()
    return render(request,'ADMIN/view_public_complaint.html',{'data':data})

def view_public_complaint_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    fsearch=request.POST['textfield']
    tsearch=request.POST['textfield2']
    ss=Public.objects.filter(Date__range=[fsearch,tsearch])
    return render(request,'ADMIN/view_public_complaint.html',{'data':ss})



def district_add(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    return render(request,'ADMIN/District_add.html')

def district_add_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    district=request.POST['textfield']
    if District.objects.filter(Dis_name__icontains=district).exists():
        return HttpResponse('''<Script>alert("District all ready added");history.back()</Script>''')
    obj=District()
    obj.Dis_name=district
    obj.save()
    return HttpResponse('''<Script>alert("ADDED");window.location="/myapp/district_add/";</Script>''')

def View_District(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    data=District.objects.all()
    return render(request,'ADMIN/view_district.html',{"data":data})

def delete_District(request,id):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    dele=District.objects.filter(id=id).delete()
    return HttpResponse('''<Script>alert("Deleted");window.location="/myapp/View_District/";</Script>''')

def Add_meter_reader(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    return render(request,'ADMIN/Add_meter_reader.html')

def Add_meter_reader_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    name=request.POST['textfield']
    gender=request.POST['RadioGroup1']
    dob=request.POST['textfield5']
    place = request.POST['textfield4']
    district= request.POST['textfield2']
    pincode= request.POST['textfield3']
    photo= request.FILES['fileField']
    email=request.POST['textfield7']
    if Login.objects.filter(Username__icontains=email).exists():
        return HttpResponse('''<Script>alert("Email all ready Exists");history.back()</Script>''')
    phone=request.POST['textfield8']
    fs=FileSystemStorage()
    d="meter_reader/"+datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"
    fn=fs.save(d,photo)

    Lo=Login()
    Lo.Username=email
    Lo.Password=phone
    Lo.Type="meterreader"
    Lo.save()
    obj=Meterreader()
    obj.LOGIN=Lo
    obj.Name=name
    obj.Gender=gender
    obj.Dob = dob
    obj.Place=place
    obj.District=district
    obj.Pincode=pincode
    obj.Photo=fs.url(fn)
    obj.Email=email
    obj.Phone=phone
    obj.save()
    return HttpResponse('''<Script>alert("Meter Reader Added");window.location="/myapp/Add_meter_reader/";</Script>''')


def View_meter_reader(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    data = Meterreader.objects.all()
    return render(request,'ADMIN/View_meter_reader.html',{"data":data})

def View_meter_reader_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    search=request.POST['textfield']
    mm=Meterreader.objects.filter(Name__icontains=search)
    return render(request,'ADMIN/View_meter_reader.html',{'data':mm})

def delete_meter_reader(request,id):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    dele=Meterreader.objects.filter(LOGIN_id=id).delete()
    lob=Login.objects.filter(pk=id).delete()
    return HttpResponse('''<Script>alert("Deleted");window.location="/myapp/View_meter_reader/";</Script>''')

def edit_meter_reader(request,id):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    edit=Meterreader.objects.get(id=id)
    return render(request,'ADMIN/edit_meter_reader.html',{'data':edit})

def edit_meter_reader_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    name=request.POST['textfield']
    gender=request.POST['RadioGroup1']
    dob=request.POST['textfield5']
    place=request.POST['textfield4']
    district=request.POST['textfield2']
    pincode=request.POST['textfield3']
    email=request.POST['textfield7']
    phone=request.POST['textfield8']
    id=request.POST['id']

    if 'fileField' in request.FILES:
        photo=request.FILES['fileField']

        fs = FileSystemStorage()
        d = "meter_reader/" + datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
        fn = fs.save(d, photo)

        obj = Meterreader.objects.get(id=id)
        obj.Name = name
        obj.Gender = gender
        obj.Dob = dob
        obj.Place = place
        obj.District = district
        obj.Pincode = pincode
        obj.Photo = fs.url(fn)
        obj.Email = email
        obj.Phone = phone
        obj.save()
        return HttpResponse('''<Script>alert("UPDATED");window.location="/myapp/View_meter_reader/";</Script>''')
    else:
        obj = Meterreader.objects.get(id=id)
        obj.Name = name
        obj.Gender = gender
        obj.Dob = dob
        obj.Place = place
        obj.District = district
        obj.Pincode = pincode
        obj.Email = email
        obj.Phone = phone
        obj.save()
        return HttpResponse('''<Script>alert("UPDATED");window.location="/myapp/View_meter_reader/";</Script>''')


#ADMIN ADD VIEW EDIT AREA ------------------------------------------------------------------------------------------------------------------
def Add_area(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    res=District.objects.all()
    return render(request,'ADMIN/Add_area.html',{'data':res})



def Add_area_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    district=request.POST['textfield']
    place=request.POST['textfield2']
    if Area.objects.filter(Place__icontains=place).exists():
        return HttpResponse('''<Script>alert("District all ready added");history.back()</Script>''')
    obj=Area()
    obj.District_id=district
    obj.Place=place
    obj.save()
    return HttpResponse('''<Script>alert("Area Added");window.location="/myapp/Add_area/";</Script>''')

def View_area(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    data=Area.objects.all()
    return render(request,'ADMIN/View_area.html',{"data":data})

def View_area_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    search=request.POST['textfield']
    dd=Area.objects.filter(District__Dis_name__icontains=search)
    return render(request,'ADMIN/View_area.html',{'data':dd})

def delete_area(request,id):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    dele=Area.objects.get(id=id).delete()
    return HttpResponse('''<Script>alert("Deleted");window.location="/myapp/View_area/";</Script>''')

def Edit_area(request,id):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    res2 = District.objects.all()
    res=Area.objects.get(pk=id)
    return render(request,'ADMIN/Edit_area.html',{'data':res,'data1':res2})

def Edit_area_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    district=request.POST['textfield']
    place=request.POST['textfield2']
    id=request.POST['id']
    res=Area.objects.filter(pk=id).update(District=district,Place=place)
    return HttpResponse('''<Script>alert("Edited");window.location="/myapp/View_area/";</Script>''')

#ADMIN ASSIGN METER READER---------------------------------------------------------------------------------------------------------------------------------------

def Assign_meter_reader_get(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    res=Meterreader.objects.all()
    res2=Area.objects.all()
    res3 = District.objects.all()
    return render(request,'ADMIN/Assign_meter_reader.html',{'data':res,'data2':res2,'data3':res3})

def Assign_meter_reader_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    meter=request.POST['select']
    mm=Meterreader.objects.get(id=meter)
    # district=request.POST['select2']
    # dd = Area.objects.get(id=district)
    place = request.POST['select3']
    pp=Area.objects.get(id=place)
    if Assign_meter_reader.objects.filter(AREA=pp,METRERREADER=mm).exists():
        return HttpResponse('''<Script>alert("Already assigned");history.back()</Script>''')
    obj=Assign_meter_reader()
    obj.METRERREADER=mm
    obj.AREA=pp
    obj.save()
    return HttpResponse('''<Script>alert("Assigned");window.location="/myapp/Assign_meter_reader_get/";</Script>''')

# def Assign_meter_reader_get(request):
#     district_id = request.GET.get('District')
#     place = Area.objects.filter(dis_id=district_id).values('id', 'place')
#     data = list(place)
#     return (data, safe=False)
#

def View_assigned_mtr_reader(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    res=Assign_meter_reader.objects.all()
    return render(request,'ADMIN/View_assigned_mtr_reader.html',{'data':res})


def View_assigned_mtr_reader_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    search=request.POST['textfield']
    mm=Assign_meter_reader.objects.filter(METRERREADER__Name__icontains=search)
    return render(request,'ADMIN/View_assigned_mtr_reader.html',{'data':mm})

def Edit_assigned_meter_readers(request,id):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    res = Meterreader.objects.all()
    res2 = Area.objects.all()
    assi=Assign_meter_reader.objects.get(id=id)
    return render(request,'ADMIN/Edit_assigned_meter_readers.html',{'data':res,'data1':res2,'data2':assi})


def Edit_assigned_meter_readers_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    meter=request.POST['select']
    mm=Meterreader.objects.get(id=meter)
    # district=request.POST['select2']
    # dd = Area.objects.get(id=district)
    place = request.POST['select2']
    pp=Area.objects.get(id=place)
    id = request.POST['id']

    obj=Assign_meter_reader.objects.get(id=id)
    obj.METRERREADER=mm
    # obj.AREA=dd
    obj.AREA=pp
    obj.save()
    return HttpResponse('''<Script>alert("Edited");window.location="/myapp/View_assigned_mtr_reader/";</Script>''')

def delete_assigned_meter_reader(request,id):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    dele=Assign_meter_reader.objects.get(id=id).delete()
    return HttpResponse('''<Script>alert("Deleted");window.location="/myapp/View_assigned_mtr_reader/";</Script>''')

#ADMIN VIEW NEW CONNECTION--------------------------------------------------------------------------------------------------------------------------------------

# def view_new_conn_report(request):
#     data = Usage.objects.filter(Type="New_connection")
#     return render(request,'ADMIN/view_new_conn_report.html',{"data":data})
#
#
# def view_new_conn_report_post(request):
#     sfrom=request.POST['textfield']
#     sto=request.POST['textfield2']
#     ss=Usage.objects.filter(Date__range=[sfrom,sto])
#     return render(request,'ADMIN/view_new_conn_report.html',{'data':ss})
#
# def new_conn_approve(request,id):
#     app=Usage.objects.filter(id=id).update(ConnectionsStatus="Comfirm")
#     return HttpResponse('''<Script>alert("Confirmed");window.location="/myapp/view_new_conn_report/";</Script>''')

#ADMIN VIEW CONNECTION--------------------------------------------------------------------------------------------------------------------------------------------
def admin_view_connection(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    data = User.objects.filter(ConnectionsStatus="New_connection")
    return render(request,'ADMIN/admin_view_connection.html',{"data":data})

def admin_view_connection_approve(request,id):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    User.objects.filter(LOGIN=id).update(ConnectionsStatus="Active")
    Login.objects.filter(id=id).update(Type='user')
    return HttpResponse('''<Script>alert("Confirmed");window.location="/myapp/admin_view_connection/";</Script>''')

def admin_connection_reject(request,id):
    if request.session['lin'] == 'out':
        return redirect('/myapp/login/')
        User.objects.filter(LOGIN=id).update(ConnectionsStatus="Rejected")
        Login.objects.filter(id=id).update(Type='Rejected')
        return HttpResponse('''<Script>alert("Confirmed");window.location="/myapp/admin_view_connection/";</Script>''')

def admin_view_connection_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    search=request.POST['textfield']
    dd=User.objects.filter(Name__icontains=search,ConnectionsStatus="New_connection")
    return render(request,'ADMIN/admin_view_connection.html',{'data':dd})

def admin_view_approved_connection(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    data = User.objects.filter(ConnectionsStatus='Active')
    return render(request,'ADMIN/admin_view_approved_connection.html',{"data":data})

def admin_view_connection_reject(request,id):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    app2=User.objects.filter(id=id).update(ConnectionsStatus="Rejected")
    return HttpResponse('''<Script>alert("Confirmed");window.location="/myapp/admin_view_connection/";</Script>''')

def admin_view_approved_connection_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    search=request.POST['textfield2']
    dd=User.objects.filter(ConnectionsStatus='Active',Name__icontains=search)
    return render(request,'ADMIN/admin_view_rejected_connections.html',{'data':dd})

def admin_view_rejected_connections(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    data = User.objects.filter(ConnectionsStatus='Rejected')
    return render(request,'ADMIN/admin_view_rejected_connections.html',{"data":data})

def admin_view_rejected_connections_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    search=request.POST['textfield2']
    dd=User.objects.filter(ConnectionsStatus='Rejected',Name__icontains=search)
    return render(request,'ADMIN/admin_view_rejected_connections.html',{'data':dd})

def admin_view_deactive_connection(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    data = User.objects.filter(ConnectionsStatus='Deactive')
    # Login.objects.filter(id=id).update(Type='Disabled')
    return render(request,'ADMIN/admin_view_deactive.html',{"data":data})

def admin_view_deactive_connection_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    search=request.POST['textfield2']
    dd=User.objects.filter(ConnectionsStatus='Deactive',Name__icontains=search)
    return render(request,'ADMIN/admin_view_deactive.html',{'data':dd})


#ADMIN ADD VIEW EDIT CHARGES----------------------------------------------------------------------------------------------------------------------------------------

def Admin_add_Charge(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    return render(request,'ADMIN/Admin_add_Charge.html')

def Admin_add_Charge_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    fromunit=request.POST['textfield']
    tounit=request.POST['textfield2']
    amount=request.POST['textfield3']
    if Charges.objects.filter(Fromunit__icontains=fromunit,Tounit=tounit).exists():
        return HttpResponse('''<Script>alert("All ready Exists");history.back()</Script>''')



    Cs= Charges.objects.all()
    s=True

    for i in Cs:

        if  i.Fromunit> float(fromunit) and float(fromunit) < i.Tounit:
            s=False
            break

        if i.Fromunit > float(tounit) and float(tounit) < i.Tounit:
            s = False
            break


    if s== True:

        obj=Charges()




        obj.Fromunit=fromunit
        obj.Tounit=tounit
        obj.Amount=amount
        obj.save()
        return HttpResponse('''<Script>alert("Charge Added");window.location="/myapp/Admin_add_Charge/";</Script>''')
    else:
        return HttpResponse('''<Script>alert("Charge already exists");window.location="/myapp/Admin_add_Charge/";</Script>''')

def admin_edit_charge(request,id):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    res = Charges.objects.get(id=id)
    return render(request,'ADMIN/admin_edit_charge.html',{'data':res})

def admin_edit_charge_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    fromunit=request.POST['textfield']
    tounit=request.POST['textfield2']
    amount=request.POST['textfield3']
    id=request.POST['id']
    # res=Charges.objects.filter(pk=id).update(Fromunit=fromunit,Tounit=tounit,Amount=amount)
    obj=Charges.objects.get(id=id)
    obj.Fromunit = fromunit
    obj.Tounit = tounit
    obj.Amount = amount
    obj.save()
    return HttpResponse('''<Script>alert("Edited");window.location="/myapp/admin_view_charge/";</Script>''')

def admin_view_charge(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    data = Charges.objects.all()
    return render(request,'ADMIN/admin_view_charge.html',{"data":data})

def delete_charge(request,id):
    dele=Charges.objects.get(id=id).delete()
    return HttpResponse('''<Script>alert("Deleted");window.location="/myapp/admin_view_charge/";</Script>''')


#ADMIN ADD VIEW EDIT NOTIFICATTON-----------------------------------------------------------------------------------------------------------------------------------------------

def admin_view_notification(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    data = Notification.objects.all()
    return render(request,'ADMIN/view_notification.html',{"data":data})

def view_notificationsearch_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    fsearch=request.POST['textfield']
    tsearch=request.POST['textfield2']
    ss=Notification.objects.filter(Date__range=[fsearch,tsearch])
    return render(request,'ADMIN/view_notification.html',{'data':ss})

def Notification_send(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    return render(request,'ADMIN/Notification_send.html')

def Notification_send_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    Noti=request.POST['textarea']
    obj=Notification()
    obj.Notification=Noti
    obj.Date=datetime.now().date()
    obj.save()
    return HttpResponse('''<Script>alert("Notification Sented");window.location="/myapp/Notification_send/";</Script>''')

def Edit_notification(request,did):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    res=Notification.objects.get(id=did)
    return render(request,'ADMIN/Edit_notification.html',{'data':res})

def delete_notification(request,id):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    dele=Notification.objects.get(id=id).delete()
    return HttpResponse('''<Script>alert("Deleted");window.location="/myapp/view_notification/";</Script>''')

def Edit_notification_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    noti=request.POST['Noti']
    did=request.POST['id3']
    # res=Notification.objects.filter(pk=id).update(noti=Notification)
    obj=Notification.objects.get(id=did)
    obj.Notification=noti
    obj.save()
    return HttpResponse('''<Script>alert("Edited");window.location="/myapp/view_notification/";</Script>''')


#ADMIN VIEW AND REPLY COMPLAINT-------------------------------------------------------------------------------------------------------------------------------------------

def view_complaint(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    data = Complaint.objects.all()
    return render(request,'ADMIN/view_complaint.html',{"data":data})

def view_complaint_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    Fsearch=request.POST['textfield']
    Tsearch=request.POST['textfield2']
    return HttpResponse('ok')

def complnt_reply_form(request,id):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    return render(request,'ADMIN/complnt_reply_form.html',{'id':id})

def complnt_reply_form_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    id=request.POST['cid']
    reply=request.POST['textarea']
    obj=Complaint.objects.filter(pk=id).update(Reply=reply,Status='Replied')
    return HttpResponse('''<Script>alert("Replied");window.location="/myapp/view_complaint/";</Script>''')


#ADMIN VIEW DUE REPORT----------------------------------------------------------------------------------------------------------------------------------------------------

def view_due_report(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    data = Usage.objects.filter(Payment_status="pending", USER__ConnectionsStatus='Active')
    return render(request,'ADMIN/view_due_report.html',{"data":data})

def view_due_report_deactivate(request,id):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    dea= User.objects.filter(id=id).update(ConnectionsStatus="Deactive")
    dea2=Usage.objects.filter(USER=id).update(Payment_status="Deactive")
    Login.objects.filter(id=User.objects.get(id=id).LOGIN_id).update(Type='Disabled')
    return HttpResponse('''<Script>alert("Deactivated");window.location="/myapp/view_due_report/";</Script>''')

def view_due_report_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    fsearch=request.POST['textfield']
    tsearch=request.POST['textfield2']
    ss=Usage.objects.filter(Payment_status="pending",Date__range=[fsearch,tsearch])
    return render(request, 'ADMIN/view_due_report.html', {'data': ss})



#ADMIN-CHANGE PASSWORD----------------------------------------------------------------------------------------------------------------------------------------------------

def Change_password_admin(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    return render(request,'ADMIN/Change_password_admin.html')

def Change_password_admin_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    oldpass=request.POST['textfield']
    newpass=request.POST['textfield2']
    confpass=request.POST['textfield3']
    res = Login.objects.filter(id=request.session['lid'], Password=oldpass)
    if res.exists():
        if newpass == confpass:
            ress = Login.objects.filter(id=request.session['lid'], Password=oldpass).update(Password=newpass)
            return HttpResponse('''<Script>alert("Password Updated");window.location="/myapp/login/";</Script>''')
        else:
            return HttpResponse('''<Script>alert("Password Does Not Match");window.location="/myapp/Change_password_admin/";</Script>''')
    else:
        return HttpResponse('''<Script>alert("Invalid");window.location="/myapp/Change_password_admin/";</Script>''')




#____________________________________________________________________________________________________________________________________________________
#__________METER READER _____________________________________________________________________________________________________________________________
def readerhome(request):
    return render(request,'Meter_Reader/reader_home_index.html')

def view_profile_reader(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    res=Meterreader.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'Meter_Reader/view_profile_reader.html',{'data':res})

def view_assigned_area(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    res=Assign_meter_reader.objects.filter(METRERREADER__LOGIN_id=request.session['lid'])
    return render(request,'Meter_Reader/view_assigned_area.html',{'data':res})

def search_customer_usage_entry(request,id):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    res=User.objects.filter(AREA_id=id,ConnectionsStatus="Active")
    return render(request,'Meter_Reader/search_customer_usage_entry.html',{'data':res, 'id':id})

def search_customer_usage_entry_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    search=request.POST['textfield']
    id=request.POST['id']
    res=User.objects.filter(AREA_id=id,ConnectionsStatus="Active",Name__icontains=search)
    return render(request,'Meter_Reader/search_customer_usage_entry.html',{'data':res, 'id':id})

def Usage_entry(request,id):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    return render(request,'Meter_Reader/Usage_entry.html',{'id':id})

def Usage_entry_post(request):
    usage=request.POST['textfield']
    Year=request.POST['select2']
    id2=request.POST['id3']
    Month=request.POST['select1']
    if Usage.objects.filter(Month__icontains=Month, Year=Year, USER_id=id2, Usage__gt=0).exists():
        return HttpResponse('''<Script>alert("This Month usage already entered");history.back()</Script>''')


    amnt=0

    if Usage.objects.filter(USER_id=id2).exists():

        s=Usage.objects.filter(USER_id=id2).order_by('Date')

        s=s[len(s)-1]

        tot= float(usage)- s.Usage


        print(tot)

        Chargesall = Charges.objects.all()

        for i in Chargesall:

            if i.Fromunit <= float(tot) <= i.Tounit:
                amnt = i.Amount


        pass
    else:

        Chargesall= Charges.objects.all()

        for i in Chargesall:

            if i.Fromunit <= float(usage) <= i.Tounit:
                amnt=i.Amount



    obj=Usage()
    import datetime
    date=datetime.datetime.now().date()
    obj.Date=date
    obj.Usage=usage
    obj.Amount=amnt
    obj.Year=Year
    obj.Month=Month
    obj.Payment_status='Pending'
    obj.USER_id=id2
    obj.save()
    return HttpResponse('''<Script>alert("Usage Entered");window.location="/myapp/view_assigned_area/";</Script>''')


def view_notification(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    res=Notification.objects.all()
    return render(request,'Meter_Reader/view_notification.html',{'data':res})

def view_notification_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    fsearch=request.POST['textfield']
    tsearch=request.POST['textfield2']
    res=Notification.objects.filter(Date__range=[fsearch,tsearch])
    return render(request,'Meter_Reader/view_notification.html',{'data':res})

def view_previous_meter_readings(request):

    res= Assign_meter_reader.objects.filter(METRERREADER__LOGIN_id= request.session['lid'])
    l=[]


    for i in res:
        r=Usage.objects.filter(USER__AREA= i.AREA,USER__ConnectionsStatus="Active")

        for j in r:
            l.append(j)
    return render(request,'Meter_Reader/view_previous_meter_readings.html',{'data':l})

def view_previous_meter_readings_post(request):
    fsearch=request.POST['textfield']
    tsearch=request.POST['textfield2']

    res = Assign_meter_reader.objects.filter(METRERREADER__LOGIN_id=request.session['lid'])
    l = []

    for i in res:
        r = Usage.objects.filter(USER__AREA=i.AREA, USER__ConnectionsStatus="Active",Date__range=[fsearch,tsearch])

        for j in r:
            l.append(j)

    # ss=Usage.objects.filter()
    return render(request, 'Meter_Reader/view_previous_meter_readings.html', {'data': l})


def view_user_upload_readings(request):

    a=Assign_meter_reader.objects.filter(METRERREADER__LOGIN_id= request.session['lid'])

    m=[]
    for i in a:

        res=Userupload.objects.filter(USER__AREA=i.AREA)
        for i in res:
            m.append(i)
    return render(request,'Meter_Reader/view_user_upload_readings.html',{'data':m})

def view_user_upload_readings_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    fsearch=request.POST['textfield']
    tsearch=request.POST['textfield2']
    return HttpResponse('ok')


def Change_pass_meter(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    return render(request,'Meter_Reader/Change_pass_meter.html')

def Change_pass_meter_post(request):
    if request.session['lin']=='out':
        return redirect('/myapp/login/')
    oldpass=request.POST['textfield']
    newpass=request.POST['textfield2']
    confpass=request.POST['textfield3']
    # return HttpResponse('ok')
    res = Login.objects.filter(id=request.session['lid'], Password=oldpass)
    if res.exists():
        if newpass == confpass:
            ress = Login.objects.filter(id=request.session['lid'], Password=oldpass).update(Password=newpass)
            return HttpResponse('''<Script>alert("Password Updated");window.location="/myapp/login/";</Script>''')
        else:
            return HttpResponse('''<Script>alert("Password Does Not Match");window.location="/myapp/Change_pass_meter/";</Script>''')
    else:
        return HttpResponse('''<Script>alert("Invalid");window.location="/myapp/Change_pass_meter/";</Script>''')

#_______________________________________________________________________________________________________________________________________________________
#___________USER________________________________________________________________________________________________________________________________________

def userhome(request):
    return render(request,'User/user_home_index.html')

def user_view_profile(request):
    res=User.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'User/user_view_profile.html',{'data':res})


def edit_profile(request):
    edit=User.objects.get(LOGIN_id=request.session['lid'])
    area2=Area.objects.all()
    return render(request,'User/edit_profile.html',{'data':edit,'data1':area2})

def edit_profile_post(request):

    name=request.POST['textfield']
    phone = request.POST['textfield11']
    email = request.POST['textfield10']
    gender = request.POST['RadioGroup1']
    dob = request.POST['textfield2']
    district = request.POST['textfield6']
    Panchayath = request.POST['textfield5']
    village = request.POST['textfield6']
    pincode = request.POST['textfield8']

    if 'fileField' in request.FILES:
        photo=request.FILES['fileField']

        fs = FileSystemStorage()
        d = "user/" + datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
        fn = fs.save(d, photo)

        obj = User.objects.get(LOGIN__id=request.session['lid'])
        obj.Name = name
        obj.Gender = gender
        obj.Dob = dob
        obj.District = district
        obj.Pincode = pincode
        obj.Photo = fs.url(d)
        obj.Email = email
        obj.Phone = phone
        obj.Panchayath=Panchayath
        obj.Village=village
        obj.save()
        return HttpResponse('''<Script>alert("UPDATED");window.location="/myapp/user_view_profile/";</Script>''')
    else:
        obj = User.objects.get(LOGIN__id=request.session['lid'])
        obj.Name = name
        obj.Gender = gender
        obj.Dob = dob
        obj.District = district
        obj.Pincode = pincode
        obj.Email = email
        obj.Phone = phone
        obj.Panchayath = Panchayath
        obj.Village = village
        obj.save()
        return HttpResponse('''<Script>alert("UPDATED");window.location="/myapp/user_view_profile/";</Script>''')





def new_bill_pay(request):
    res = Usage.objects.filter(Q(USER__LOGIN_id=request.session['lid'],Type='Monthly Bill',Payment_status="Pending")|Q(USER__LOGIN_id=request.session['lid'],Type='Monthly Bill',Payment_status="Deactive"))
    return render(request,'User/new_bill_pay.html',{'data':res})

def payment_form(request,id,amnt):
    request.session["usageid"]= id


    return render(request,'User/payment_form.html',{'amnt':amnt})

def payment_form_post(request):
    amount=request.POST['textfield']
    Accountno = request.POST['textfield2']
    ifsc = request.POST['textfield3']
    cvv = request.POST['textfield4']
    usid= request.session["usageid"]

    res=Bank.objects.filter(Accno=Accountno,Ifsc=ifsc,Cvv=cvv)
    if res.exists():
        res1=Bank.objects.get(Accno=Accountno,Ifsc=ifsc,Cvv=cvv)
        if res1.Balance>=amount:


            u=Usage.objects.get(id=usid)
            u.Payment_status="Done"
            u.save()

            pobj=Payment()
            pobj.REQUESTID=Usage.objects.get(id=usid)
            pobj.Date=datetime.now()
            pobj.Amount=amount
            pobj.save()
            tamnt=float(res1.Balance)-float(amount)
            res = Bank.objects.filter(Accno=Accountno, Ifsc=ifsc, Cvv=cvv).update(Balance=tamnt)
            Login.objects.filter(id=request.session['lid']).update(Type='user')
            User.objects.filter(id=request.session['lid']).update(ConnectionsStatus='Active')

            return HttpResponse('''<script>alert('Payment Successfull');window.location="/myapp/userhome/"</script>''')
        else:
            return HttpResponse('''<script>alert('Insufficient Balance');window.location="/myapp/new_bill_pay/"</script>''')
    else:
        return HttpResponse('''<script>alert('Account Not Found');window.location="/myapp/new_bill_pay/"</script>''')


def view_montly_bill(request):
    res = Usage.objects.filter(USER__LOGIN_id=request.session['lid'])
    return render(request,'User/view_montly_bill.html',{'data':res})

def view_montly_bill_post(request):
    fsearch=request.POST['textfield']
    mm=Usage.objects.filter(Month__icontains=fsearch,USER__LOGIN_id=request.session['lid'])
    return render(request,'User/view_montly_bill.html',{'data':mm})

def user_upload(request):
    return render(request,'User/user_upload.html')

def user_upload_post(request):
    upload=request.FILES['fileField']
    fs=FileSystemStorage()
    d="userupload/"+datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"
    fn=fs.save(d,upload)

    obj=Userupload()
    obj.Date = datetime.now().date()
    obj.Photo=fs.url(d)
    obj.USER=User.objects.get(LOGIN__id=request.session['lid'])
    obj.save()
    return HttpResponse('''<Script>alert("UPLOADED");window.location="/myapp/user_upload/";</Script>''')

def Sent_complaint(request):
    edit = User.objects.get(LOGIN_id=request.session['lid'])
    request.session['aid'] = edit.AREA.id
    res = Assign_meter_reader.objects.filter(AREA=request.session['aid'])
    return render(request,'User/Sent_complaint.html',{'data':res})

def complaintform(request,id):
    return render(request,'User/complaintform.html',{'id':id})

def complaintform_post(request):
    id=request.POST['cid']
    complaint=request.POST['textarea']
    obj=Complaint()
    import datetime
    date=datetime.datetime.now().date()
    obj.Date=date
    obj.Complaint=complaint
    obj.Status='pending'
    obj.Reply='Pending'
    obj.FROM=User.objects.get(LOGIN=request.session['lid'])
    obj.TO_id=id
    obj.save()
    return HttpResponse('''<Script>alert("Complaint Sent");window.location="/myapp/Sent_complaint/";</Script>''')





def user_change_pass(request):
    return render(request,'User/user_change_pass.html')

def user_change_pass_post(request):
    oldpass=request.POST['textfield']
    newpass=request.POST['textfield2']
    confpass=request.POST['textfield3']
    res = Login.objects.filter(id=request.session['lid'], Password=oldpass)
    if res.exists():
        if newpass == confpass:
            ress = Login.objects.filter(id=request.session['lid'], Password=oldpass).update(Password=newpass)
            return HttpResponse('''<Script>alert("Password Updated");window.location="/myapp/login/";</Script>''')
        else:
            return HttpResponse('''<Script>alert("Password Does Not Match");window.location="/myapp/Change_pass_meter/";</Script>''')
    else:
        return HttpResponse(
            '''<Script>alert("Invalid");window.location="/myapp/Change_pass_meter/";</Script>''')

#____________PUBLIC________________________________________________________________________________________________________________________________

def New_conn(request):
    res=Area.objects.all()
    return render(request,'Public/signup_index.html',{'data':res})

def New_conn_post(request):
    name=request.POST['textfield']
    gender = request.POST['RadioGroup1']
    dob = request.POST['textfield2']
    # place = request.POST['textfield4']
    area=request.POST['select']
    panchayath = request.POST['textfield5']
    village = request.POST['textfield6']
    # district = request.POST['textfield7']
    pincode = request.POST['textfield8']
    email = request.POST['textfield10']
    if Login.objects.filter(Username__icontains=email).exists():
        return HttpResponse('''<Script>alert("Email all ready Exist");history.back()</Script>''')
    phone = request.POST['textfield11']
    newpass=request.POST['textfield16']
    confpass=request.POST['textfield17']
    photo = request.FILES['fileField']
    Accno=request.POST['textfield18']
    ifsc=request.POST['textfield19']
    cvv=request.POST['textfield20']
    amt=request.POST['textfield21']

    if newpass==confpass:


        ress=Bank.objects.filter(Accno=Accno,Ifsc=ifsc,Cvv=cvv)
        if ress.exists():
            resss = Bank.objects.get(Accno=Accno, Ifsc=ifsc, Cvv=cvv)
            if resss.Balance>amt:
                tamount=float(resss.Balance)-float(amt)
                ress = Bank.objects.filter(Accno=Accno, Ifsc=ifsc, Cvv=cvv).update(Balance=tamount)

                fs=FileSystemStorage()
                d="user/"+datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"
                fn=fs.save(d,photo)

                Lo=Login()
                Lo.Username=email
                Lo.Password=confpass
                Lo.Type="pending"
                Lo.save()
                obj=User()
                obj.LOGIN=Lo
                obj.Name=name
                obj.Gender=gender
                obj.Dob = dob
                # obj.Place=place
                obj.Panchayath=panchayath
                obj.Village=village
                obj.ConnectionsStatus="New_connection"
                # obj.District=district
                obj.Pincode=pincode
                obj.Photo=fs.url(fn)
                obj.Email=email
                obj.Phone=phone
                obj.AREA=Area.objects.get(id=area)
                obj.save()
                from datetime import date
                todays_date = date.today()



                obj2=Usage()
                obj2.Date=datetime.now().date()
                obj2.Usage=0
                obj2.Month=datetime.now().strftime("%B")
                obj2.Year=todays_date.year
                obj2.USER=obj
                obj2.Type="New_Connection"
                obj2.Payment_status="Done"
                obj2.Amount="750"
                obj2.save()

                request.session["uid"]=obj.id
                request.session["usage_id"]=obj2.id
                request.session["lid"]=Lo.id
                return HttpResponse('''<Script>alert("Successfull");window.location="/myapp/login/";</Script>''')
            else:
                return HttpResponse('''<Script>alert("Insufficient Balance");window.location="/myapp/New_conn/";</Script>''')
        else:
            return HttpResponse(
                '''<Script>alert("Account Not Found");window.location="/myapp/New_conn/";</Script>''')
    else:
        return HttpResponse('''<Script>alert("Password Missmatch");window.location="/myapp/New_conn/";</Script>''')


def New_conn_payment(request):
    return render(request,'Public/payment.html')

def pub_complaint_sent(request):
    return render(request,'Public/complaint_index.html')

def pub_complaint_sent_post(request):
    email=request.POST['textfield']
    complaint=request.POST['textarea']

    obj=Public()
    obj.Date=datetime.now().date()
    obj.email=email
    obj.Complaint=complaint
    obj.status='Pending'
    obj.save()

    return HttpResponse('''<Script>alert("Sented");window.location="/myapp/login/";</Script>''')

def forget_pass(request):
    return render(request,'forgot_index.html')

def forget_pass_post(request):
    email=request.POST['textfield']
    qry = Login.objects.filter(Username=email)
    if not qry.exists():
        return HttpResponse('''<Script>alert("User Not Found");window.location="/myapp/login/";</Script>''')

    else:
        import random
        new_pass = random.randint(0000, 9999)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("akashmappoyil123@gmail.com", "iytv urhn nhrc xlma")  # App Password

        to = email
        subject = "Test Email"
        body = "Your new password is " + str(new_pass)
        msg = "Subject: {subject}\n\n{body}"
        server.sendmail("s@gmail.com", to, msg)

        # Disconnect from the server
        server.quit()
        qryy = Login.objects.filter(Username=email).update(Password=new_pass)

        return HttpResponse('''<Script>alert("Please Check Your Email");window.location="/myapp/login/";</Script>''')