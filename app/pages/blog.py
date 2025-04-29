from flask import render_template

# Örnek blog verileri
BLOG_POSTS = [
    {"title": "Deprem Nedir?", "excerpt": "Depremler hakkında temel bilgiler ve nedenleri...", "url": "/blog/deprem-nedir", "category": "deprem-nedir"},
    {"title": "Deprem Önlemleri", "excerpt": "Deprem sırasında hayatta kalmak için önemli ipuçları...", "url": "/blog/deprem-onlemleri", "category": "deprem-onlemleri"},
    {"title": "Deprem Bölgeleri ve Risk Haritası", "excerpt": "Türkiye'nin deprem bölgeleri ve risk haritası...", "url": "/blog/deprem-bolgeleri", "category": "deprem-bolgeleri"},
    {"title": "Son Deprem Haberleri", "excerpt": "Türkiye ve dünyadan son deprem haberleri...", "url": "/blog/deprem-haberleri", "category": "deprem-haberleri"},
]

def blog_page(category=None):
    if category:
        # Kategoriye göre blog yazılarını filtrele
        filtered_posts = [post for post in BLOG_POSTS if post["category"] == category]
        category_name = category.replace("-", " ").title()  # Kategori adını düzenle
        return render_template("blog_category.html", category_name=category_name, blogs=filtered_posts)
    
    # Tüm blog yazılarını gönder
    return render_template("blog.html", blogs=BLOG_POSTS)