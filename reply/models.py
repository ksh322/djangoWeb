from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from board.models import Post


class Reply(models.Model):
    contents = models.TextField(max_length=100)
    create_date= models.DateTimeField(auto_now_add=True)


    # post -reply 1 :N Model -> VIEW -> template 순으로작성
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    # user :writer- 1:N  # 일대다에서 다 N에게 foreignkey 부여
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
