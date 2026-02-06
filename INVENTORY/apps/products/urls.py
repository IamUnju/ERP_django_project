from django.urls import path
from apps.products.views import productViews
urlpatterns = [
    path('CreateMainCategory/',productViews.CreateMainCategory.as_view()),
    path('CreateSubCategory/',productViews.CreateSubCategory.as_view()),
]
