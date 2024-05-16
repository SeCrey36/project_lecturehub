from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('create/', views.create_article, name='create_article'),
    path('article/<int:article_id>/', views.view_or_edit_article, name='view_or_edit_article'),
    re_path(r'^login/$', LoginView.as_view(), name='login'),
    re_path(r'^logout/$', LogoutView.as_view(), name='logout'),
    re_path(r'^$', views.dashboard, name='dashboard'),
    re_path(r'^password-change/$', PasswordChangeView.as_view(), name='password_change'),
    re_path(r'^password-change/done/$', PasswordChangeDoneView.as_view(), name='password_change_done'),
    re_path(r'^register/$', views.register, name = 'register'),
    path('edit_user/', views.edit_user, name='edit_user'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)