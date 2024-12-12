from django.db import models

class BooksModel(models.Model):
    GENRE = (
        ("fantasy", "fantasy"),
        ("comedy", "comedy"),
        ("romance", "romance")
    )
    image = models.ImageField(upload_to="images/", verbose_name="Upload Image of the book")
    title = models.CharField(max_length=100, verbose_name="Enter a title of the book", blank=True)
    description = models.TextField(verbose_name="Enter a description of the book")
    price = models.FloatField(verbose_name="Enter the price of the book")
    created_at = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=100, choices=GENRE, default="fantasy")
    mail = models.EmailField(max_length=100, verbose_name="Enter the autor's email address", blank=True)
    author = models.CharField(max_length=100, verbose_name="Enter the author's name")
    trailer = models.URLField(verbose_name="Enter the trailer URL")

    class Meta:
        verbose_name = "книгу"
        verbose_name_plural = "книги"

    def __str__(self):
        return self.title

class Review(models.Model):
    STARS = (
        ('⭐', '⭐'),
        ('⭐⭐', '⭐⭐'),
        ('⭐⭐⭐', '⭐⭐⭐'),
        ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
        ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
    )
    book = models.ForeignKey(BooksModel, on_delete=models.CASCADE, related_name="reviews")
    created_at = models.DateField(auto_now_add=True)
    text = models.TextField(verbose_name="Enter a review of the book")
    rate = models.CharField(max_length=100, choices=STARS,
                            verbose_name="your rating of the book", default='⭐')

    def __str__(self):
        return f'{self.book} - {self.rate}'