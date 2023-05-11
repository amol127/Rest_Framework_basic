from django.shortcuts import render
from rest_framework import viewsets
from app.models import Company ,Employee
from app.serializers import CompanySerializer , EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company .objects.all()
    serializer_class = CompanySerializer


    # Create a Custom Url to filter employee to perculer company {company_id}
    @action(detail=True,methods=['get'])
    def employee(self, request ,pk=None):
        try:
            company = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=company)
            emps_serializer = EmployeeSerializer(emps,many=True,context={'request':request})
            return Response(emps_serializer.data)
        except Exception as e:
            return Response({
                'message':'Company might Exists !! Error'
            })

    

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee .objects.all()
    serializer_class = EmployeeSerializer