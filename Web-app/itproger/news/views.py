from django.shortcuts import render, redirect
from .models import Articles
from django.views.generic import DetailView, UpdateView, DeleteView



def news_home(request):
    news = Articles.objects.order_by('date')
    return render(request, 'news/news_home.html', {'news': news})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/deteils_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    fields = ['title']


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news-delete.html'


def create(request):
    return render(request, 'news/create.html')




#python manage.py runserver