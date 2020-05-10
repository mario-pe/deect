from django.conf.urls import url

from search.views import search

app_name = "search "

urlpatterns = [
    url(r"^search/", search, name="searcch"),
]
# if settings.DEBUG:
#     urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)