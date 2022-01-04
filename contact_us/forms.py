from django import forms


class ContactForm(forms.Form):
    CHOICES= (
        ('ST','Interested Service(s)?'),
        ('Residential Solar', 'Residential Solar'),
        ('Commercial Solar', 'Commercial Solar'),
        ('Inverter Installation', 'Inverter Installation'),
        ('Solar Lighting', 'Solar Lighting'),
        ('Solar Water Pump', 'Solar Water Pump'),
        ('Solar Energy Storage', 'Solar Energy Storage'),
        ('Energy Management', 'Energy Management'),
        ('Electrical Installation', 'Electrical Installation'),
        ('Maintenance / Retrofit', 'Maintenance / Retrofit'),
        
    )
    # amount = forms.DecimalField()
    # date = forms.DateField()

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),label='',max_length=50,required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),label='',max_length=50,required=True)
    from_email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'id':'from_email', 'placeholder':'Email'}),label='',required=True)
    phone= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'phone'}),label='',max_length=50,required=True)
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'City'}),label='',max_length=50,required=True)
    service = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control','placeholder':'Service'}),label='',choices=CHOICES,required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Message', 'rows':8}),label='',required=True)