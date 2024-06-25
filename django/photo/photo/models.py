from django.db import models


class Photo(models.Model):
    # CharField : max_length를 정해주어야 함 / TextField 는 정해주지 않아도 됨
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()

    # admin 화면에서 photo 에 추가할 때 내가 쓴 제목으로 보이게 하기
    def __str__(self) -> str:
        return self.title
