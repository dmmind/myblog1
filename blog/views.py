from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Category, Banner, Tag, Link
# 插入分页插件包
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request):
    allcategory = Category.objects.all()
    banner = Banner.objects.filter(is_active=True)[0:4]
    tui = Article.objects.filter(tui__id=2)[:3]
    allarticle = Article.objects.all().order_by('-id')[0:10]
    hot = Article.objects.all().order_by('views')[:10]
    remen = Article.objects.filter(tui__id=3)[:6]
    tags = Tag.objects.all()
    link = Link.objects.all()
    context = {
        'allcategory': allcategory,
        'banner': banner,
        'tui': tui,
        'allarticle': allarticle,
        'hot': hot,
        'remen': remen,
        'tags': tags,
        'link': link,
    }
    return render(request, 'index.html', context)


def list(request, lid):
    list= Article.objects.filter(category_id=lid)
    cname = Category.objects.get(id=lid)
    remen = Article.objects.filter(tui__id=3)[:6]
    allcategory = Category.objects.all()
    tags = Tag.objects.all()
    # locals()的作用是返回一个包含当前作用域里面的所有变量和它们的值的字典
    page = request.GET.get('page')
    paginator = Paginator(list, 5)
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return render(request, 'list.html', locals())


def show(request, sid):
    show = Article.objects.get(id=sid)
    allcategory = Category.objects.all()
    tags = Tag.objects.all()
    remen = Article.objects.filter(tui__id=2)[:6]
    hot = Article.objects.all().order_by('?')[:10]
    previous_blog = Article.objects.filter(created_time__gt=show.created_time, category=show.category.id).first()
    next_blog = Article.objects.filter(created_time__lt=show.created_time, category=show.category.id).last()
    show.views = show.views + 1
    show.save()
    return render(request, 'show.html', locals())


def tag(request, tag):
    pass


def search(request):
    ss = request.GET.get('search')
    list = Article.objects.filter(title__icontains=ss)
    remen = Article.objects.filter(tui__id=2)[:6]
    allcategory = Category.objects.all()
    page = request.GET.get('page')
    tags = Tag.objects.all()
    paginator = Paginator(list, 10)
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return render(request, 'search.html', locals())


def about(request):
    allcategory = Category.objects.all()
    return render(request, 'page.html', locals())