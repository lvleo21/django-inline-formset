from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import QuestionForm, AlternativeInlineFormset
from .models import Question


class QuestionCreateView(CreateView):
    form_class = QuestionForm
    model = Question
    template_name = "core/index.html"
    success_url = reverse_lazy("question_create_view")

    def get_context_data(self, **kwargs):
        context = super(QuestionCreateView, self).get_context_data(**kwargs)
        context['alternative_formset'] = AlternativeInlineFormset()
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        alternative_formset = AlternativeInlineFormset(self.request.POST)
        if form.is_valid() and alternative_formset.is_valid():
            return self.form_valid(form, alternative_formset)
        else:
            return self.form_invalid(form, alternative_formset)

    def form_valid(self, form, alternative_formset):
        self.object = form.save(commit=False)
        self.object.save()
        
        instance = alternative_formset.save(commit=False)

        for alternative in instance:
            alternative.question = self.object
            alternative.save()
            
        return redirect(reverse("question_create_view"))

    def form_invalid(self, form, alternative_formset):
        return self.render_to_response(
            self.get_context_data(
                form=form,
                alternative_formset=alternative_formset
            )
        )


class QuestionListView(ListView):
    pass