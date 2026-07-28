from django import forms

from shopapp.models import Product


class MultipleImageInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "name", "price", "description", "discount", "preview"

    images = forms.ImageField(
        required=False,
        widget=MultipleImageInput(),
    )


class CSVImportForm(forms.Form):
    csv_file = forms.FileField()
