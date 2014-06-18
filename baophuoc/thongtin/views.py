from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from libs.lib_navside import *
from thongtin.models import *

def retrieve_data(request, url_tag, template_path):
    content = ThongtinDB.objects.get(url_tag=url_tag)
    
    print '****: ', type(content.thumbnail)
    
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
    }
    
    return render_to_response(template_path, context_dict)

def thongtin_gioithieu_index(request):
    gioithieu_cat = ThongtinCategory.objects.get(tag='gioithieu')
    tosu_cat = ThongtinCategory.objects.get(tag='tosu')
    thongtin_gioithieu_data = ThongtinDB.objects.filter(category=gioithieu_cat.id)
    thongtin_tosu_data = ThongtinDB.objects.filter(category=tosu_cat.id)
    
    context_dict = {
        'thongtin_update': get_thongtin_update(),
        'phathoc_update': get_phathoc_update(),
        'phapam_update': get_phapam_update(),
        'thuvien_photo_update': get_thuvien_photo_update(),
        'thuvien_video_update': get_thuvien_video_update(),
        'lienket_links': get_lienket_link(),
        'sukien_date': get_sukien(),
        'links': topnews(),
        'thongtin_gioithieu_data': thongtin_gioithieu_data,
        'thongtin_tosu_data': thongtin_tosu_data
    }
    
    return render_to_response('thongtin/thongtin_gioithieu_index.html', context_dict)

def thongtin_thongbao_index(request):
    thongbao_cat = ThongtinCategory.objects.get(tag='thongbao')
    content_list = ThongtinDB.objects.filter(category_id=thongbao_cat.id).order_by('date')
    paginator = Paginator(content_list, 10) # Show 5 titles per page
    
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
        'contents': contents,
    }
    return render_to_response('thongtin/thongtin_thongbao_index.html', context_dict)

def thongtin_gioithieu(request, url_tag):
    return retrieve_data(request, url_tag, 'thongtin/thongtin_gioithieu.html')

def thongtin_thongbao(request, url_tag):
    return retrieve_data(request, url_tag, 'thongtin/thongtin_thongbao.html')