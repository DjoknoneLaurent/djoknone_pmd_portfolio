from django.shortcuts import render, get_object_or_404
from .models import Article, Category, Tag


def article_list(request):
    """Liste des articles publiés"""
    articles = Article.objects.filter(status='published').select_related('category').prefetch_related('tags')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    # Filtrage par catégorie
    category_slug = request.GET.get('category')
    if category_slug:
        articles = articles.filter(category__slug=category_slug)
    
    # Filtrage par tag
    tag_slug = request.GET.get('tag')
    if tag_slug:
        articles = articles.filter(tags__slug=tag_slug)
    
    context = {
        'articles': articles,
        'categories': categories,
        'tags': tags,
        'current_category': category_slug,
        'current_tag': tag_slug,
    }
    return render(request, 'app_blog/article_list.html', context)


def article_detail(request, slug):
    """Détail d'un article"""
    article = get_object_or_404(Article, slug=slug, status='published')
    
    # Incrémenter le compteur de vues
    article.views_count += 1
    article.save(update_fields=['views_count'])
    
    # Articles similaires (même catégorie)
    similar_articles = Article.objects.filter(
        category=article.category,
        status='published'
    ).exclude(id=article.id)[:3]
    
    context = {
        'article': article,
        'similar_articles': similar_articles,
    }
    return render(request, 'app_blog/article_detail.html', context)