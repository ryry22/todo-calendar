from django import forms

class EventForm(forms.Form):
    title = forms.CharField(label='イベント', max_length=50)
    description = forms.CharField(label='場所・URL', required=False, empty_value='', max_length=50)

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')  # フィールド名を修正
        description = cleaned_data.get('description')  # フィールド名を修正

        if not title and not description:
            raise forms.ValidationError("イベントを入力してください")

        return cleaned_data