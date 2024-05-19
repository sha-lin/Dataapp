from django.urls import path
from .views import (
    ReportListView,
    ReportDetailView,
    ReportCreateView,
    ReportUpdateView,
    ReportDeleteView,
    export_excel,
    generate_pdf
)

urlpatterns = [
    path('', ReportListView.as_view(), name='report-list'),
    path('report/<int:pk>/', ReportDetailView.as_view(), name='report-detail'),
    path('report/new/', ReportCreateView.as_view(), name='report-create'),
    path('report/<int:pk>/edit/', ReportUpdateView.as_view(), name='report-update'),
    path('report/<int:pk>/delete/', ReportDeleteView.as_view(), name='report-delete'),
    path('report/<int:pk>/pdf/', generate_pdf, name='report-pdf'),
    path('export/excel/', export_excel, name='export-excel'),
]
