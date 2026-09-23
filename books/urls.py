from django.urls import path
from . import views
urlpatterns=[
 path('favorites/',views.favorites,name='favorites'), path('books/<int:pk>/favorite/',views.toggle_favorite,name='toggle_favorite'),
 path('books/<int:pk>/contact/',views.contact_seller,name='contact_seller'), path('messages/',views.messages_inbox,name='messages_inbox'), path('messages/<int:pk>/status/<str:status>/',views.message_status,name='message_status'),
 path('books/<int:pk>/report/',views.report_listing,name='report_listing'),
]
