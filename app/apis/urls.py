from django.urls import path, include


urlpatterns = [
    path('cases/', include('app.apis.cases.urls'))

]

