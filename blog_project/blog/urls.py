from django.urls import path
from .views import home, post_detail, register, logout_view, create_post, login_view,update_post  # ✅ Import login_view

urlpatterns = [
    path('', home, name='blog-home'),
    path('post/<int:post_id>/', post_detail, name='post-detail'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),  # ✅ Added Login Page
    path('logout/', logout_view, name='logout'),
    path('create/', create_post, name='create-post'),
    path('post/update/<int:post_id>/', update_post, name='update-post'),

]
