from .views import article_list , article_detail ,ArticleAPIView,ArticleDetail,GenericAPIView, ArticleViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register ('article',ArticleViewSet,basename='article' )


urlpatterns = [
    path('viewset/', include(router.urls)),
    path('article/<int:id>/', GenericAPIView.as_view()),
    path('article/', GenericAPIView.as_view()),
    path('detail/<int:id>/', ArticleDetail.as_view()),
    
]