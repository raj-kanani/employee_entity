from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
router = DefaultRouter()
router.register('emp2', views.EmployeeView, basename='employee2')

urlpatterns = [
    path('emp', views.EmployeeListView.as_view(), name='employee'),
    # path('emp1', views.EmployeeGetSalary.as_view(), name='employee1'),
    path('', include(router.urls))
]
