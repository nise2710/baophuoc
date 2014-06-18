""" collection of functions for navigation - sidebar """
   
def topnews():
    from thongtin.models import ThongtinDB
    links = ThongtinDB.objects.filter(news_display=1).order_by('-date')
    return links

def get_thongtin_update():
    from thongtin.models import ThongtinDB
    return ThongtinDB.objects.order_by('-date')[:1]

def get_phathoc_update():
    from phathoc.models import PhathocDB
    return PhathocDB.objects.order_by('-date')[:1]

def get_phapam_update():
    from phapam.models import PhapamDB
    return PhapamDB.objects.order_by('-date')[:1]

def get_thuvien_photo_update():
    from thuvien.models import ContentPhoto
    return ContentPhoto.objects.order_by('-date')[:1]

def get_thuvien_video_update():
    from thuvien.models import ContentVideo
    return ContentVideo.objects.order_by('-date')[:1]

def get_lienket_link():
    from trangchu.models import LienKetLink
    return LienKetLink.objects.all()

def get_sukien():
    from trangchu.models import SuKienDate
    return SuKienDate.objects.all()
    