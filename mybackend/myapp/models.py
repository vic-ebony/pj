from django.db import models

class Hall(models.Model):
    name = models.CharField("館別名稱", max_length=100)

    def __str__(self):
        return self.name

class Animal(models.Model):
    name = models.CharField("動物名稱", max_length=100)
    age = models.IntegerField("年齡")
    species = models.CharField("物種", max_length=100)
    hall = models.ForeignKey(Hall, verbose_name="館別", on_delete=models.SET_NULL, null=True, blank=True)
    photo = models.ImageField("照片", upload_to='animal_photos/', blank=True, null=True)
    time_slot = models.CharField(
        "時段",
        max_length=200,
        blank=True,
        help_text="請輸入時段，每個時段用 '.' 隔開，例如：12.13.14.15.16.17.18.19.20"
    )

    def __str__(self):
        return self.name
