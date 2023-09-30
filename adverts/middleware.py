from django.contrib.auth import get_user_model
from django.utils.timezone import now

def last_visit_middleware(get_response):

    User = get_user_model()

    def middleware(request):
        if request.user.is_authenticated:
            user = User.objects.filter(id=request.user.id)
            user.update(last_visit=now())
        response = get_response(request)
        return response
    
    return middleware



