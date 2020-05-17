from django.urls import path
from django.conf.urls import url,include
from searchapp import views
urlpatterns = [
    path('',views.home),
    path('employee',views.employee),
    path('company',views.company),
    path('searchemp',views.searchemp),
    path('searchcom',views.searchcom),
    path('companydata',views.companydata),
    path('employeedata',views.employeedata),
    path('searchempdata',views.searchempdata),
    path('searchcomdata',views.searchcomdata),
    path('viewempdata',views.viewempdata),
    path('viewcomdata',views.viewcomdata),
    
]


