from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View


class ShowMainPage(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'home/index.html', context)