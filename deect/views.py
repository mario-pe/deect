import random

from django.shortcuts import render

from .models import Word


def words(request):
    words = Word.objects.all()
    return render(request, "words.html", {"words": words})


def en_translation(request, word):
    word = Word.objects.get(word=word)
    return render(request, "words.html", {"word": word.translation})


def pl_translation(request, word):
    word = Word.objects.get(translation=word)
    return render(request, "words.html", {"word": word.word})


def pl_random(request):
    ids = Word.objects.values_list("id", flat=True)
    id = random.choice(ids)
    word = Word.objects.get(id=id)
    return render(
        request, "words.html", {"word": word.translation, "translation": word.word}
    )


def en_random(request):
    ids = Word.objects.values_list("id", flat=True)
    id = random.choice(ids)
    word = Word.objects.get(id=id)

    return render(
        request, "words.html", {"word": word.word, "translation": word.translation}
    )
