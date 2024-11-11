from django.urls import path


from . import views

urlpatterns = [
    path("mylist/", views.CarCollectionView.as_view()),
    path("<int:pk>/", views.CarSingletonView.as_view()),
    path('list/', views.CarListView.as_view(), name='car_list')
]