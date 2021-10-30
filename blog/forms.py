from django import forms

from .models import Post, blogCategory


class PostCreateForm(forms.ModelForm):
    title = forms.CharField(required=True, max_length=200, label='Title',
                            widget=forms.TextInput(attrs={
                                'class': 'form-control  ',
                                'label': 'Title',

                            }))
    # image = forms.ImageField(required=True, validators=[FileTypeValidator(
    #     allowed_types=['image/*']
    # )],
    #                          widget=forms.FileInput(attrs={
    #                              'class': '  waves-effect    ',
    #
    #                          }))

    published_date = forms.DateTimeField(label='Published Date', widget=forms.SelectDateWidget(attrs={
        'class': 'form-control   datetimepicker ',
        'label': 'published_date',
    }))

    category = forms.ChoiceField(choices=blogCategory, required=False,
                                 widget=forms.Select(attrs={
                                     'class': 'form-control bg-primary text-info dropdown-toggle ',
                                     'type': "button",
                                     'data-toggle': "dropdown"
                                 }))

    class Meta:
        model = Post
        fields = ['title'
            , 'category'
            , 'description'
            , 'image'
            , 'published_date']
