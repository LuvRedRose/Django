from django import forms
from .models import ProductModel

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = [
            'product_name',
            'detail',
            'category',
            'price',
            'quantity',
            'image'
        ]

        widgets = {
            'product_name' : forms.TextInput(
                attrs = {'class' : 'form-control',
                        'placeholder' : 'Input Product Name Here....'}
            ), 
            'detail' : forms.Textarea(
                attrs = {'class' : 'form-control',
                        'placeholder' : 'Input Detail Here...'}
            ),
            'category' : forms.TextInput(
                attrs = {'class' : 'form-control',
                        'placeholder' : 'Input Category Here..'}
            ),
            'price' : forms.NumberInput(
                attrs = {'class' : 'form-control',
                        'placeholder' : 'Input Price Here..'}
            ),
            'quantity' : forms.NumberInput(
                attrs = {'class' : 'form-control',
                        'placeholder' : 'Input quantity Here..'}
            ),
            'image' : forms.FileInput(
                attrs = {'class' : 'form-control',
                        'placeholder' : 'Choose Image..'}
            ),
        }