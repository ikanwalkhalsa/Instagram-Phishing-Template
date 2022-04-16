from django.urls import path
import login.views
urlpatterns = [
    path('', login.views.home)
]
