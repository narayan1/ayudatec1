from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from ayudatec1.models import *
from django.views.generic import TemplateView, DetailView, ListView, FormView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


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

#class ContactView(DetailView):
#
#    template_name = 'contact.html'
#
#    def contact(request):
#        if request.method == 'POST':
#            form = ContactForm(request.POST)
#            if form.is_valid():
#                return HttpResponseRedirect('/articles/')
#        else:
#            form = ContactForm()
#
#        return render_to_response('contact.html', {'form': form,})

class ContactView(FormView):

    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/articles'

    def form_valid(self, request):
            f = ContactForm(self.request.POST)
            f.save()
            return HttpResponseRedirect(self.success_url)

class UserInterface(DetailView):

    context_object_name = 'u'
    template_name = 'user_interface.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserInterface, self).dispatch(*args, **kwargs)

    def get_object(self):
            c = get_object_or_404(UserProfile, user__username=self.request.user.username)
            return c

    def get_context_data(self, **kwargs):
        context = super(UserInterface, self).get_context_data(**kwargs)
        context['categories_l'] = Category.objects.all()
        return context

class LoginView(FormView):

    template_name = 'registration/login.html'
    form_class = LoginForm
    success_url = '/userinterface'

    def form_valid(self, request):
        username = self.request.POST['username']
        password = self.request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return HttpResponseRedirect(self.success_url)
            else:
                return HttpResponseRedirect('/login')
        else:
            return HttpResponseRedirect('/login')

class LogoutView(DetailView):

    template_name = 'registration/logout.html'
    context_object_name = 'u'

    def get_object(self):
        c = get_object_or_404(UserProfile, user__username=self.request.user.username)
        logout(self.request)
        return c

class EditProfileView(FormView):

    template_name = 'edit_profile.html'
    form_class = EditProfileForm
    success_url = '/userinterface'

    def form_valid(self, request):
        x = get_object_or_404(UserProfile, user__username=self.request.user.username)
        x.NOTDONEYET
        return HttpResponseRedirect(self.success_url)
