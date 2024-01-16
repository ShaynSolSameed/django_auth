from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Article, Author
from django.views.decorators.csrf import csrf_exempt

def get_articles(request):
    articles = Article.objects.all()
    if len(articles) == 0:
        print("no articles exist")
    return articles
    
def add_article(request):
    headline = request.body.headline
    
@csrf_exempt    
def author(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name', '')
        new_author = Author(full_name=full_name)
        new_author.save()
        return HttpResponse("status: Author added successfully", status=201)
    elif request.method == 'GET':
        author_name = request.GET.get('author_name', None)

        if author_name is None:
            return JsonResponse({"error": "author_name not included in request"}, status=400)

        authors = Author.objects.filter(full_name=author_name)

        if authors.exists():
            author_list = []
            for author in authors:
                author_data = {
                    "id": author.id,
                    "full_name": author.full_name,
                    # Add other fields as needed
                }
                author_list.append(author_data)

            return JsonResponse({"authors": author_list})
        else:
            return JsonResponse({"error": "Authors not found"}, status=404)
        