from django.forms import ModelForm, forms

from catalog.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    banned_words = [
        'казино',
        'криптовалюта',
        'крипта',
        'биржа',
        'дешево',
        'бесплатно',
        'обман',
        'полиция',
        'радар',
    ]

    def clean_name(self):
        name = self.cleaned_data['name']
        for word in self.banned_words:
            if word.lower() in name.lower():
                raise forms.ValidationError(f'Название содержит запрещенное слово "{word}".')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description', '')

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите наименование продукта"
        })

        self.fields['description'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите описание продукта"
        })

        self.fields['image'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите изображение продукта (необязательно)"
        })

        self.fields['category'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите категорию продукта"
        })

        self.fields['cost'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите цену продукта"
        })


