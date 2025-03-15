from django.db import models

class Hall(models.Model):
    name = models.CharField("館別名稱", max_length=100)

    def __str__(self):
        return self.name

class Animal(models.Model):
    name = models.CharField("動物名稱", max_length=100)
    height = models.IntegerField("身高", blank=True, null=True)  # 身高
    weight = models.IntegerField("體重", blank=True, null=True)  # 體重
    cup_size = models.CharField("罩杯", max_length=5, blank=True, null=True)  # 罩杯
    fee = models.IntegerField("台費", blank=True, null=True)  # 台費
    time_slot = models.CharField(
        "時段",
        max_length=200,
        blank=True,
        help_text="請輸入時段，每個時段用 '.' 隔開，例如：12.13.14.15.16.17.18.19.20"
    )
    hall = models.ForeignKey(Hall, verbose_name="館別", on_delete=models.SET_NULL, null=True, blank=True)
    photo = models.ImageField("照片", upload_to='animal_photos/', blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def size_display(self):
        """組合身高.體重.罩杯"""
        return f"{self.height}.{self.weight}.{self.cup_size}" if self.height and self.weight and self.cup_size else ""
