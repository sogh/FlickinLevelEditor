from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from Flick.models import Card, Target, CardListEntry, Level
from django import forms


class NewCardForm(forms.Form):
    name = forms.CharField(max_length=200)
    image = forms.CharField(max_length=200)
    text = forms.CharField(max_length=200)
    targetName = forms.CharField(max_length=200)

class NewPatternForm(forms.Form):
    name = forms.CharField(max_length=200)

class EditPatternForm(forms.Form):
    name = forms.CharField(max_length=200)
    cardList = forms.CharField(max_length=200)


# Create your views here.
def index(request):
    context = {}
    return render(request, "Flick/index.html", context)


def card(request, cardName):
    return HttpResponse("You is lookin at card {}".format(cardName))

def cards(request):

    cards_list = Card.objects.all().order_by('name')
    targets_list = Target.objects.all()

    targets_dict = {}
    for target in targets_list:
        targets_dict[target.name] = target

    context = {
        'FlickCards' : cards_list,
        'FlickTargets' : targets_dict
    }
    return render(request, "Flick/cards.html", context)

def newcard(request):

    form = NewCardForm(request.POST)
    if form.is_valid():
        #make sure this card doesn't already exist
        existingCardQ = Card.objects.filter(name=form.cleaned_data['name'])
        if (len(existingCardQ) == 0):
            #insert the new card
            newCard = Card()
            newCard.name = form.cleaned_data['name']
            newCard.image = form.cleaned_data['image']
            newCard.targetName = form.cleaned_data['targetName']
            newCard.text = form.cleaned_data['text']

            newCard.save()


        return HttpResponseRedirect('/Flick/cards/')
    else:
        #invalid
        form = NewCardForm()


    context = {
    'form': form
    }
    return render(request, "Flick/newcard.html", context)

def patterns(request):
    cards_list = Card.objects.all().order_by('name')
    patterns_list = CardListEntry.objects.all()

    newPatternForm = NewPatternForm()


    patternDict = {}
    for entry in patterns_list:
        if entry.listName not in patternDict.keys():
            patternDict[entry.listName] = []

        patternList = patternDict[entry.listName]
        patternList.append(entry.cardName)
        patternDict[entry.listName] = patternList


    cardsDict = {}
    for card in cards_list:
        cardsDict[card.name] = card

    context = {
        'FlickPatterns' : patternDict,
        'FlickCards' : cardsDict,
        'NewPatternForm' : newPatternForm,
    }
    return render(request, "Flick/patterns.html", context)

def newpattern(request):

    newPatternForm = NewPatternForm(request.POST)
    if newPatternForm.is_valid():
        #make sure this card doesn't already exist
        existingPatternQ = Card.objects.filter(name=newPatternForm.cleaned_data['name'])
        if (len(existingPatternQ) == 0):
            #insert the new card
            newPattern = CardListEntry()
            newPattern.listName = newPatternForm.cleaned_data['name']
            newPattern.cardName = "Up"
            newPattern.save()


    return HttpResponseRedirect('/Flick/patterns/')
