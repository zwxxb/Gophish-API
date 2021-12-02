from django.urls import path
from core.views import *

app_name = 'core'

urlpatterns = [
    path('SendProfiles/<str:id>', SendingProfiles.as_view(), name='SendingProfiles'),
    # path('SendProfile/', SendingProfiles.as_view(), name='SendingProfiles'),
    path('Reset/', Reset.as_view(), name='Reset'),
    path('Templates/', Templates.as_view(), name='Templates'),
    path('Templates/<int:id>', Templates.as_view(), name='Template'),
    path('Pages/<int:id>', Pages.as_view(), name='Pages'),
    path('Pages/', Pages.as_view(), name='Pages'),
    path('Groups/<int:id>', Groups.as_view(), name='Groups'),
    path('Groups/', Groups.as_view(), name='Groups'),
    path('Campaigns/<int:id>', Campaigns.as_view(), name='Campaigns'),
    path('Campaigns/', Campaigns.as_view(), name='Campaigns'),
    path('Users/<int:id>', Users.as_view(), name='Users'),
    path('Users/', Users.as_view(), name='Users'),
]