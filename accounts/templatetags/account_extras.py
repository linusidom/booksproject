from django import template
register = template.Library()

@register.filter
def index(List, i):
	if List:
		return List[int(i)]
	else:
		return None
