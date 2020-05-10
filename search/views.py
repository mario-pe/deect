from django.shortcuts import render

from search.document import WordDocument


def search(request):
    q = request.GET.get('q')
    if q:
        words = WordDocument.search().query("match", word="fri")
    else:
        words = ""

    return render(request, "words.html", {"words": words})
