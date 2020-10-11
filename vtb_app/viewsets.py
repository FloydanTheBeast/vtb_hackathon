from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins
from .vtb_api import *
import json


class TestViewSet(viewsets.ViewSet):
    """
    Example empty viewset demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the `format=None` keyword argument for each action.
    """

    def list(self, request):
        pass

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


class SearchHistoryViewSet(mixins.ListModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SearchHistorySerializer
    queryset = SearchHistory.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(user=self.request.user)
        return query_set

    @action(detail=False, methods=['delete'])
    def delete_all(self, request):
        SearchHistory.objects.all().delete()
        return Response("Successfully deleted search history")


class LoanHistoryViewSet(mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LoanHistorySerializer
    queryset = LoanHistory.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(user=self.request.user)
        return query_set

    @action(detail=False, methods=['delete'])
    def delete_all(self, request):
        LoanHistory.objects.all().delete()
        return Response("Successfully deleted loan history")


class PaymentsGraphHistoryViewSet(mixins.ListModelMixin,
                                  mixins.RetrieveModelMixin,
                                  mixins.DestroyModelMixin,
                                  viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PaymentsGraphHistorySerializer
    queryset = PaymentsGraphHistory.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(user=self.request.user)
        return query_set

    @action(detail=False, methods=['delete'])
    def delete_all(self, request):
        PaymentsGraphHistory.objects.all().delete()
        return Response("Successfully deleted payments graph history")


class ExtraUserDataViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ExtraUserDataSerializer
    queryset = ExtraUserData.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(user=self.request.user)
        return query_set

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CarRecognizeViewSet(viewsets.ViewSet):
    serializer_class = CarRecognizeSerializer

    # def list(self, request):
    #     return Response('Car recognize Method')
    #     pass

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            photo = request.data.get('photo')
            response = car_recognize_method(photo)
            if request.auth:
                sh_model = SearchHistory(response=response, user=request.user)
                sh_model.save()
            return Response(response)
        return Response(serializer.errors)


class CarLoanViewSet(viewsets.ViewSet):
    serializer_class = CarLoanSerializer

    # def list(self, request):
    #     return Response('Car loan Method')
    #     pass

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            response = request_vtb_api(data, 'carloan')
            print(request.auth)
            if request.auth:
                lh_model = LoanHistory(response=response, user=request.user)
                lh_model.save()
            return Response(response)

        return Response(serializer.errors)


class MarketplaceViewSet(viewsets.ViewSet):
    serializer_class = QueryCarModelSerializer

    def create(self, request):
        query_serializer = self.serializer_class(data=request.data)
        if query_serializer.is_valid():
            query = query_serializer.validated_data.get('query')

            with open('marketplace.json', 'r', encoding='utf-8') as file:
                marketplace_data = json.load(file, )

                if query in marketplace_data:
                    serializer = CarInfoSerializer(data=marketplace_data[query])

                    if serializer.is_valid():
                        return Response(marketplace_data[query])

                    return Response(serializer.errors, status=400)

        return Response({"error": 'No cars have been found'}, status=400)


class PaymentsGraphViewSet(viewsets.ViewSet):
    serializer_class = PaymentsGraphSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            response = payments_graph_method(serializer.validated_data)

            # TODO: Check auth if needed
            print(request.user)
            if request.auth:
                pg_model = PaymentsGraphHistory(response=response, user=request.user)
                pg_model.save()
            return Response(response)

        return Response(serializer.errors)
