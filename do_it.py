from blog.models import Category
from django.utils.text import slugify

for cat in Category.objects.all():
    base = slugify(cat.category)
    slug = base
    counter = 1
    while Category.objects.exclude(pk=cat.pk).filter(slug=slug).exists():
        counter += 1
        slug = f"{base}-{counter}"
    cat.slug = slug
    cat.save()