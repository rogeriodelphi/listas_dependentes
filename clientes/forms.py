from django import forms
from .models import Cliente, Cidade

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome', 'data_nascimento', 'uf', 'cidade')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cidade'].queryset = Cidade.objects.none()

        if 'uf' in self.data:
            try:
                uf_id = int(self.data.get('uf'))
                self.fields['cidade'].queryset = Cidade.objects.filter(uf_id=uf_id).order_by('nome')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['cidade'].queryset = self.instance.uf.cidade_set.order_by('nome')
