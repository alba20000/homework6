from news import models, forms
from django.views.generic import ListView, TemplateView, DetailView, RedirectView, FormView


class ClassBasedIndex(TemplateView):
    template_name = 'news/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news = models.News.objects.all()
        categories = models.Category.objects.all()
        context['news'] = news
        context['categories'] = categories
        context['title'] = 'Список новостей'
        return context


class ClassBasedGetCategory(TemplateView):
    template_name = 'news/category.html'

    def get_context_data(self, category_id, **kwargs):
        context = super().get_context_data(**kwargs)
        news = models.News.objects.filter(category=category_id)
        categories = models.Category.objects.all()
        category = models.Category.objects.get(pk=category_id)
        context['news'] = news
        context['categories'] = categories
        context['category'] = category
        return context


class NewsList(ListView):
    model = models.News
    context_object_name = 'news'
    template_name = 'news/list.html'


class NewsDetail(DetailView):
    model = models.News
    context_object_name = 'item'
    template_name = 'news/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = 'Пишите письма: mail@mail.ru'
        return context


class Redirect(RedirectView):
    query_string = True
    url = 'https://yandex.ru/pogoda/'


class SimpleForm(FormView):
    template_name = 'news/form.html'
    form_class = forms.SimpleForm
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
