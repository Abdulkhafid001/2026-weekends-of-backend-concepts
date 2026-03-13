from django.urls import path
from . import views
urlpatterns = [
    path('blog/', views.paginated_blogposts),
    path('blog/detail/<int:pk>', views.BlogDetailView.as_view())
]
