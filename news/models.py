from django.db import models


class Headline(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(null = True, blank = True)
    url = models.TextField()
    source = models.CharField(max_length=200,null = True,blank=True)

    def __str__(self):
        return self.title

class EHeadline(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(null = True, blank = True)
    url = models.TextField()
    source = models.CharField(max_length=200,null = True,blank=True)

    def __str__(self):
        return self.title

class SHeadline(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(null = True, blank = True)
    url = models.TextField()
    source = models.CharField(max_length=200,null = True,blank=True)

    def __str__(self):
        return self.title

class PHeadline(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(null = True, blank = True)
    url = models.TextField()
    source = models.CharField(max_length=200,null = True,blank=True)

    def __str__(self):
        return self.title

class LHeadline(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(null = True, blank = True)
    url = models.TextField()
    source = models.CharField(max_length=200,null = True,blank=True)

    def __str__(self):
        return self.title

class ENHeadline(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(null = True, blank = True)
    url = models.TextField()
    source = models.CharField(max_length=200,null = True,blank=True)

    def __str__(self):
        return self.title