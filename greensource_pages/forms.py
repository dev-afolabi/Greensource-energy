from django import forms


class OrderForm(forms.Form):

    SELECT_CHOICES= [
        ('N405, 000','N405, 000'),
        ('N517, 500', 'N517, 500'),
        ('N585, 000', 'N585, 000'),
        ('N702, 000', 'N702, 000'), 
    ]

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),label='',max_length=50,required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),label='',max_length=50,required=True)
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Whatsapp Phone'}),label='',required=True)
    from_email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','id':'from_email', 'placeholder':'Email'}),label='')
    service_option = forms.ChoiceField(widget=forms.RadioSelect, choices=SELECT_CHOICES,label='')
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),label='',max_length=150,required=True)
    agree = forms.BooleanField(initial=False,required=True, label='I AGREE WITH THE TERMS AND CONDITION OF PURCHASE')
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Provide us any further information you think may be important:', 'rows':8}),label='',required=True)
