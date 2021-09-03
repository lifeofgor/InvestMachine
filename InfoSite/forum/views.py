from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, DeleteView
from LK.models import Lkpage
from django.views.generic.edit import FormMixin
from forum.forms import CommentForm
from forum.models import Comment


def ForumPage(request):
    search_query = request.GET.get('search', '')
    if search_query:
        forumNews = Lkpage.objects.filter(title_page=search_query)
    else:
        forumNews = Lkpage.objects.order_by('-data_page')
    return render(request, 'forum/forumPage.html', {'forumNews': forumNews})

class DetailForum(DetailView, FormMixin):
    model = Lkpage
    template_name = 'forum/forumdetails.html'
    context_object_name = 'article'
    form_class = CommentForm
    success_msg = 'Комментарий успешно создан'

    def get_success_url(self):
        return reverse_lazy('detailforum', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.post = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class CommentDeleteView(DeleteView):
    model = Comment
    success_url = '/forum/'

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

class PostDeleteView(DeleteView):
    model = Lkpage
    success_url = '/forum/'

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)






