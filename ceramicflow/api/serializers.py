from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from forum.models import Post, Comments
from supplier.models import Suppliers, Reviews
from administration.models import Inventory, Sales

# class UserSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = User
# 		fields = ('correo','nombre')

class PostSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ('id','user','created','content','likes','image')
    def get_imagen(self, obj):
        return obj.image.url

class CommentsSerializer(serializers.ModelSerializer):
	post = PostSerializer()
	class Meta:
		model = Comments
		fields = ('id','user','comment','post','likes')

class SuppliersSerializer(serializers.ModelSerializer):
	class Meta:
		model = Suppliers
		fields = ('id','rating','name','description')

class ReviewsSerializer(serializers.ModelSerializer):
	supplier = SuppliersSerializer()
	class Meta:
		model = Reviews
		fields = ('id','user', 'supplier','rating','comment')

class InventorySerializer(serializers.ModelSerializer):
	image = serializers.SerializerMethodField()
	class Meta:
		model = Inventory
		fields = ('id','name', 'description','cost','price', 'aviable', 'user','image')
	def get_imagen(self, obj):
        return obj.image.url

class SalesSerializer(serializers.ModelSerializer):
	product = InventorySerializer()
	class Meta:
		model = Sales
		fields = ('id','product', 'quantity')