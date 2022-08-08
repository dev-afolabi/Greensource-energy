from django import forms


class ContactForm(forms.Form):
    CHOICES= (
        ('ST','Solar Solution(s) For?'),
        ('Homes', 'Homes'),
        ('Farms', 'Farms'),
        ('Schools', 'Schools'),
        ('Offices', 'Offices'),
        ('Business', 'Business'),
        ('Agencies', 'Agencies'),
        ('Worship Centers', 'worship Centers'),
        
        
    )
    # amount = forms.DecimalField()
    # date = forms.DateField()

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),label='',max_length=50,required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),label='',max_length=50,required=True)
    from_email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'id':'from_email', 'placeholder':'Email'}),label='',required=True)
    phone= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}),label='',max_length=50,required=True)
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Location'}),label='',max_length=150,required=True)
    service = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control','placeholder':'Service'}),label='',choices=CHOICES,required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Type your message', 'rows':8}),label='',required=True)