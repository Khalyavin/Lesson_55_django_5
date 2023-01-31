from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy, reverse

from blog.models import Blog


def contacts(request):
    return render(request, 'blog/contacts.html')


class BlogActiveListView(ListView):
    queryset = Blog.objects.filter(published=Blog.STATUS_ACTIVE).all()
    template_name = 'blog/index.html'


class BlogAllListView(ListView):
#    model = Blog
    queryset = Blog.objects.all()
#    context_object_name = 'posts'


class BlogCreateView(CreateView):
    model = Blog
    fields = '__all__'
    #    fields = ('title', 'content', 'preview', 'published', 'views_cntr',)
    success_url = reverse_lazy('blog:list', )


class BlogUpdateView(UpdateView):
    model = Blog
    #    fields = ('title', )
    fields = '__all__'
    success_url = reverse_lazy('blog:list', )


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.published == 'active':
            obj.views_cntr += 1

        if obj.views_cntr == 100:
            print('Ушла почта!')
            send_mail(
                subject='Достижение',
                message=f'Ваша публикация {obj.published} достигла {obj.views_cntr} просмотров',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['VsslVssl@yandex.ru'],
            )

        obj.save()
        return obj


def change_status(request, pk):
    blog_item = get_object_or_404(Blog, pk=pk)
    if blog_item.published == Blog.STATUS_ACTIVE:
        blog_item.published = Blog.STATUS_INACTIVE
    else:
        blog_item.published = Blog.STATUS_ACTIVE

    blog_item.save()

    return redirect(reverse('blog:list'))
