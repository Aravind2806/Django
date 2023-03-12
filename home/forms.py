from django import forms
from .models import booking

class date_input(forms.DateInput):
    input_type='date'

class BookingForm(forms.ModelForm):
    class Meta:
        model=booking
        fields='__all__'

        widgets={
            'booking_date':date_input()
        }


        labels={
            'p_name' : 'Patient Name',
            'p_age'  : 'Age',
            'p_phone': 'Phone Number',
            'p_email' : 'Email',
            'doc_name' : 'Doctor Name',
            'booking_date':'Booking Date'
            
        }



