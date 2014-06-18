from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from libs.lib_navside import *
from phapam.models import PhapamDB, PhapamCategory
import json

def retrieve_data(request, url_tag, template_path):
    context = RequestContext(request)
    content = get_object_or_404(PhapamDB, url_tag=url_tag)
    phapam_data = PhapamDB.objects.filter(category=content.category).order_by('-date')[:10]
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
        'phapam_data': phapam_data
    }
    return render_to_response(template_path, context_dict, context)

def phapam_index(request, cat_tag):
    cat = PhapamCategory.objects.get(tag=cat_tag)
    cat_id = cat.id
    content_list = PhapamDB.objects.filter(category_id=cat_id).order_by('date')
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
    return render_to_response('phapam/phapam_index.html', context_dict)

def phapam_radio(request, url_tag):
    return retrieve_data(request, url_tag, 'phapam/phapam_radio.html')

def phapam_phapthoai_hangngay(request, url_tag):
    return retrieve_data(request, url_tag, 'phapam/phapam_phapthoai_hangngay.html')

def phapam_phapthoai_chunhat(request, url_tag):
    return retrieve_data(request, url_tag, 'phapam/phapam_phapthoai_chunhat.html')

def phapam_phapthoai_batquantrai(request, url_tag):
    return retrieve_data(request, url_tag, 'phapam/phapam_phapthoai_batquantrai.html')