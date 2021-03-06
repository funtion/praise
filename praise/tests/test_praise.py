from unittest import TestCase
from .helper import *
import praise


class TestPraise(TestCase):

    def test_corner_case(self):
        self.assertEqual("", praise.praise(""))
        self.assertEqual("None", praise.praise(None))
        self.assertEqual("foo", praise.praise("foo"))
        self.assertEqual("${foo}", praise.praise("${foo}"))

    def test_word(self):
        self.assertTrue(
            praise.praise("${adjective}") in praise.adjective.adjective)
        self.assertTrue(praise.praise("${adverb}") in praise.adverb.adverb)
        self.assertTrue(
            praise.praise("${exclamation}") in praise.exclamation.exclamation)
        self.assertTrue(praise.praise("${smiley}") in praise.smiley.smiley)
        self.assertTrue(praise.praise("${created}") in praise.verb.created)
        self.assertTrue(praise.praise("${creating}") in praise.verb.creating)

    def test_milti_words(self):
        template = "${adjective},${adverb},${exclamation},${smiley},${created},${creating}"
        result = praise.praise(template).split(",")
        self.assertEqual(6, len(result))

        self.assertTrue(result[0] in praise.adjective.adjective)
        self.assertTrue(result[1] in praise.adverb.adverb)
        self.assertTrue(result[2] in praise.exclamation.exclamation)
        self.assertTrue(result[3] in praise.smiley.smiley)
        self.assertTrue(result[4] in praise.verb.created)
        self.assertTrue(result[5] in praise.verb.creating)

    def test_caption_words(self):
        self.assertTrue(caption_check(praise.praise("${ADJECTIVE}"), praise.adjective.adjective))
        self.assertTrue(caption_check(praise.praise("${ADVERB}"), praise.adverb.adverb))
        self.assertTrue(caption_check(praise.praise("${EXCLAMATION}"), praise.exclamation.exclamation))
        self.assertTrue(caption_check(praise.praise("${SMILEY}"), praise.smiley.smiley))
        self.assertTrue(caption_check(praise.praise("${CREATED}"), praise.verb.created))
        self.assertTrue(caption_check(praise.praise("${CREATING}"), praise.verb.creating))

    def test_first_caption_words(self):
        self.assertTrue(first_letter_caption_check(praise.praise("${Adjective}"), praise.adjective.adjective))
        self.assertTrue(first_letter_caption_check(praise.praise("${Adverb}"), praise.adverb.adverb))
        self.assertTrue(first_letter_caption_check(praise.praise("${Exclamation}"), praise.exclamation.exclamation))
        self.assertTrue(first_letter_caption_check(praise.praise("${Smiley}"), praise.smiley.smiley))
        self.assertTrue(first_letter_caption_check(praise.praise("${Created}"), praise.verb.created))
        self.assertTrue(first_letter_caption_check(praise.praise("${Creating}"), praise.verb.creating))
