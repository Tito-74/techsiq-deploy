from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import BlogSerializer, CategorySerializer, TechsiqTeamSerializer, CohortApplicationSerializer
# , cohortApplicationSerializer
# , CategorySerializer, CommentSerializer 
from .models import Blog, Category, TechsiqTeam, CohortApplication
# , Comment
from django.shortcuts import get_object_or_404
# Create your views here.

# blog crud functions
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def Blog_lists(request):
  user = request.user
  
  try:
    # blog = user.blog_set.all()
    blog = Blog.objects.all()
  except Blog.DoseNotExist:
    return Response(status = status.Http_404_NOT_FOUND)
  if request.method == 'GET':
        # blog = Blog.objects.all()
        serializer = BlogSerializer(blog, many=True)
        return Response(serializer.data)


@api_view(['PUT'])
def update_Blog_list(request, id):

  try:
    blog = Blog.objects.get(pk=id)
  except Blog.DoseNotExist:
    return Response(status = status.Http_404_NOT_FOUND)
  if request.method == 'PUT':
        # blog = Blog.objects.all()
        serializer = BlogSerializer(blog, data=request.data)
        data = {}
        if serializer.is_valid():
          serializer.save()
          data["Success"] = "Updated Successfully"
          return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_Blog(request, id):

  try:
    blog = Blog.objects.get(pk=id)
  except Blog.DoseNotExist:
    return Response(status = status.Http_404_NOT_FOUND)
  if request.method == 'DELETE':
        operations =  blog.delete()
        data = {}
        if operations:
          data["Success"] = "Deleted Successfully"
        else:
          data["Failed"] = "Failed to Delete"

        return Response(data=data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_blog(request):
  if request.method == 'POST':
        serializer = BlogSerializer(data = request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def fetch_single_blog(request, id):
  
    try:
     blog = Blog.objects.get(pk=id) 
    except Blog.DoesNotExist:
      return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method =='GET':
      serializer = BlogSerializer(blog)
      return Response(serializer.data)



# category crud functions

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_category(request):
  if request.method == 'POST':
    serializer = CategorySerializer(data = request.data)
    if serializer.is_valid():
      serializer.Save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def fetch_Category(request):
  try:
    category = Category.objects.all()
  except Category.DoseNotExist:
    return Response(status = status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def fetch_single_category(request, id):

  try:
    category = Category.objects.get(pk=id)
  except Category.DoesNotExist:
    return Response(status = status.HTTP_404_NOT_FOUND)

  if request.method =='GET':
    serializer = CategorySerializer(category)
    return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_category(request, id):

  try:
    category = Category.objects.get(pk=id)

  except Category.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  if request.method == 'PUT':
    serializer = CategorySerializer(category, data=request.data)
    data = {}
    if serializer.is_valid():
      serializer.save()
      data['success'] = "Updated successfully"
      return Response(data = data)
    return Response(status = status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_category(request, id):

  try:
    category = Category.objects.get(pk=id)

  except Category.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  if request.method == 'DELETE':
    operations = category.delete()
    data = {}
    if operations:
      data['success'] = "Deleted Successfully"
    else:
      data['failed']  = "Failed to Delete"
    return Response(data=data)
  return Response(status=status.HTTP_400_BAD_REQUEST)


# TechsiqTeam crud functions

@api_view(['GET'])
def get_techsiq_team(request):
  try:
    team = TechsiqTeam.objects.all()
  except TechsiqTeam.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    serializer = TechsiqTeamSerializer(team, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_single_techsiq_team(request, id):
  try:
    team = TechsiqTeam.objects.get(pk=id)
  except TechsiqTeam.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  if request.method == 'GET':
    serializer = TechsiqTeamSerializer(team)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_techsiq_team(request, id):
  try:
    team = TechsiqTeam.objects.get(pk=id)
  except TechsiqTeam.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_NOT_)
  if request.method == 'PUT':
    serializer = TechsiqTeamSerializer(team, data=request.data)
    data = {}
    if serializer.is_valid():
      serializer.save()
      data["success"] ="Updated successfully"
      return Response(data=data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['Delete'])
@permission_classes([IsAuthenticated])
def delete_techsiq_team(request, id):
  try:
    team = TechsiqTeam.objects.get(pk=id)
  except TechsiqTeam.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  if request.method == 'DELETE':
    operations = team.delete()
    data= {}
    if operations:
      data["Success"] = "Deleted Successfully"
      return Response(data=data)
    else:
      data["Failed"] = "Failed to Delete"

      return Response(data=data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_techsiq_team(request):
  if request.method == 'POST':
    serializer = TechsiqTeamSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# cohort application models

@api_view(['GET'])
def get_cohort_application_list(request):
  try:
    list = CohortApplication.objects.all()
  except CohortApplication.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  if request.method == 'GET':
    serializer = CohortApplicationSerializer(list, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_single_applicant_info(request,id):
  try:
    applicant = CohortApplication.objects.get(pk=id)

  except CohortApplication.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = CohortApplicationSerializer(applicant)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_applicant_info(request,id):
  try:
    info = CohortApplication.objects.get(pk=id)
  
  except CohortApplication.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'PUT':
    serializer = CohortApplicationSerializer(info, data = request.data)
    data = {}
    if serializer.is_valid():
      serializer.save()
      data["Success"] ="Updated Successfully"
      return Response(data=data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

  
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_applicant_info(request, id):
  try:
    info = CohortApplication.objects.get(pk=id)
  
  except CohortApplication.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'DELETE':
    operations = CohortApplication.delete()
    data = {}
    if operations:
      data["Success"] = "Deleted Successfully"
      return Response(data=data)
    else:
      data["failed"] = "Failed to Delete"
      return Response(data=data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_application(request):
  if request.method == 'POST':
      serializer = CohortApplicationSerializer(data = request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)