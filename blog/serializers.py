from rest_framework import serializers

from blog.models import Blog, Category, TechsiqTeam, CohortApplication


class BlogSerializer(serializers.ModelSerializer):
  class Meta:
    model = Blog
    fields = ['id','title','images', 'body','date_published']
    # 


class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = '__all__'

class TechsiqTeamSerializer(serializers.ModelSerializer):
  class Meta:
    model = TechsiqTeam
    fields = '__all__'


class CohortApplicationSerializer(serializers.ModelSerializer):
  class Meta:
    model = CohortApplication
    fields = '__all__'