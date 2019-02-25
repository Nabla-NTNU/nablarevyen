from django.forms import ModelForm, ModelChoiceField
from django.utils import timezone


from apps.groups.models import Group
from . models import Position, Application


class ApplicationForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['position'].queryset = Position.objects.filter(published=True, deadline__gte=timezone.now(), open__lte=timezone.now()).order_by('deadline')
        self.fields['first_group'].queryset = Group.objects.filter(published=True)
        self.fields['second_group'].queryset = Group.objects.filter(published=True)
        self.fields['third_group'].queryset = Group.objects.filter(published=True)
        self.fields['name'].widget.attrs.update({'placeholder': 'Navn'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Epostadresse'})
        self.fields['phone'].widget.attrs.update({'placeholder': 'Telefon'})
        self.fields['student_class'].widget.attrs.update({'placeholder': 'Klasse'})
        self.fields['text'].widget.attrs.update({'placeholder': 'Søketekst'})

    class Meta:
        model = Application
        fields = ['position', 'name', 'email', 'phone', 'student_class', 'text', 'first_group', 'second_group', 'third_group']
