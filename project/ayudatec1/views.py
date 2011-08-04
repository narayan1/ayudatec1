from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from ayudatec1.models import UserProfile, Article, Category
from django.views.generic import TemplateView, DetailView, ListView

# def expert_list(request):
#
#     return render_to_response('experts_list.html', {})

class ExpertsListView(TemplateView):
    template_name = 'experts_list.html'

# def profile(request, username):
#     u = get_object_or_404(UserProfile, user__username=username)    
#     return render_to_response('profile.html', {'user': ' - '.join([u.user.username, u.bio, u.user.email])})

class ProfileView(DetailView):

    context_object_name = 'u'

    def get_object(self):
        u = get_object_or_404(UserProfile, user__username=self.kwargs['username'])
        return u

class ArticlesListView(ListView):

    context_object_name = 'articles_l'
    queryset = Article.objects.all()
    template_name = 'articles_list.html'

    def get_context_data(self, **kwargs):
        context = super(ArticlesListView, self).get_context_data(**kwargs)
        context['categories_l'] = Category.objects.all()
        return context

class CategoryView(ListView):

    context_object_name = 'cat'
    template_name = 'category.html'

    def get_queryset(self):
        c = get_object_or_404(Category, slug=self.kwargs['category'])
        return c

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['arts'] = Article.objects.filter(category__name=context['cat'].name)
        return context

class ArticleView(DetailView):

    context_object_name = 'art'
    template_name = 'article.html'

    def get_object(self):
        a = get_object_or_404(Article, slug=self.kwargs['article_slug'])
        return a
