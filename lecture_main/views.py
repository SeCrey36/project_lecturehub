from django.shortcuts import get_object_or_404, render, redirect
from .forms import ArticleForm, UserRegistrationForm, ChangeUsernameForm, ChangePasswordForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.views.generic import DetailView
from .models import Article
from django.urls import reverse

    
def view_or_edit_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    user = request.user
    articles = Article.objects.filter(author=user)
    links = []
    for article in articles:
        url = reverse('view_or_edit_article', kwargs={'article_id': article.pk})
        links.append({'title': article.title, 'url': url})
    if request.user == article.author:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('view_or_edit_article', article_id=article_id)
        else:
            form = ArticleForm(instance=article)
        return render(request, 'view_article.html', {'form': form, 'article': article, 'links': links})
    else:
        return render(request, 'view_article.html', {'article': article, 'links': links})
    

def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('dashboard')
    else:
        form = ArticleForm()
    return render(request, 'create_article.html', {'form': form})



@login_required
def dashboard(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('dashboard')
    else:
        form = ArticleForm()
    
    user = request.user
    articles = Article.objects.filter(author=user)
    links = []
    for article in articles:
        url = reverse('view_or_edit_article', kwargs={'article_id': article.pk})
        links.append({'title': article.title, 'url': url})
    
    return render(request, 'account/dashboard.html', {'section': 'dashboard', 'form': form, 'links': links})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


@login_required
def edit_user(request):
    if request.method == 'POST':
        if 'change_username' in request.POST:
            username_form = ChangeUsernameForm(request.POST)
            password_form = ChangePasswordForm(user=request.user)
            if username_form.is_valid():
                new_username = username_form.cleaned_data['new_username']
                request.user.username = new_username
                request.user.save()
                return redirect('dashboard')  # Перенаправление на главную страницу
        elif 'change_password' in request.POST:
            username_form = ChangeUsernameForm()
            password_form = ChangePasswordForm(request.user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)  # Обновление сессии пользователя
                return redirect('dashboard')  # Перенаправление на главную страницу
    else:
        username_form = ChangeUsernameForm()
        password_form = ChangePasswordForm(user=request.user)
    return render(request, 'account/edit_profile.html', {'username_form': username_form, 'password_form': password_form})




