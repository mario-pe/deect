from django_elasticsearch_dsl import Index
from django_elasticsearch_dsl.documents import DocType

from deect.models import Word

words_index = Index("words")


@words_index.doc_type
class WordDocument(DocType):
    class Django:
        model = Word

        fields = ["word", "translation", "date", "tutor"]
