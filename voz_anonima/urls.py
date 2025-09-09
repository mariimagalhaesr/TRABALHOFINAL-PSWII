
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from voz_anonima import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('denuncia/', include('denuncia.urls')),
    path('midia/', include('midia.urls')),
    path('usuario/', include('usuario.urls')),
    path('categoria/', include('categoria.urls')),
    path('', views.index, name='index'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
