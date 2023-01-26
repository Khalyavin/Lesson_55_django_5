from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy, reverse

from blog.models import Blog


def blog(request):
    return render(request, 'blog/index.html')


def contacts(request):
    return render(request, 'blog/contacts.html')


class BlogListView(ListView):
    model = Blog
    context_object_name = 'posts'


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title')
    success_url = reverse_lazy('blog:list')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title')
    success_url = reverse_lazy('blog:list')


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:delete')


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        queryset = super().get_queryset()
        queryset = queryset.filter(published=Blog.STATUS_ACTIVE)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['title'] = 'Бла-бла-бла'
        return context_data

    # def get_object(self, queryset=None):
    #     send_mail(
    #         subject='Достижение',
    #         message=f'Ваша публикация {blog_item.published} достигла {blog_item.cntr} просмотров',
    #         from_email=settings.EMAIL_HOST_USER,
    #         recipient_list=[],
    #     )

def change_status(request, pk):
    blog_item = get_object_or_404(Blog, pk=pk)
    if blog_item.published == Blog.STATUS_ACTIVE:
        blog_item.published = Blog.STATUS_INACTIVE
    else:
        blog_item.published = Blog.STATUS_ACTIVE

    blog_item.save()

    return redirect(reverse('blog:list'))
