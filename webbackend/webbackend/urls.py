"""
URL configuration for webbackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    path("admin/", admin.site.urls),
    
    path('api/chat/', include('socials.urls')),

    path('api/tickets/', include('tickets.urls')),
    path('api/comments/', include('comments.urls')),
    path('api/customer/', include('customer.urls')),
    path('api/achievement/', include('achievemets.urls')),
    path('api/entity/', include('entity.urls')),
    path('api/solutions/', include('solutions.urls')),  
    path('api/heropage/', include('HeroPage.urls')),
    path('api/homeview/', include('Homeview.urls')),  
    path('api/testimonials/', include('testimonials.urls')),
    path('api/license/',include ('license.urls')),
    path('api/users/',include('users.urls')),
    path('api/', include('login.urls')), 
    path('api/', include('logo.urls')),
    path('api/products/', include('product.urls')),
    path('api/category/', include('category.urls')),
    path('api/brand/', include('brands.urls')),
    path('api/color/', include('colors.urls')),
    path('api/enquiry/', include('Enquiry.urls')),
    path('api/payments/', include('payments.urls')),




    # Include HomeView app URLs
]
if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

