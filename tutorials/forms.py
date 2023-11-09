from django import forms
from .models import Step
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class StepForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Step
        fields = ['title', 'content', 'creator', 'order']

    def __init__(self, *args, **kwargs):
        super(StepForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})  # Add the 'form-control' class to all fields

        # Add additional Bootstrap classes to specific fields if needed
        self.fields['title'].widget.attrs.update({'class': 'form-control mb-2'})  # Example: Add 'mb-2' margin-bottom class
        self.fields['order'].widget.attrs.update({'class': 'form-control'})  # Example: Add 'form-control' class
