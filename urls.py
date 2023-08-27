from django.contrib import admin
from django.urls import path
from form import views

urlpatterns = [
    # path('formHome',views.formHome,name='formHome'),
    path('formInput',views.formInput,name='formInput'),
    path('addData', views.addData, name='addData'),
    path('displayData', views.displayData, name='displayData'),
    path('pdf_view/<name>', views.ViewPDF.as_view(), name="pdf_view"),
    path('pdf_download/<name>', views.DownloadPDF.as_view(), name="pdf_download"),
]