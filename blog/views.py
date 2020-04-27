from django.shortcuts import render,reverse,get_object_or_404
from . models import Post
from django.contrib.auth.models import User
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.





# @login_required(login_url='login')
# def home(request):
#     title='Home Page'
#     posts=Post.objects.all()
#     context={'posts':posts,'title':title}
#
#     return render(request,'blog/home.html',context=context)


@login_required(login_url='login')
def about(request):
    return render(request,'blog/about.html')



class Postview(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = ['-date_posted']
    paginate_by = 5



class UserPostview(ListView):
    model = Post
    template_name = 'blog/user_posts.html'

    paginate_by = 3


    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user)




class PostDetailview(DetailView):
    model = Post


class PostCreateview(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateview(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    login_url = '/login/'
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False



class PostDeleteview(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    login_url = '/login/'
    success_url = '/'
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False

