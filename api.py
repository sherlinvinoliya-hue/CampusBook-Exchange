from rest_framework import generics,permissions
from rest_framework.exceptions import PermissionDenied
from .models import Book,Category
from .serializers import BookSerializer,CategorySerializer,FavoriteSerializer,MessageSerializer
from interactions.models import Favorite
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self,request,view,obj): return request.method in permissions.SAFE_METHODS or obj.seller==request.user
class BookListCreate(generics.ListCreateAPIView):
    serializer_class=BookSerializer; permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self): return Book.objects.filter(is_approved=True).select_related('category','seller').prefetch_related('images')
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=BookSerializer; permission_classes=[IsOwnerOrReadOnly]; queryset=Book.objects.filter(is_approved=True)
class CategoryList(generics.ListAPIView): serializer_class=CategorySerializer; permission_classes=[permissions.AllowAny]; queryset=Category.objects.all()
class FavoriteCreate(generics.CreateAPIView): serializer_class=FavoriteSerializer; permission_classes=[permissions.IsAuthenticated]
class FavoriteDelete(generics.DestroyAPIView): serializer_class=FavoriteSerializer; permission_classes=[permissions.IsAuthenticated]
    
class UserFavoriteDelete(FavoriteDelete):
    def get_queryset(self): return Favorite.objects.filter(user=self.request.user)
class MessageCreate(generics.CreateAPIView): serializer_class=MessageSerializer; permission_classes=[permissions.IsAuthenticated]
