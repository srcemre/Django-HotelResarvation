from django.shortcuts import render

# Create your views here.
from accommodation.models import Category
from home.models import Settings, UserProfile


def index(request):
    setting = Settings.objects.get(pk=1)
    category = Category.objects.all()
    current_user = request.user
    current_user = UserProfile.objects.get(user_id=current_user.id)
    context = {
        'setting': setting,
        'category': category,
        'current_user': current_user,
    }
    return render(request, 'userprofile.html', context)
