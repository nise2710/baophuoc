from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from libs.lib_navside import *
from thuvien.models import ThuvienCategory, ContentVideo, ContentPhoto, ContentPhotoLink
import json

def thuvien_photo_index(request):
    cat = ThuvienCategory.objects.get(tag='hinhanh')
    cat_id = cat.id
    content_list = ContentPhoto.objects.filter(category_id=cat_id).order_by('-date')
    paginator = Paginator(content_list, 10) # Show 10 titles per page
    # divide pages
    page = request.GET.get('page')
    try:
        contents = paginator.page(page)
    except PageNotAnInteger:
        contents = paginator.page(1)
    except EmptyPage:
        contents = paginator.page(paginator.page_number)
    
    context_dict = {
        'thongtin_update': get_thongtin_update(),
        'phathoc_update': get_phathoc_update(),
        'phapam_update': get_phapam_update(),
        'thuvien_photo_update': get_thuvien_photo_update(),
        'thuvien_video_update': get_thuvien_video_update(),
        'lienket_links': get_lienket_link(),
        'sukien_date': get_sukien(),
        'links': topnews(),
        'cat': cat,
        'contents': contents,
    }
    return render_to_response('thuvien/thuvien_photo_index.html', context_dict)

def thuvien_video_index(request):
    cat = ThuvienCategory.objects.get(tag='video')
    cat_id = cat.id
    content_list = ContentVideo.objects.filter(category_id=cat_id).order_by('-date')
    paginator = Paginator(content_list, 10) # Show 10 titles per page
    # divide pages
    page = request.GET.get('page')
    try:
        contents = paginator.page(page)
    except PageNotAnInteger:
        contents = paginator.page(1)
    except EmptyPage:
        contents = paginator.page(paginator.page_number)
    
    context_dict = {
        'thongtin_update': get_thongtin_update(),
        'phathoc_update': get_phathoc_update(),
        'phapam_update': get_phapam_update(),
        'thuvien_photo_update': get_thuvien_photo_update(),
        'thuvien_video_update': get_thuvien_video_update(),
        'lienket_links': get_lienket_link(),
        'sukien_date': get_sukien(),
        'links': topnews(),
        'cat': cat,
        'contents': contents,
    }
    return render_to_response('thuvien/thuvien_video_index.html', context_dict)

def thuvien_photo(request,url_tag):
    context = RequestContext(request)
    content = get_object_or_404(ContentPhoto, url_tag=url_tag)
    photo_url = ContentPhotoLink.objects.filter(content_photo=content.id)
    thuvien_data = ContentPhoto.objects.filter(category=content.category).order_by('-date')[:10]
    content.views+=1 # increase views record
    content.save()
    context_dict = {
        'thongtin_update': get_thongtin_update(),
        'phathoc_update': get_phathoc_update(),
        'phapam_update': get_phapam_update(),
        'thuvien_photo_update': get_thuvien_photo_update(),
        'thuvien_video_update': get_thuvien_video_update(),
        'lienket_links': get_lienket_link(),
        'sukien_date': get_sukien(),
        'links': topnews(),
        'content': content,
        'photo_url': photo_url,
        'thuvien_data': thuvien_data
    }
    return render_to_response('thuvien/thuvien_photo.html', context_dict, context)

def thuvien_video(request, url_tag):
    context = RequestContext(request)
    content = get_object_or_404(ContentVideo, url_tag=url_tag)
    thuvien_data = ContentVideo.objects.filter(category=content.category).order_by('-date')[:10]
    content.views+=1 # increase views record
    content.save()
    json_data = json.dumps({'url':content.url})
    context_dict = {
        'thongtin_update': get_thongtin_update(),
        'phathoc_update': get_phathoc_update(),
        'phapam_update': get_phapam_update(),
        'thuvien_photo_update': get_thuvien_photo_update(),
        'thuvien_video_update': get_thuvien_video_update(),
        'lienket_links': get_lienket_link(),
        'sukien_date': get_sukien(),
        'links': topnews(),
        'content': content,
        'json_data': json_data,
        'thuvien_data': thuvien_data
    }
    return render_to_response('thuvien/thuvien_video.html', context_dict, context)