# coding:utf-8
from django import template
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
register = template.Library()

@register.simple_tag(takes_context=True)
def paginate(context, object_list, page_count):
	left = 3
	right = 3
	paginator = Paginator(object_list, page_count)
	page = context['request'].GET.get('page')

	try:
		object_list = paginator.page(page)
		context['current_page'] = int(page)
		pages = get_left(context['current_page'], left, paginator.num_pages) + get_right(context['current_page'], right, paginator.num_pages)
	except PageNotAnInteger:

		object_list = paginator.page(1) # 获取首页数据页码对象
		context['current_page'] = 1
		pages = get_right(context['current_page'], right, paginator.num_pages)
	except EmptyPage:
		object_list = paginator.page(paginator.num_pages)
		context['currten_page'] = paginator.num_pages
		pages = get_left(context['current_page'], left, paginator.num_pages)

	context['questions'] = object_list
	context['pages'] = pages  # 页码列表
	context['last_page'] = paginator.num_pages
	context['first_page'] = 1

	try:
		context['pages_first'] = pages[0]
		context['pages_last'] = pages[-1] + 1
	except IndexError:
		context['pages_first'] = 1
		context['pages_last'] = 2
	return ''
def get_left(current_page, left, num_pages):

  """
  辅助函数，获取当前页码的值得左边两个页码值，要注意一些细节，比如不够两个那么最左取到2
  ，为了方便处理，包含当前页码值，比如当前页码值为5，那么pages = [3,4,5]
  """
  if current_page == 1:
  	return []
  elif current_page == num_pages:
		l = [i - 1 for i in range(current_page, current_page - left, -1) if i - 1 > 1]
		l.sort()
		return l
  l = [i for i in range(current_page, current_page - left, -1) if i > 1]
  l.sort()
  return l
def get_right(current_page, right, num_pages):
  """
  辅助函数，获取当前页码的值得右边两个页码值，要注意一些细节，
  比如不够两个那么最右取到最大页码值。不包含当前页码值。比如当前页码值为5，那么pages = [6,7]
  """
  if current_page == num_pages:
		return []
  return [i + 1 for i in range(current_page, current_page + right - 1) if i < num_pages - 1]















