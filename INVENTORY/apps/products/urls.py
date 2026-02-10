from django.urls import path
from apps.products.views import productViews
from apps.products.views import ProductGRNView
urlpatterns = [
    path('CreateMainCategory/',productViews.CreateMainCategory.as_view()),
    path('CreateSubCategory/',productViews.CreateSubCategory.as_view()),
    path('CreateProducts/',productViews.CreateProductMaster.as_view()),
    path('CreateGRN/',ProductGRNView.CreateProductGRN_hdr.as_view())
]
