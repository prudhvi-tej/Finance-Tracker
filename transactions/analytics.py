from django.db.models import Sum
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .models import Transaction
from django.db.models.functions import TruncMonth
from rest_framework.permissions import IsAuthenticated
from .permissions import RolePermission
from django.http import HttpResponse
import csv 

@api_view(['GET'])
@permission_classes([IsAuthenticated, RolePermission])
def summary(request):
    total_income=Transaction.objects.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = Transaction.objects.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0

    return Response({
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": total_income - total_expense
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated, RolePermission])
def category_summary(request):
    data = Transaction.objects.values('category').annotate(total=Sum('amount'))
    return Response(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated, RolePermission])
def monthly_summary(request):
    data = Transaction.objects.annotate(month=TruncMonth('date')) \
        .values('month') \
        .annotate(total=Sum('amount')) \
        .order_by('month')

    return Response(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated, RolePermission])
def recent_transactions(request):
    data = Transaction.objects.order_by('-date')[:5]
    return Response([
        {
            "id": t.id,
            "amount": t.amount,
            "type": t.type,
            "category": t.category,
            "date": t.date
        } for t in data
    ])


@api_view(['GET'])
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment;filename="transactions.csv"'
    writer = csv.writer(response)
    writer.writerow(['Amount','Type','Category'])
    for t in Transaction.objects.all():
        writer.writerow([t.amount,t.type,t.category])
    return response

