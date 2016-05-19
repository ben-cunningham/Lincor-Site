from rest_framework import generics
from rest_framework.views import APIView
from models import (
    Job,
    CheckIn,
    ResultsCalculator,
    Quote
)
from serializers import (
    JobListSerializer,
    JobCreateSerializer,
    CheckInSerializer,
    JobUpdateSerializer,
    QuoteListSerializer,
    QuoteDetailSerializer
)
from employees.models import (
    Employee,
    Estimator,
    Foreman
)
from team.models import Team

from rest_framework.response import Response
from rest_framework import status

class JobList(generics.ListCreateAPIView):
    def get_queryset(self):
        employee = Employee.objects.get(user=self.request.user)
        team = employee.team
        try:
            if employee.is_admin:
                return Job.objects.filter(team=team)
        except:
            return None

        # TODO: Downcast so I don't need to requery
        foreman = Foreman.objects.get(user=self.request.user)
        return Job.objects.filter(team=team).filter(foreman=foreman)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return JobListSerializer
        else:
            return JobCreateSerializer

class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return JobUpdateSerializer
        else:
            return JobListSerializer

class QuoteList(generics.ListCreateAPIView):
    def get_queryset(self):
        employee = Employee.objects.get(user=self.request.user)
        team = Team.objects.get(pk=employee.team.pk)
        try:
            if not employee.is_admin:
                return Response(status=status.HTTP_403_FORBIDDEN)
            return Quote.objects.filter(team=team)
        except:
            return None

    serializer_class = QuoteListSerializer

class QuoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteDetailSerializer


class CheckIn(APIView):
    def post(self, request, format=None):
        check_in = CheckInSerializer(data=request.data)
        if check_in.is_valid():
            check_in.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class results_calculator(APIView):
    def get(self, request, *args, **kw):
        results_calculator = ResultsCalculator()
        result = results_calculator.jobTotals()
        response = Response(result, status=status.HTTP_200_OK)
        return response
