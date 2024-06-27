from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Userform 을 사용해서 만들 수도 있다
class UserForm(UserCreationForm):

    # 필수 요소 추가 정의 가능
    email = forms.EmailField(label="이메일", help_text="사용할 이메일을 입력해 주세요")

    class Meta:
        model = User
                # fields = "__all__"
        # 비밀번호는 필수로 같이 들어감
        # username == id
        fields = ["username", "email"]
