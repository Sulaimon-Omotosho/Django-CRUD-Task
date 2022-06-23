from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post

class PostList(ListView):
    model = Post

class PostCreate(CreateView):
    model: Post
    fields: "__all__"
    success_url = reverse_lazy("blog:all")

class PostDetail(DetailView):
    model= Post

class PostUpdate(UpdateView):
    model = Post
    fields: '__all__'
    success_url = reverse_lazy('blog:all')

class  PostDelete(DeleteView):
    model = Post
    fields= '__all__'
    success_url = reverse_lazy('blog:all')




