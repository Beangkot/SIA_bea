from django.db import models


class LostFoundItem(models.Model):

    STATUS_CHOICES = [
        ('Lost', 'Lost'),
        ('Found', 'Found'),
        ('Claimed', 'Claimed'),
    ]

    CATEGORY_CHOICES = [
        ('Electronics', 'Electronics'),
        ('School Supplies', 'School Supplies'),
        ('Clothing', 'Clothing'),
        ('Accessories', 'Accessories'),
        ('Documents', 'Documents'),
        ('Keys', 'Keys'),
        ('Bags', 'Bags'),
        ('Others', 'Others'),
    ]

    item_id = models.AutoField(primary_key=True)

    item_name = models.CharField(
        max_length=200
    )

    description = models.TextField()

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Lost'
    )

    location = models.CharField(
        max_length=200
    )

    date_reported = models.DateField(
        auto_now_add=True
    )

    contact_name = models.CharField(
        max_length=150
    )

    contact_information = models.CharField(
        max_length=200
    )

    item_image = models.ImageField(
        upload_to='lost_found/',
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.item_name} - {self.status}"

    class Meta:
        ordering = ['-date_reported']
