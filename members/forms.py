from django.forms import ModelForm
from .models import Member

# Create the Member Form
class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ["f_name", "l_name", "email", "phone_number", "role"]

    def clean_phone_number(self):
        # add '-' to the phone numbers if user didn't enter
        super().clean()
        phone_number = self.cleaned_data["phone_number"]
        if phone_number[3] != "-":
            phone_number = phone_number[:3] + "-" + phone_number[3:]

        if phone_number[7] != "-":
            phone_number = phone_number[:7] + "-" + phone_number[7:]

        return phone_number
