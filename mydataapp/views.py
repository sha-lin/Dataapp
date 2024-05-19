from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Report
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .models import Report
import pandas as pd

class ReportListView(LoginRequiredMixin, ListView):
    model = Report
    template_name = 'report_list.html'

class ReportDetailView(LoginRequiredMixin, DetailView):
    model = Report
    template_name = 'report_detail.html'

class ReportCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Report
    fields = ['title', 'content']
    template_name = 'report_form.html'

    def test_func(self):
        return self.request.user.groups.filter(name='Admin').exists()

class ReportUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Report
    fields = ['title', 'content']
    template_name = 'report_form.html'

    def test_func(self):
        return self.request.user.groups.filter(name='Admin').exists()

class ReportDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Report
    template_name = 'report_confirm_delete.html'
    success_url = reverse_lazy('report-list')

    def test_func(self):
        return self.request.user.groups.filter(name='Admin').exists()

def generate_pdf(request, pk):
    report = get_object_or_404(Report, pk=pk)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{report.title}.pdf"'
    
    p = canvas.Canvas(response)
    p.drawString(100, 750, report.title)
    p.drawString(100, 730, report.content)
    p.showPage()
    p.save()
    
    return response

def export_excel(request):
    reports = Report.objects.all()
    data = {
        'Title': [report.title for report in reports],
        'Content': [report.content for report in reports],
        'Created At': [report.created_at for report in reports],
        'Updated At': [report.updated_at for report in reports],
    }
    df = pd.DataFrame(data)
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="reports.xlsx"'
    df.to_excel(response, index=False)

    return response