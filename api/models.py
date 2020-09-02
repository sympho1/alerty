from django.db import models


class Abus(models.Model):
    description = models.TextField()
    localisation = models.CharField("lieu", max_length=255)
    commission_date = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to="", null=True, blank=True)
    alerted_at = models.DateTimeField(auto_now_add=True)

    # def save(self, *args, **kwargs):
    #     self.commission_date = self.commission_date.strftime("%m-%d-%Y")
    #     super().save(*args, **kwargs)


class Author(models.Model):
    name = models.CharField("Nom et prénoms", max_length=255, null=True, blank=True)
    author_residence = models.CharField(max_length=255)
    abuse = models.ForeignKey(Abus, on_delete=models.CASCADE, related_name="author_abuse")

    def __str__(self):
        return self.name


class Victim(models.Model):
    name = models.CharField("Nom et prénoms", max_length=255, null=True, blank=True)
    victim_residence = models.CharField(max_length=255)
    abuse = models.ForeignKey(Abus, on_delete=models.CASCADE, related_name="victim_abuse")

    def __str__(self):
        return self.name
    pass


class Alert(models.Model):
    abuse = models.ForeignKey(Abus, on_delete=models.CASCADE, related_name="alert_abuse")
    created_at = models.DateTimeField(auto_now_add=True)
    pass


class Alerter(models.Model):
    name = models.CharField("Nom et prénoms", max_length=255, default="Anonyme")
    phone = models.CharField("Téléphone", max_length=100, blank=True, null=True)
    residence = models.CharField(max_length=255, null=True, blank=True)
    abuse = models.ForeignKey(Abus, on_delete=models.CASCADE, related_name="alerter_abuse")
    # alert = models.ForeignKey("Alert", on_delete=models.CASCADE, related_name="alerter_alert")

    def __str__(self):
        return self.name

