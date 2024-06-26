from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    class Meta:
        model = User
        # fields = "__all__"
        # 비밀번호는 필수로 같이 들어감
        # username == id

        email = forms.EmailField(
            label="이메일", help_text="사용할 이메일을 입력해 주세요"
        )

        fields = ["username", "email"]
