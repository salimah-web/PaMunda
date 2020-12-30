from django.urls import path
from .views import home, details,all_product,categories,trans,charge,success_msg,add_post,delete,update
urlpatterns=[
    path('', home, name='homepage'),
    path('product_list', all_product.as_view(), name='all_product'),
    path('add_post', add_post.as_view(), name='add_post'),
    #path('add_profile', add_profile.as_view(), name='add_profile'),
    path('details/<int:pk>/', details, name='detail'),
    path('category/<str:cats>/', categories, name='category'),
    path('details/<int:pk>/trans', trans, name='trans'),
    path('charge/', charge, name='charge'),
    path('success/', success_msg, name='success'),
    path('update/<int:pk>/', update, name='update'),
    #path('update_profile/<int:pk>/', update_profile.as_view(), name='update_profile'),
    path('delete/<int:pk>/', delete, name='delete')
]