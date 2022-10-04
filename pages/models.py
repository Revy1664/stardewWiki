from django.db import models
from slugify import slugify
from django.urls import reverse


class Theme(models.Model):
	slug = models.SlugField(null=True, blank=True)
	image = models.ImageField(upload_to="themes_images/", null=True, blank=True)
	title = models.CharField(max_length=50)
	description = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		return super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse("theme_detail/", kwargs={"slug": self.slug})
