from django import forms


class ContactForm(forms.Form):
    CHOICES= (
        ('ST','State'),
        ('Abia','Abia'), 
        ('Adamawa','Adamawa'), 
        ('Akwa ibom','Akwa ibom'), 
        ('Anambra','Anambra'),
        ('Bauchi', 'Bauchi'), 
        ('Bayelsa','Bayelsa'), 
        ('Benue','Benue'), 
        ('Borno','Borno'), 
        ('Cros river','Cross River'),
        ('Delta','Delta'), 
        ('Ebonyi','Ebonyi'), 
        ('Edo','Edo'), 
        ('Ekiti','Ekiti'), 
        ('Enugu','Enugu'), 
        ('Gombe','Gombe'),
        ('Imo','Imo'), 
        ('Jigawa','Jigawa'), 
        ('Kaduna','Kaduna'), 
        ('Kano','Kano'), 
        ('Katsina','Katsina'), 
        ('Kebbi','Kebbi'),
        ('Kogi','Kogi'), 
        ('Kwara','Kwara'), 
        ('Lagos','Lagos'), 
        ('Nasarawa','Nasarawa'), 
        ('Niger','Niger'), 
        ('Ogun','Ogun'),
        ('Ondo','Ondo'), 
        ('Osun','Osun'), 
        ('Oyo','Oyo'), 
        ('Plateau','Plateau'), 
        ('Rivers','Rivers'), 
        ('Sokoto','Sokoto'),
        ('Taraba','Taraba'), 
        ('Yobe','Yobe'), 
        ('Zamfara','Zamfara'),
        ('Abuja','Abuja'),
    )
    # amount = forms.DecimalField()
    # date = forms.DateField()

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),label='',max_length=50,required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),label='',max_length=50,required=True)
    from_email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'id':'from_email', 'placeholder':'Email'}),label='',required=True)
    phone= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'phone'}),label='',max_length=50,required=True)
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'City'}),label='',max_length=50,required=True)
    state = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control','placeholder':'State'}),label='',choices=CHOICES,required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'What services are you interested in?', 'rows':8}),label='',required=True)