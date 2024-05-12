from django.urls import path
from .views import PenulisListView, PenulisDetailView, 
                     KategoriListView, KategoriDetailView, 
                     BukuListView, BukuDetailView, 
                     # Add your other view functions here)

urlpatterns = 
    path('penulis/', PenulisListView.as_view()),
    path('penulis/<int:pk>/', PenulisDetailView.as_view()),
    path('kategori/', KategoriListView.as_view()),
    path('kategori/<int:pk>/', KategoriDetailView.as_view()),
    path('buku/', BukuListView.as_view()),
    path('buku/<int:pk>/', BukuDetailView.as_view()),
    # Add URL patterns for your other views here

urlpatterns = [format_suffix_patterns(urlpatterns)
]
