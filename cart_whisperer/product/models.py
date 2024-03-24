from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nombre")
    parent = models.ForeignKey(
        to="self",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name="Categoría padre",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["name"]


class Brand(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nombre")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
        ordering = ["name"]


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nombre")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    brand = models.ForeignKey(to=Brand, on_delete=models.CASCADE, verbose_name="Marca")
    category = models.ForeignKey(
        to=Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Categoría",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["name"]
