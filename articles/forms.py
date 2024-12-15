from django import forms

from .models import Article


class AddArticle(forms.ModelForm):
    categorie_select = [
                    ("DEVELOPPEMENT WEB", "DEVELOPPEMENT WEB"), 
                    ("MARKETING DIGITAL", "MARKETING DIGITAL"), 
                    ("DEVELOPPEMENT WEB", "DEVELOPPEMENT WEB"), 
    ]
    categorie = forms.ChoiceField(choices=categorie_select, widget=forms.Select(
                                            attrs={
                                                "class":"block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-xs focus:ring-[#4a355b] focus:border-[#4a355b] dark:bg-[#4a355b] dark:border-[#4a355b] dark:placeholder-gray-400 dark:text-white dark:focus:ring-[#4a355b] dark:focus:border-[#4a355b]"
                                                }
                                 ))
    titre = forms.CharField(max_length=255,widget=forms.TextInput(
                                            attrs={
                                                "class":"block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-xs focus:ring-[#4a355b] focus:border-[#4a355b] dark:bg-[#4a355b] dark:border-[#4a355b] dark:placeholder-gray-400 dark:text-white dark:focus:ring-[#4a355b] dark:focus:border-[#4a355b]"
                                                }))
    img = forms.FileInput
    resume = forms.CharField(widget=forms.TextInput(
                            attrs={
                                "class":"block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-xs focus:ring-[#4a355b] focus:border-[#4a355b] dark:bg-[#4a355b] dark:border-[#4a355b] dark:placeholder-gray-400 dark:text-white dark:focus:ring-[#4a355b] dark:focus:border-[#4a355b]"
                                }))
    contenu = forms.CharField(max_length=255, widget=forms.TextInput(
                            attrs={
                                "class":"block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-xs focus:ring-[#4a355b] focus:border-[#4a355b] dark:bg-[#4a355b] dark:border-[#4a355b] dark:placeholder-gray-400 dark:text-white dark:focus:ring-[#4a355b] dark:focus:border-[#4a355b]"
                                }))

    class Meta:
        model = Article
        fields = ("categorie", "titre", "img", "resume", "contenu")
       
  

