from django.urls import path
from .views import signup, user_login, user_logout, create_form, form_detail, handle_form_submission, main_page

urlpatterns = [
    path('', main_page, name='main_page'),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('create/', create_form, name='create_form'),
    path('<str:form_id>/', form_detail, name='form_detail'),
    path('r/<str:form_id>/', handle_form_submission, name='handle_form_submission'),
]
