from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.conf import settings
from .models import Notice
from .forms import NoticeForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def notice_list(request):
    notice_list = Notice.objects.all().order_by("-create_time")
    page = request.GET.get('page')
    
    paginator = Paginator(notice_list, 10)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        page_obj = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        page_obj = paginator.page(page)
        
    leftIndex = (int(page)-2)
    if leftIndex < 1:
        leftIndex = 1
    
    rightIndex = (int(page)+2)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages
        
    custom_range = range(leftIndex, rightIndex+1)
    return render(request, 'notice_list.html', {'notice_list' : notice_list, 'page_obj':page_obj, 
                                                'paginator':paginator, 'custom_range':custom_range})

def notice_detail(request, pk):
    notice = Notice.objects.get(pk=pk)
    # 이전글
    previous_notice = Notice.objects.filter(create_time__lt=notice.create_time).order_by('-create_time').first()
    # 다음글
    next_notice = Notice.objects.filter(create_time__gt=notice.create_time).order_by('create_time').first()
    return render(request, 'notice_detail.html', {'notice':notice, 'previous_notice':previous_notice, 'next_notice':next_notice})


@login_required
def notice_new(request):
    if not request.user.is_staff:
        return redirect('notice_list')
    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.author = request.user
            if request.FILES:
                if 'upload_files' in request.FILES.keys():
                    notice.filename = request.FILES['upload_files'].name    
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
        form = NoticeForm(request.POST, request.FILES, instance=notice)
        if form.is_valid():
            notice = form.save(commit=False)
            
            # 삭제 처리
            if request.POST.get('delete_file') and notice.upload_files:
                notice.upload_files.delete()
                notice.upload_files = None
                notice.filename = None
            if 'upload_files' in request.FILES.keys():
                notice.filename = request.FILES['upload_files'].name
                notice.upload_files = request.FILES['upload_files']
            notice.save()
            return redirect('notice:notice_detail', pk=notice.pk)
    else: 
        form = NoticeForm(instance=notice)

    return render(request, 'notice_edit.html', {'form':form})

@login_required
def notice_delete(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    if notice.author != request.user:
        raise PermissionDenied("You are not allowed to edit this notice.")
    notice.delete()
    return redirect('notice:notice_list')

import urllib
import os
from django.http import HttpResponse, Http404
import mimetypes

# 한글명 첨부파일 다운로드
@login_required
def notice_download_view(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    url = notice.upload_files.url[1:]
    file_url = urllib.parse.unquote(url)
    
    if os.path.exists(file_url):
        with open(file_url, 'rb') as fh:
            quote_file_url = urllib.parse.quote(notice.filename.encode('utf-8'))
            response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(file_url)[0])
            response['Content-Disposition'] = 'attachment;filename*=UTF-8\'\'%s' % quote_file_url
            return response
        raise Http404
