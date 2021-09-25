from leads.api import LeadViewset
from django.urls import path
from rest_framework import routers, urlpatterns
from .api import LeadViewset

router = routers.DefaultRouter()
router.register('api/leads',LeadViewset, 'leads')

app_name = 'leads'

urlpatterns = router.urls