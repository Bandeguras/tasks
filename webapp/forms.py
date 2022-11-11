from django import forms
STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]


class TaskForm(forms.Form):
    title = forms.CharField(max_length=30, required=True, label="Title")
    description = forms.CharField(max_length=3000, required=False, label="Description")
    status = forms.ChoiceField(required=True, choices=STATUS_CHOICES, label="Status")
    completion_at = forms.DateField(required=False, label="Completion_at")
