from django.http import HttpResponse
def about(request):
	return HttpResponse('Hello, mouse!')