from rest_framework import generics, viewsets
from rest_framework.response import Response
from .serializers import *
from .models import *


class EmployeeListView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def list(self, request, *args, **kwargs):
        emp = Employee.objects.all()
        print(emp)
        return Response('employee data display')


# class EmployeeGetSalary(generics.ListAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
#     def list(self, request, *args, **kwargs):
#         # import pdb
#         # pdb.set_trace()
#         emp = self.get_queryset()
#         d = []
#         for data in emp:
#             if data.manager and data.salary > data.manager.salary: d.append(data)
#             print(d)
#         serializer = EmployeeSerializer(d, many=True).data
#         return Response(serializer)


class EmployeeView(viewsets.ViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def list(self, request, *args, **kwargs):
        queryset = Employee.objects.all()

        d = []
        for data in queryset:
            if data.manager and data.salary > data.manager.salary: d.append(data)
            # print(d)
        serializer = EmployeeSerializer(d, many=True).data
        return Response(serializer)

