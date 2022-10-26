from django import forms



class ContactForm(forms.Form):
    CHOICES=[
        ('ST','Please indicate urgency request:'),
        ('high priority', 'High priority'),
        ('medium priority', 'Medium priority'),
        ('low priority', 'Low priority'),  
    ]
    

    SELECT_CHOICES= [
        ('purchase','Purchase'),
        ('installation', 'Installation'),
        ('maintenance', 'Maintenance'),
        ('others', 'Others'), 
    ]

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),label='',max_length=50,required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),label='',max_length=50,required=True)
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Whatsapp Phone'}),label='',max_length=11,required=True)
    priority_list = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control','placeholder':'Service'}),label='',choices=CHOICES,required=True)
    service_option = forms.ChoiceField(widget=forms.RadioSelect, choices=SELECT_CHOICES,label='',required=True)
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),label='',max_length=150,required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Provide us any further information you think may be important:', 'rows':8}),label='',required=True)

