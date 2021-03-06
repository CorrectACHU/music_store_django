from django.forms import ModelChoiceField, ModelForm
from django.contrib import admin
from .models import *


class EarphoneAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance.wireless:
            print('HUY')
            self.fields['cable_len'].widget.attrs.update({
                'readonly': True, 'style': 'background: grey;'
            })

    def clean(self):
        if self.cleaned_data['wireless']:
            self.cleaned_data['cable_len'] = None
        return self.cleaned_data


class EarphonesAdmin(admin.ModelAdmin):

    change_form_template = 'admin.html'
    # form = EarphoneAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='earphonesproduct'))
        return super().formfield_for_foreignkey(db_field,request,**kwargs)

class SpeakersAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='speakersproduct'))
        return super().formfield_for_foreignkey(db_field,request,**kwargs)

# Register your models here.
admin.site.register(Category)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(SpeakersProduct, SpeakersAdmin)
admin.site.register(EarphonesProduct, EarphonesAdmin)
admin.site.register(Order)