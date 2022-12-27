from django.forms import ModelForm
from core.models import Question, Alternative
from django.forms import inlineformset_factory


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = "__all__"


class AlternativeForm(ModelForm):
    class Meta:
        model = Alternative
        fields=["description", "is_correct"]

AlternativeInlineFormset = inlineformset_factory(
    Question,
    Alternative,
    form=AlternativeForm,
    extra=5,
    # max_num=5,
    # fk_name=None,
    # fields=None, exclude=None, can_order=False,
    # can_delete=True, max_num=None, formfield_callback=None,
    # widgets=None, validate_max=False, localized_fields=None,
    # labels=None, help_texts=None, error_messages=None,
    # min_num=None, validate_min=False, field_classes=None
)