from rest_framework import serializers
from .models import Book,Category,BookImage
from interactions.models import Favorite,ContactRequest
class CategorySerializer(serializers.ModelSerializer):
    class Meta: model=Category; fields=('id','name','slug')
class BookImageSerializer(serializers.ModelSerializer):
    class Meta: model=BookImage; fields=('id','image','position')
class BookSerializer(serializers.ModelSerializer):
    seller=serializers.CharField(source='seller.username',read_only=True); images=BookImageSerializer(many=True,read_only=True); category_name=serializers.CharField(source='category.name',read_only=True)
    class Meta: model=Book; fields='__all__'; read_only_fields=('seller','is_approved','created_at','updated_at')
    def create(self,validated_data): validated_data['seller']=self.context['request'].user; return super().create(validated_data)
class FavoriteSerializer(serializers.ModelSerializer):
    class Meta: model=Favorite; fields=('id','book','created_at'); read_only_fields=('created_at',)
    def validate(self,attrs):
        if Favorite.objects.filter(user=self.context['request'].user,book=attrs['book']).exists(): raise serializers.ValidationError('Already favorited.')
        return attrs
    def create(self,validated_data): return Favorite.objects.create(user=self.context['request'].user,**validated_data)
class MessageSerializer(serializers.ModelSerializer):
    class Meta: model=ContactRequest; fields=('id','book','message','optional_contact','status','created_at'); read_only_fields=('status','created_at')
    def create(self,validated_data):
        user=self.context['request'].user; book=validated_data['book']
        if book.seller==user: raise serializers.ValidationError('Cannot contact yourself.')
        return ContactRequest.objects.create(buyer=user,seller=book.seller,**validated_data)
