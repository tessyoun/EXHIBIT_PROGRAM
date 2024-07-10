from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from .models import Notice
from .forms import NoticeForm

def notice_list(request):
    notice_list = Notice.objects.all().order_by("-update_time")
    return render(request, 'notice_list.html', {'notice_list' : notice_list})

def notice_detail(request, pk):
    notice = Notice.objects.get(pk=pk)
    return render(request, 'notice_detail.html', {'notice':notice})


@login_required
def notice_new(request):
    if not request.user.is_staff:
        return redirect('notice_list')
    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.author = request.user
            notice.save()
            return redirect('notice:notice_detail', pk=notice.pk)
    else:
        form = NoticeForm()
    return render(request, 'notice_form.html', {'form':form})

@login_required
def notice_edit(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    if notice.author != request.user:
        raise PermissionDenied("You are not allowed to edit this notice.")
    if request.method == 'POST':
        form = NoticeForm(request.POST, instance=notice)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.save()
            return redirect('notice:notice_detail', pk=notice.pk)
    else:
        form = NoticeForm(instance=notice)
    return render(request, 'notice_form.html', {'form':form})

@login_required
def notice_delete(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    if notice.author != request.user:
        raise PermissionDenied("You are not allowed to edit this notice.")
    notice.delete()
    return redirect('notice:notice_list')