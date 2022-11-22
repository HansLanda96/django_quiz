from django import forms
from django.core.exceptions import ValidationError

from .models import Choice


class QuestionInlineFormSet(forms.BaseInlineFormSet):
    def clean(self):
        if not (self.instance.QUESTION_MIN_LIMIT <= len(self.forms) <= self.instance.QUESTION_MAX_LIMIT):
            raise ValidationError(
                f'Questions count must be range '
                f'from {self.instance.QUESTION_MIN_LIMIT} '
                f'to {self.instance.QUESTION_MAX_LIMIT} inclusive'
            )

        # order_num validators
        index = 1
        for form in self.forms:
            if form.cleaned_data['order_num'] != index:
                raise ValidationError(
                    f'Question order must be in range from 1 to {self.instance.QUESTION_MAX_LIMIT}'
                    f'and greater than previous by 1'
                )
            elif self.instance.QUESTION_MAX_LIMIT < form.cleaned_data['order_num']:
                raise ValidationError(
                    f'Question order must be less than {self.instance.QUESTION_MAX_LIMIT} inclusive'
                )
            else:
                index += 1


class ChoiceInlineFormSet(forms.BaseInlineFormSet):
    def clean(self):
        num_correct_answers = sum(form.cleaned_data['is_correct'] for form in self.forms)

        if num_correct_answers == 0:
            raise ValidationError('Need to choose one option minimum')

        if num_correct_answers == len(self.forms):
            raise ValidationError('It is not allowed to select all options')


class ChoiceForm(forms.ModelForm):
    is_selected = forms.BooleanField(required=False)

    class Meta:
        model = Choice
        fields = ('text',)


ChoicesFormSet = forms.modelformset_factory(
    model=Choice,
    form=ChoiceForm,
    extra=0
)
