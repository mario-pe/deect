from datetime import datetime

import factory
from factory.compat import UTC
from factory.fuzzy import FuzzyDateTime, FuzzyDate

from deect.models import Word


class WordFactory(factory.DjangoModelFactory):
    word = factory.Faker("word")
    translation = factory.Faker("word")
    add_date = FuzzyDateTime(datetime.now(tz=UTC))
    tutor = factory.Faker("name")

    class Meta:
        model = Word