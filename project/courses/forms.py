from ckeditor.fields import RichTextField

from courses.models import Course
from django.forms import ModelForm


class CourseCreationForm(ModelForm):
    description = RichTextField()

    class Meta:
        model = Course
        exclude = ('mentor', 'date-created', 'date-updated',)
