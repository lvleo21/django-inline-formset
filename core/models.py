from django.db import models
from django.utils.translation import gettext_lazy as _


class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True


class Question(Timestamp):
    title = models.CharField(max_length=255, verbose_name = _(u"Título"))
    description = models.TextField(verbose_name = _(u"Descrição"), blank=True, null=True)

    class Meta:
        verbose_name = _(u"Questão")
        verbose_name_plural = _(u"Questões")

    def __str__(self):
        return F"#{self.id} - Question"


class Alternative(Timestamp):
    description = models.CharField(max_length=255, verbose_name = _(u"Descrição"))
    is_correct = models.BooleanField(verbose_name = _(u"É a correta?"), default=False)
    question = models.ForeignKey(Question, verbose_name = _(u"Questão"), on_delete=models.CASCADE, blank=True)

    class Meta:
        verbose_name = _(u"Alternativa")
        verbose_name_plural = _(u"Alternativas")

    def __str__(self):
        return F"#{self.id} - Alternative"