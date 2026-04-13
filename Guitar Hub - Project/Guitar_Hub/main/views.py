from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from django.shortcuts import get_object_or_404, redirect

def home_page(request):
    return render(request, "main/home.html")

def types_page(request):
    return render(request, "main/types.html")

def chords_page(request):
    return render(request, "main/chords.html")

def tips_page(request):
    return render(request, "main/tips.html")

def facts_page(request):
    return render(request, "main/facts.html")

def forum_page(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("/accounts/login/?next={request.path}")

        text = request.POST.get("text")

        parent_id = request.POST.get('parent_id')

        parent = Message.objects.get(id=parent_id) if parent_id else None

        Message.objects.create(
            user=request.user,
            text=text,
            parent=parent
        )

        return redirect('forum')

    messages = Message.objects.filter(parent__isnull=True).order_by('-date')
    return render(request, "main/forum.html", {"messages": messages})


@login_required
def delete_message(request, message_id):
    msg = get_object_or_404(Message, id=message_id)

    # Allow delete if:
    # - user owns the message
    # - OR user is moderator
    if msg.user == request.user or request.user.has_perm('main.can_moderate'):
        msg.delete()

    return redirect('forum')

@login_required
def edit_message(request, message_id):
    msg = get_object_or_404(Message, id=message_id)

    if not (msg.user == request.user or request.user.has_perm('main.can_moderate')):
        return redirect('forum')

    if request.method == 'POST':
        msg.text = request.POST.get('text')
        msg.save()
        return redirect('forum')

    return render(request, 'main/edit_message.html', {'message': msg})
