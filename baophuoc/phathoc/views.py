from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from libs.lib_navside import *
from phathoc.models import PhathocDB, PhathocCategory


def retrieve_data(request, url_tag, template_path):
    context = RequestContext(request)
    contents = get_object_or_404(PhathocDB, url_tag=url_tag)
    contents.views += 1
    contents.save()
    context_dict = {
        'thongtin_update': get_thongtin_update(),
        'phathoc_update': get_phathoc_update(),
        'phapam_update': get_phapam_update(),
        'thuvien_photo_update': get_thuvien_photo_update(),
        'thuvien_video_update': get_thuvien_video_update(),
        'lienket_links': get_lienket_link(),
        'sukien_date': get_sukien(),
        'links': topnews(),
        'contents': contents
    }
    return render_to_response(template_path, context_dict, context)

def phathoc_index(request, cat_tag):
    cat = PhathocCategory.objects.get(tag=cat_tag)
    cat_id = cat.id
    content_list = PhathocDB.objects.filter(category_id=cat_id).order_by('date')
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
        'cat': cat,
        'contents': contents,
    }
    return render_to_response('phathoc/phathoc_index.html', context_dict)

def phathoc_canban(request, url_tag):
    return retrieve_data(request, url_tag, 'phathoc/phathoc_canban.html')

def phathoc_chuyensau(request, url_tag):
    return retrieve_data(request, url_tag, 'phathoc/phathoc_chuyensau.html')

def phathoc_chotreem(request, url_tag):
    return retrieve_data(request, url_tag, 'phathoc/phathoc_chotreem.html')

def phathoc_thienhoc(request, url_tag):
    return retrieve_data(request, url_tag, 'phathoc/phathoc_thienhoc.html')

def phathoc_tinhdo(request, url_tag):
    return retrieve_data(request, url_tag, 'phathoc/phathoc_tinhdo.html')

def phathoc_mattong(request, url_tag):
    return retrieve_data(request, url_tag, 'phathoc/phathoc_mattong.html')