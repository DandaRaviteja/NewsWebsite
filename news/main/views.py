from django.shortcuts import render
from django.shortcuts import render
from .models import Articles,View,ArticleView,Categories
from django.http import HttpResponse
from django.utils import timezone
from django.db import models
from datetime import timedelta
# Create your views here.
def article(request,slug):
    
    article = Articles.objects.filter(slug=slug).first()
    
    


    
    if article:
        
        article_id=article.article_id
        views = View.objects.filter(article_id=article_id)
        
        
        #session_key = f'viewed_article_{article_id}'
        
    

        #if not request.session.get(session_key, False):
        article.view_count += 1

        article.save()
        ArticleView.objects.create(article=article, viewed_at=timezone.now())
        #request.session[session_key] = True
    
        return render(request, 'main/article.html',{'article': article,'views':views})
    else:
       
        return HttpResponse("Article not found", status=404)
    

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def vote(request):
    if request.method == "POST":
        data = json.loads(request.body)
        option_id = data.get('option_id')

        try:
            option = View.objects.get(view_id=option_id)
            option.polled_votes += 1
            option.save()
            
            return JsonResponse({'success': True, 'message': 'Vote recorded.'})
        except PollOption.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Invalid option.'})

    return JsonResponse({'success': False, 'message': 'Invalid request.'})

def get_poll_results(request, poll_id):
    # Fetch all options for the poll
    options = View.objects.filter(article_id=poll_id)
    
    if not options.exists():
        # If no options are found, return a 'Poll not found' message
        return JsonResponse({'success': False, 'message': 'Poll not found.'})

    # Process the results if options exist
    results = {option.view_id: option.polled_votes for option in options}
    total_votes = sum(results.values())
    results['total_votes'] = total_votes
    
    return JsonResponse(results)



def home(request):
   
    latest_articles = Articles.objects.order_by('-created_at')[:10]
    
    last_24_hours = timezone.now() - timedelta(hours=24)
    
   
    trending_articles2 = (
        ArticleView.objects.filter(viewed_at__gte=last_24_hours).values('article').annotate(view_count=models.Count('article')).order_by('-view_count')[:10])
    trending_article_ids2 = [item['article'] for item in trending_articles2]
    trending_articles2=[]
    for ind,id in enumerate(trending_article_ids2):
     trending_articles2.append(Articles.objects.get(article_id=id))
    categories = Categories.objects.all()
    poltics=Articles.objects.filter(category='Poltics').order_by('-created_at')[:10]
    film=Articles.objects.filter(category='Film').order_by('-created_at')[:10]
    International=Articles.objects.filter(category='International').order_by('-created_at')[:10]
    print(len(poltics))
    #print(categories)
    category_articles = {category: Articles.objects.filter(category=category).order_by('-created_at')[:10] for category in categories}
    
    print(category_articles.get('Film'))
    context = {
        'latest_articles': latest_articles,
        'trending_articles': trending_articles2,
        'Poltics': poltics,
        'Film':film,
        'International':International
    }
    
    return render(request, 'main/index.html', context)
