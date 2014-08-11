from django.db import models

# Create your models here.


class Card(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    targetName = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Target(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    slot = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class CardListEntry(models.Model):
    listName = models.CharField(max_length=200)
    cardName = models.CharField(max_length=200)
    def __str__(self):
        return "{}-{}" % self.listName, cardName

class Level(models.Model):
    name = models.CharField(max_length=200)
    cardsetName = models.CharField(max_length=200)  #refers to a CardList
    deckName = models.CharField(max_length=200) #refers to a CardList
    time = models.IntegerField(default=0)
    numberOfCards = models.IntegerField(default=0)
    levelStyle = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class LevelPackEntry(models.Model):
    name = models.CharField(max_length=200)
    levelName = models.CharField(max_length=200)

    def __str__(self):
        return self.name

