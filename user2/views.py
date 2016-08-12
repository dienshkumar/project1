import datetime
from django.shortcuts import render, redirect
from django.conf import settings
# Create your views here.
from user2.models import Student1,Student2
def index_1(request ):
#dispaly the data using the code
    temp2 = Student1.objects.all()
    temp3=Student2.objects.all()#(address_name="doctor")
    #temp3=Student2.objects.filter(student1__father_name="sdfo",address_name="hyderabad")
    #temp3=temp3.filter(address_name="hyderabad")


    #temp1 = Student1.objects.values_list("father_name")
    print temp3
    print temp2
    return render(request, 'Details.html', {"temp": temp3})# linking purpose using in "temp"


def index(request):
    if request.method=='POST':
        file_1=request.FILES['upload']
        filename=settings.MEDIA_ROOT+"images/"+file_1.name
        with open(filename,'wb+') as destination:
            for chunk in file_1.chunks():
                destination.write(chunk)
        father_name=request.POST['fathername']
        mather_name=request.POST['mathername']
        vaccination=request.POST['vaccination']
        price=request.POST['price']
        auther_name = request.POST['authername']
        address_name = request.POST['addressname']
        date = request.POST['date']
        print father_name
        print mather_name
        print vaccination
        print price
        #temper variables
        temp=Student1()
        temp.father_name=father_name
        temp.mather_name=mather_name
        temp.vaccination=vaccination
        temp.price=price
        temp.save()
        #temper variables
        temp2 = Student2()
        temp2.student1=temp#forigen key relations
        temp2.auther_name = auther_name
        temp2.address_name = address_name
        temp2.date = datetime.datetime.now()
        temp2.save()

        temp.save()
        return redirect("/user2/details")
    return  render(request,'login.html')

#def index_4(request):
#    if request.method=='POST':
#        request.FILES
