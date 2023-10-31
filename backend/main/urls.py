from django.urls import path, include
#from rest_framework.routers import DefaultRouter
from main.views import BloodPressureAV, WeightAV, FoodCategoryAV

# router = DefaultRouter()
# router.register('bloodpressure', BloodPressureAV)
urlpatterns = [
    path('bloodpressure',BloodPressureAV.as_view(), name='bloodpressure'),
    path('weights',WeightAV.as_view(), name='weights'),
    path('foodcategory',FoodCategoryAV.as_view(), name='foodcategory'),
]
