from thongtin.models import Content

def thongtin_sidebar(s):
    data = Content.objects.filter(category_id=s, display=1).order_by('date')
    return data
    