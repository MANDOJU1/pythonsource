# request.method : http method 가져오기
# request.META : https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.META


def get_client_ip(request):
    ip = request.META.get("REMOTE_ADDR")  # request.META['REMOTE_ADDR']
    return ip
