from django import template

# template 에서 사용할 태그
# load 해서 사용

register = template.Library()
# 일련번호
# 전체 게시물 개수 - 시작 인덱스 - 현재 인덱스 + 1

@register.filter
def sub(value, arg):
    return value - arg