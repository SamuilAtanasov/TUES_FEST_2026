from django.shortcuts import render
from .models import Message

def forum_page(request):
    messages = Message.objects.all().order_by('-date')
    return render(request, "forum.html", {"messages": messages})