from django.shortcuts import render, get_object_or_404, redirect
from board.models import Question
from board.forms import QuestionForm


from django.contrib.auth.decorators import login_required

from django.utils import timezone


# 로그인 권한 필요, 로그인 페이지로 이동
@login_required(login_url="common:login")
def question_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            # 작성자 = 로그인 유저
            question.author = request.user
            question.save()
            return redirect("board:question_list")
    else:
        form = QuestionForm()
    return render(request, "board/question_form.html", {"form": form})


@login_required(login_url="common:login")
def question_delete(request, qid):

    question = get_object_or_404(Question, id=qid)
    question.delete()
    return redirect("board:question_list")


@login_required(login_url="common:login")
def question_modify(request, qid):
    # qid 에 해당하는 question 찾은 후
    # 변경할 부분 수정후 save()

    question = get_object_or_404(Question, id=qid)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modified_at = timezone.now()
            question.save()
            return redirect("board:question_detail", qid=qid)
    else:
        form = QuestionForm(instance=question)

    return render(request, "board/question_form.html", {"form": form})
