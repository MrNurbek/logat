from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, View
from main.form import *
from .models import Word
from django.http import HttpResponseRedirect

class HomePageView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countWords'] = Word.objects.all().count()
        context['title'] = 'Bosh sahifa'

        return context


class HomePageView2(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countWords'] = Word.objects.all().count()
        context['title'] = 'Bosh sahifa'

        return context


def contact_view(request):
    return render(request, 'contact.html')


def about_view(request):
    return render(request, 'about.html')


class SearchResultsView(ListView):
    model = Word
    template_name = 'main/index.html'

    # extra_context = {'title': 'Bosh sahifa', 'countWords': Word.objects.all().count()}
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countWords'] = Word.objects.all().count()
        context['title'] = 'Bosh sahifa'

        return context

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Word.objects.filter(Q(name=query))
        return object_list


class SearchResultsView2(ListView):
    model = Word
    template_name = 'index.html'

    # extra_context = {'title': 'Bosh sahifa', 'countWords': Word.objects.all().count()}
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['countWords'] = Word.objects.all().count()
        context['title'] = 'Bosh sahifa'

        return context

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Word.objects.filter(Q(name=query))
        return object_list


# server {
#     listen 80;
#     server_name gippologik-termin.uz;
#
#     location = /favicon.ico { access_log off; log_not_found off; }
#     location /static/ {
#         root /home/ubuntu/nurbek/djangodictionary
# ;
#     }
#
#     location / {
#         include proxy_params;
#         proxy_pass http://unix:/run/sayt.sock;
#     }
# }
def contact_view(request):
    form = ContactForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, 'contact.html', context)
