from django.db import models


class CreatedTimeMixin(models.Model):
    """Field created_at for models"""

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True



class LoanApplication(CreatedTimeMixin):
    """Loan Application model"""

    name = models.CharField(max_length=50)
    contract = models.OneToOneField('Contract', on_delete=models.CASCADE, related_name='contract')

    class Meta:
        verbose_name = 'Loan Application'
        verbose_name_plural = 'Loan Applications'

    def __str__(self):
        return f'{self.name}'


class Contract(CreatedTimeMixin):
    """Contract model"""
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Contract'
        verbose_name_plural = 'Contracts'

    def __str__(self):
        return f'{self.name}'


class Product(CreatedTimeMixin):
    """Product model"""

    name = models.CharField(max_length=100)
    loan_application = models.ForeignKey(LoanApplication, on_delete=models.CASCADE, related_name='products')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.name}'


class Manufacturer(CreatedTimeMixin):
    """Manufacturer model"""

    name = models.CharField(max_length=255)
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='manufacturer')

    class Meta:
        verbose_name = 'Manufacturer'
        verbose_name_plural = 'Manufacturers'

    def __str__(self):
        return f'{self.name}'

