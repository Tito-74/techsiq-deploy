from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    # blog
    path('details/', views.Blog_lists, name='details'),
    path('update_blog/<id>', views.update_Blog_list, name='update_blog'),
    path('delete_blog/<id>', views.delete_Blog, name='delete_Blog'),
    path('create_blog/', views.create_blog, name='create_blog'),
    path('getSingle_blog/<id>', views.fetch_single_blog, name='get_single_blog'),

    #category
    path('category/details/', views.fetch_Category, name='category'),
    path('single_category/<id>', views.fetch_single_category, name='single_category'),
    path('update_category/<id>', views.update_category, name='update_category'),
    path('delete_category/<id>', views.delete_category, name='delete_category'),
    path('create_category/', views.create_category, name='create_category'),

    # techsiq team 
    path('techsiq/team/', views.get_techsiq_team, name='techsiq'),
    path('techsiq/team/<id>', views.get_single_techsiq_team, name='single_team'),
    path('update/techsiq/team/<id>', views.update_techsiq_team, name='update_team'),
    path('delete/techsiq/team/<id>', views.delete_techsiq_team, name='delete_category'),
    path('create_techsiq/team/', views.create_techsiq_team, name='create_team'),

    # Application part
    path('application/list/', views.get_cohort_application_list, name='applicants_list'),
    path('applicant/info/<id>', views.get_single_applicant_info, name='single_team'),
    path('update/applicant/info/<id>', views.update_applicant_info, name='update_team'),
    path('delete/applicant/info/<id>', views.delete_applicant_info, name='delete_'),
    path('apply/', views.create_application, name='create_application'),

]