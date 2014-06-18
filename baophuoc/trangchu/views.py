from django.template import RequestContext
from django.shortcuts import render_to_response
from libs.lib_navside import *
from trangchu.models import *
from phathoc.models import *
from phapam.models import *
from thuvien.models import *
from random import randint

def getPhatHocData(cat_tag):
    cat = PhathocCategory.objects.get(tag=cat_tag)
    cat_id = cat.id
    data = PhathocDB.objects.filter(category=cat_id).order_by('date')[:5]
    return data

def getPhapAmData(cat_tag):
    cat = PhapamCategory.objects.get(tag=cat_tag)
    cat_id = cat.id
    data = PhapamDB.objects.filter(category=cat_id).order_by('date')[:10]
    return data

def getThuVienData(cat_tag):
    cat = ThuvienCategory.objects.get(tag=cat_tag)
    cat_id = cat.id
    if cat_tag == 'hinhanh':
        data = ContentPhoto.objects.filter(category=cat_id).order_by('date')[:10]
    if cat_tag == 'video':
        data = ContentVideo.objects.filter(category=cat_id).order_by('date')[:10]
    return data

def randomPicture(n):
    """ pick n random pictures for main slideshow """
    data = []
    slide_photo = SlidePhoto.objects.get(display=1)
    total_link = SlideLink.objects.count()
    for i in range(n):
        while True:
            j = randint(1, total_link)
            if j not in data:
                data.append(j)
                break
    obj = SlideLink.objects.filter(id__in=data)
    print obj
    return obj

def trangchu_index(request):
    context = RequestContext(request)
    notice_text = ContentNoticeText.objects.filter(display = 1).order_by('-date')[:5]
    notice_links = ContentNotice.objects.filter(display=1).order_by('-date')[:5]
    context_dict = {
        'thongtin_update': get_thongtin_update(),
        'phathoc_update': get_phathoc_update(),
        'phapam_update': get_phapam_update(),
        'thuvien_photo_update': get_thuvien_photo_update(),
        'thuvien_video_update': get_thuvien_video_update(),
        'lienket_links': get_lienket_link(),
        'sukien_date': get_sukien(),
        'links': topnews(),
        'slide_photo_url': SlideLink.objects.all(),
        'notice_text': notice_text,
        'notice_links': notice_links,
        'phathoc_canban': getPhatHocData('phathoccanban'),
        'phathoc_chuyensau': getPhatHocData('phathocchuyensau'),
        'phathoc_treem': getPhatHocData('phathocchotreem'),
        'phapthoai_hangngay': getPhapAmData('phapthoai_hangngay'),
        'phapthoai_batquantrai': getPhapAmData('phapthoai_batquantrai'),
        'thuvien_hinhanh': getThuVienData('hinhanh'),
        'thuvien_video': getThuVienData('video'),
    }
    return render_to_response('trangchu/trangchu_index.html', context_dict, context)
