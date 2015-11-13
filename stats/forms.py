from django import forms


class UploadFileForm(forms.Form):
    options = forms.ChoiceField(
        choices=[('district', 'Dzielnice'), ('candidate', 'Kandydaci'),
                 ('city_council', 'Rada Miasta'), ('voivodeship', 'sejmik'),
                 ('president_first_turn_districts', 'Warszawa I tura dzielnice'),
                 ('president_first_turn', 'Warszawa I tura'),
                 ('president_second_turn_districts', 'Warszawa II tura dzielnice'),
                 ('president_second_turn', 'Warszawa II tura')
                 ]
    )
    file = forms.FileField()
