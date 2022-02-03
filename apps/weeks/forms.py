from django import forms


class DateInput(forms.DateInput):
    input_type = "date"


class DateForm(forms.Form):
    input_date = forms.DateField(
        label="Укажите дату",
        widget=DateInput(attrs={"class": "form-control form-control-lg"}),
    )
