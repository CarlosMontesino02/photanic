"""photanic URL Configuration
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

from .api import api_router
from django.contrib import admin
from django.urls import path, include
from photanic_app.views import *
from django.conf.urls.static import static
from django.conf import settings
from photanic_app.api import *
from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    #WagAPI
    path('api/v2/', api_router.urls),
    #URL de photanic
    path('', include('photanic_app.urls')),

    #sign log etc
    path('registro/', FormUser.as_view(), name='user-add'),
    path("accounts/", include("django.contrib.auth.urls")),

    #Stuff
    path('aboutus', aboutus, name='aboutus'),
    path('contact', contact, name='contact'),
    path('terms', terms, name='terms'),

    #API
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        #Wag
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('pages/', include(wagtail_urls)),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
