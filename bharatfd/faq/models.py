import asyncio
from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator
from django.core.cache import cache

# Create your models here.
class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = RichTextField()

    question_hi=models.TextField(blank=True, null=True)
    answer_hi=RichTextField(blank=True, null=True)
    question_bn=models.TextField(blank=True, null=True)
    answer_bn=RichTextField(blank=True, null=True)

    def get_translation(self, lang):
        cache_key = f'faq_{self.id}_{lang}'
        cached_translation = cache.get(cache_key)
        if cached_translation:
            return cached_translation

        translator = Translator()
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        if lang == 'hi':
            if not self.question_hi or not self.answer_hi:
                self.question_hi = loop.run_until_complete(translator.translate(self.question, dest='hi')).text
                self.answer_hi = loop.run_until_complete(translator.translate(self.answer, dest='hi')).text
                self.save(update_fields=['question_hi', 'answer_hi'])
            translation = (self.question_hi, self.answer_hi)
        elif lang == 'bn':
            if not self.question_bn or not self.answer_bn:
                self.question_bn = loop.run_until_complete(translator.translate(self.question, dest='bn')).text
                self.answer_bn = loop.run_until_complete(translator.translate(self.answer, dest='bn')).text
                self.save(update_fields=['question_bn', 'answer_bn'])
            translation = (self.question_bn, self.answer_bn)
        else:
            translation = (self.question, self.answer)

        cache.set(cache_key, translation, timeout=60*60*24)  # Cache for 24 hours
        return translation

    def save(self, *args, **kwargs):
        translator = Translator()
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        if not self.question_hi:
            self.question_hi = loop.run_until_complete(translator.translate(self.question, dest='hi')).text
        if not self.answer_hi:
            self.answer_hi = loop.run_until_complete(translator.translate(self.answer, dest='hi')).text
        if not self.question_bn:
            self.question_bn = loop.run_until_complete(translator.translate(self.question, dest='bn')).text
        if not self.answer_bn:
            self.answer_bn = loop.run_until_complete(translator.translate(self.answer, dest='bn')).text
        super().save(*args, **kwargs)


    def __str__(self):
        return self.question