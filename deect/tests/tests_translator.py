from django.test import TestCase

from deect.tests.factories import WordFactory


class WordsTestCase(TestCase):

    def test_words_list_should_return_translation(self):
        WordFactory.create_batch(3)

        response = self.client.get("/words/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["words"]), 3)

    def test_should_return_translation_from_en_to_pl(self):
        WordFactory.create(word="word", translation="słowo")

        response = self.client.get("/words/en/word/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["word"], "słowo")

    def test_should_return_translation_from_pl_to_en(self):
        WordFactory.create(word="word", translation="słowo")

        response = self.client.get("/words/pl/słowo/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["word"], "word")

    def test_should_return_random_pl_word(self):
        WordFactory.create(word="word", translation="słowo")
        WordFactory.create(word="dog", translation="pies")
        WordFactory.create(word="cat", translation="kot")

        response = self.client.get("/words/random/pl/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(response.context["translation"], ["word", "dog", "cat"])
        self.assertIn(response.context["word"], ["słowo", "pies", "kot"])

    def test_should_return_random_en_word(self):
        WordFactory.create(word="word", translation="słowo")
        WordFactory.create(word="dog", translation="pies")
        WordFactory.create(word="cat", translation="kot")

        response = self.client.get("/words/random/en/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(response.context["word"], ["word", "dog", "cat"])
        self.assertIn(response.context["translation"], ["słowo", "pies", "kot"])
