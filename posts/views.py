from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormView, UpdateView
from posts.forms import ReplyForm, NewPostForm
from django.views.generic.edit import FormMixin
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from .models import Post, Comment


# Create your views here.
class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'posts/index.html'
    context_object_name = 'latest_post_list'
    #raise_exception = True
    login_url = 'login/'
    redirect_field_name = 'redirect_to'

    def get_queryset(self):
        return Post.objects.order_by('-createdDate')[:5]


class CreateView(FormView):
    template_name = 'posts/create.html'
    form_class = NewPostForm

    @csrf_exempt
    def form_valid(self, form, user):
        p = Post()
        p.headline = form.cleaned_data['headline']
        p.text = form.cleaned_data['text']
        p.author_id = user.id
        p.createdDate = timezone.now()
        p.save()
        return super(CreateView, self).form_valid(form)

    def post(self, request):
        form = NewPostForm(request.POST)
        user = request.user
        if form.is_valid():
            form.cleaned_data
            return self.form_valid(form, user)
        return reverse('posts:create')

    def get_success_url(self):
        return reverse('posts:index')


class EditView(UpdateView):
    model = Post
    form_class = NewPostForm
    template_name = 'posts/edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('posts:detail', kwargs={'pk': pk})

    # def get(self, request, pk):
    #     user = request.user
    #     post = Post.objects.get(pk=pk)
    #     if user != post.author_id:
    #         return reverse('posts:index')


# def detail(request, post_id):
#     try:
#         selected_post = Post.objects.get(pk=post_id)
#     except Post.DoesNotExist:
#         raise Http404("Post doesn't exist")
#     return render(request, 'posts/details.html', {'selected_post': selected_post})


class DetailFormView(FormMixin, generic.DetailView):
    template_name = 'posts/details.html'
    model = Post
    form_class = ReplyForm

    @csrf_exempt
    def form_valid(self, form, post_id, user):
        comment = Comment()
        comment.createdDate = timezone.now()
        comment.author = user
        comment.text = form.cleaned_data['text']
        comment.parentPost = Post.objects.get(pk=post_id)
        comment.save()
        return super(DetailFormView, self).form_valid(form)

    def post(self, request, pk):
        form = ReplyForm(request.POST)
        user = request.user
        if form.is_valid():
            form.cleaned_data
            return self.form_valid(form, pk, user)
        return reverse('posts:detail', {'pk': pk})

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('posts:detail', kwargs={'pk': pk})



#
# class ReplyView(FormView):
#     template_name = 'posts/reply.html'
#     form_class = ReplyForm
#     success_url = '/posts/'
#
#     def form_valid(self, form):
#         comment.text = form.cleaned_data
#         comment.author = "Me"
#
#     def get_context_data(self, **kwargs):




