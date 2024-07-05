from django.http import JsonResponse
from django.shortcuts import render
from .models import Category, Author, News, Region
# Create your views here.

def category_api(request):
    categories = Category.objects.all()
    context_json = {'categories': []}

    for category in categories:
        context_json['categories'].append(
            {'id': category.id,
             'name': category.name}
        )

    return JsonResponse(context_json)

def region_api(request):
    regions = Region.objects.all()
    context_json = {'regions': []}

    for region in regions:
        context_json['regions'].append(
            {'id': region.id,
             'name': region.name}
        )

    return JsonResponse(context_json)


def news_api(request):
    news = News.objects.all()
    context_json = {'news': []}

    for new in news:
        context_json['news'].append(
            {'id': new.id,
             'title': new.title,
             'content': new.content,
             'published_date': new.published_date,
             'img': new.img.url,
             'category': new.category.name,
             'region': new.region.name,
             'author': {'first_name': new.author.first_name,
                        'last_name': new.author.last_name
                        }
             }
        )

    return JsonResponse(context_json)