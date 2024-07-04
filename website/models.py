from django.db import models


class Spillested(models.Model):
	navn = models.CharField(max_length=255)
	adresse = models.CharField(max_length=255)
	postnr = models.CharField(max_length=4)
	by = models.CharField(max_length=255)
	telefon = models.CharField(max_length=8, blank=True, null=True)
	email = models.EmailField()
	hjemmeside = models.URLField()

	def __str__(self):
		return self.navn

	class Meta:
		verbose_name_plural = "Spillesteder"


class Koncert(models.Model):
	navn = models.CharField(max_length=255)
	spillested = models.ForeignKey(Spillested, on_delete=models.CASCADE)
	dato = models.DateTimeField()
	facebook = models.URLField(blank=True, null=True)
	billetter = models.URLField(blank=True, null=True)
	band1 = models.CharField(max_length=255)
	band2 = models.CharField(max_length=255, blank=True, null=True)
	band3 = models.CharField(max_length=255, blank=True, null=True)
	band4 = models.CharField(max_length=255, blank=True, null=True)
	band5 = models.CharField(max_length=255, blank=True, null=True)
	band6 = models.CharField(max_length=255, blank=True, null=True)
	band7 = models.CharField(max_length=255, blank=True, null=True)
	band8 = models.CharField(max_length=255, blank=True, null=True)

	offentliggjort = models.BooleanField()

	def __str__(self):
		return self.navn + ' ' + '-' + ' ' + self.band1

	class Meta:
		verbose_name_plural = "Koncerter"


class Bestyrelse(models.Model):
	fornavn = models.CharField(max_length=255)
	mellemnavn = models.CharField(max_length=255, blank=True, null=True)
	efternavn = models.CharField(max_length=255)
	alder = models.CharField(max_length=255, blank=True, null=True)
	funktion = models.CharField(max_length=255, blank=True, null=True)
	band_dk = models.CharField(max_length=255, blank=True, null=True)
	band_int = models.CharField(max_length=255, blank=True, null=True)
	civilstatus = models.CharField(max_length=255, blank=True, null=True)
	fun_fact = models.CharField(max_length=255, blank=True, null=True)
	image = models.ImageField()

	def __str__(self):
		return self.fornavn + ' ' + self.efternavn

	class Meta:
		verbose_name_plural = "Bestyrelsen"
		ordering = ['fornavn']



class Frivillig(models.Model):
	vagter = models.CharField(max_length=255)
	beskrivelse = models.TextField(max_length=255)
	opgaver = models.TextField()
	opg_01 = models.TextField()
	opg_02 = models.TextField()
	opg_03 = models.TextField()
	opg_04 = models.TextField()
	opg_05 = models.TextField(null=True, blank=True)
	opg_06 = models.TextField(null=True, blank=True)
	opg_07 = models.TextField(null=True, blank=True)
	opg_08 = models.TextField(null=True, blank=True)
	opg_09 = models.TextField(null=True, blank=True)
	opg_10 = models.TextField(null=True, blank=True)
	opg_11 = models.TextField(null=True, blank=True)
	opg_12 = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.vagter

	class Meta:
		verbose_name_plural = "Frivillig"
