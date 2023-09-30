from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import generic
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.urls import reverse

from .models import Advert
from .forms import LoginForm, RegisterForm

class IndexView(generic.ListView):
    template_name = 'adverts/index.html'
    context_object_name = 'latest_advert_list'
    #paginate_by = 10

    def get_queryset(self):
        """Return the last ten published adverts."""
        return Advert.objects.order_by('-pub_date')[:10]

class AdvertsCreateView(generic.CreateView):
    model = Advert
    fields = ['type', 'title', 'description', 'price', 'number_of_rooms', 'area', 'thumbnail']

    def form_valid(self, form):
        #set author
        #instance = form.save(commit=False)
        form.instance.author = self.request.user
        instance = form.save()
        url = reverse('advert', args=[instance.id])
        return redirect(url)


class AdvertUpdateView(generic.UpdateView):
    model = Advert
    fields = ['type', 'title', 'description', 'price', 'number_of_rooms', 'area', 'thumbnail']
    
    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author != self.request.user:
            raise Http404("You are not allowed to edit this Advert")
        return super(AdvertUpdateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        instance = form.save()
        url = reverse('advert', args=[instance.id])
        return redirect(url)


class AdvertView(generic.DetailView):
    template_name = 'adverts/advert.html'
    model = Advert

def search(request):
    return HttpResponse("Search page")

def publish(request):
    return HttpResponse("Publish page")

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                url = reverse('index')
                messages.add_message(request, messages.INFO, 'You have been successfully logged in.')
                return redirect(url)
            else:
                messages.add_message(request, messages.ERROR, 'Incorrent username or password.')
    else:        
        form = LoginForm()
    return render(request, 'adverts/login.html', {'form': form})

def logout_user(request):
    logout(request)
    url = reverse('index')
    messages.add_message(request, messages.INFO, 'You have been successfully logged out.')
    return redirect(url)

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                url = reverse('index')
                messages.add_message(request, messages.INFO, 'You have been successfully registered.')
                return redirect(url)
    else:
        form = RegisterForm()
    return render(request, 'adverts/register.html', {'form': form})

class UserView(generic.DetailView):
    template_name = 'adverts/user.html'
    model = get_user_model()
    slug_field = 'username'
    slug_url_kwarg = 'username'
    context_object_name = 'user_object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_adverts_list = Advert.objects.filter(author=self.object)
        context['user_adverts_list'] = user_adverts_list
        return context

class UserUpdateView(generic.UpdateView):
    # Add user edit form and avatars
    model = get_user_model()
    fields = ['username', 'first_name', 'last_name', 'email', 'avatar']
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name = 'adverts/user_form.html'

    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance != self.request.user:
            raise Http404("You are not allowed to edit this profile")
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)
