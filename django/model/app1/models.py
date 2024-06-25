from django.db import models


# app1_person 테이블 생성
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        db_table = "person"

    # makemigrations 대상 아님 / 클래스메소드임
    def __str__(self) -> str:
        return self.first_name + " " + self.last_name


# 직접 코드쓸 수 있도록 함
# > python manage.py shell


# SQL 쿼리문 대체
# select * from person; == Person.objects.all()

# insert into values(); == person = Person() person.save()
# 						   Person.objects.create(first_name='park', last_name='jiho')

# select * from person where first_name='park';
# 	   == Person.objects.get(first_name='park')
# 	   == Person.objects.filter(first_name='park')
# 	   == Person.objects.get(id=5)
# 	   == Person.objects.filter(id=5)
# 	   == Person.objects.filter(first_name__contains='pa')
# 	   == Person.objects.filter(first_name__icontains='pa')
# 	   == Person.objects.filter(first_name__contains='PA')
