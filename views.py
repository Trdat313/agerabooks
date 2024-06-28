from django.http import HttpResponse

def index(reqest):
    return HttpResponse('главная страница')
def group_posts(reqest, slug):
    return HttpResponse('для страницы, на которой будут посты, отфильтрованые по группам')