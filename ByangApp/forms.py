from django import forms

from .models import LostFoundItem


class LostFoundItemForm(forms.ModelForm):

    class Meta:

        model = LostFoundItem

        fields = [
            'item_name',
            'description',
            'category',
            'status',
            'location',
            'contact_name',
            'contact_information',
            'item_image',
        ]

        widgets = {

            'item_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter item name'
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Describe the item',
                    'rows': 5
                }
            ),

            'category': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),

            'status': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),

            'location': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Where was it lost/found?'
                }
            ),

            'contact_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Your name'
                }
            ),

            'contact_information': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Phone number or email'
                }
            ),

            'item_image': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                    'accept': 'image/*'
                }
            ),
        }
