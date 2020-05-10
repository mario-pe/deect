from django.conf.urls import url

from deect.views import words, en_translation, pl_translation, en_random, pl_random

app_name = "deect"

urlpatterns = [
    url(r"^words/$", words, name="words"),
    url(r"^words/en/(?P<word>[\w-]+)/$", en_translation, name="en_translation"),
    url(r"^words/pl/(?P<word>[\w-]+)/$", pl_translation, name="pl_translation"),
    url(r"^words/random/en/$", en_random, name="en_random"),
    url(r"^words/random/pl/$", pl_random, name="pl_random"),

    # url(r"^product/(?P<product_id>[0-9]+)/$", product_details, name="product_details"),
]
# if settings.DEBUG:
#     urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)