from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from accountapp.models import HelloWorld


def hello_world(request):
    if request.method == "POST":

        temp = request.POST.get('input')

        new_data = HelloWorld()
        new_data.text = temp
        new_data.save()



        return HttpResponseRedirect(reverse('accountapp:hello_world')) # 해당하는 경로를 다시 만들어주는 함수 reverse()

    else:
        data_list = HelloWorld.objects.all()  # DB에서 object 객체를 all 모두 긁어온다 이런식으로 데이터베이스 긁어온다
        return render(request, 'accountapp/hello_world.html',
                      context={'data_list': data_list})

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accoutapp:hello_world') # 클래스에서 경로를 다시만들어주는 함수를 reverse_lazy()
    template_name = 'accountapp/create.html'  # 어느 html file을 이용할지
