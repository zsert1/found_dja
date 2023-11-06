from django.db import models


class Post(models.Model):
    message = models.TextField()
    is_pubilc = models.BooleanField(default=False, verbose_name="공개여부")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(
        blank=True, upload_to='instagram/post/%Y/%m/%d')  # pillow설치

    def __str__(self):
        # return f"Custom Post object ({self.id})"
        return self.message
    # def message_lenght(self):
    #     return len(self.message)
    # message_lenght.short_description='메세지글자수'

    class Meta:
        ordering = ['-id']
