from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from thongtin.sidebar import thongtin_sidebar
from thongtin.models import Content, Category

context_dict = {
	# use for dropdown level only
    'gioi_thieu_data': thongtin_sidebar(1),
    'thong_bao_data': thongtin_sidebar(3),
} 
      
def retrieve_data(request, url_tag, dict_key, template_path):
    context = RequestContext(request)
    content = get_object_or_404(Content, url_tag=url_tag)
    context_dict[dict_key] = content
    print context_dict
    return render_to_response(template_path, context_dict, context)

def thongtin_gioithieu(request, url_tag):
    return retrieve_data(request, url_tag, 'gioithieu', 'thongtin/thongtin_gioithieu.html')

def thongtin_thongbao(request, url_tag):
    return retrieve_data(request, url_tag, 'thongbao', 'thongtin/thongtin_thongbao.html')
	
def thongtin_tonchi(request, url_tag): 
	return retrieve_data(request, url_tag, 'tonchi', 'thongtin/thongtin_tonchi.html')