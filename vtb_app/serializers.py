from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *
from django.utils import timezone

genders = [('male', 'male'), ('female', 'female'), ('unknown', 'unknown')]


class TestSerializer(serializers.Serializer):
    text = serializers.CharField()


class CarRecognizeSerializer(serializers.Serializer):
    photo = serializers.CharField()


class PersonSerializer(serializers.Serializer):
    birth_date_time = serializers.CharField()
    birth_place = serializers.CharField()
    family_name = serializers.CharField()
    first_name = serializers.CharField()
    gender = serializers.ChoiceField(genders)
    middle_name = serializers.CharField()
    nationality_country_code = serializers.CharField()
    #       "birth_date_time": "1981-11-01",
    #       "birth_place": "г. Воронеж",
    #       "family_name": "Иванов",
    #       "first_name": "Иван",
    #       "gender": "unknown",
    #       "middle_name": "Иванович",
    #       "nationality_country_code": "RU"


class CustomerPartySerializer(serializers.Serializer):
    email = serializers.CharField()
    income_amount = serializers.IntegerField()
    person = PersonSerializer()
    phone = serializers.CharField()


# {
#   "datetime": "2020-10-10T08:15:47Z",
#   "interest_rate": 15.7,
#   "requested_amount": 300000,
#   "requested_term": 36,
#   "trade_mark": "Nissan",
#   "vehicle_cost": 600000
# }
#   "comment": "Комментарий",
#   "customer_party": {
#     "email": "apetrovich@example.com",
#     "income_amount": 140000,
#     "person": {
#       "birth_date_time": "1981-11-01",
#       "birth_place": "г. Воронеж",
#       "family_name": "Иванов",
#       "first_name": "Иван",
#       "gender": "unknown",
#       "middle_name": "Иванович",
#       "nationality_country_code": "RU"
#     },
#     "phone": "+99999999999"
#   },
class CarLoanSerializer(serializers.Serializer):
    comment = serializers.CharField()
    customer_party = CustomerPartySerializer()
    datetime = serializers.CharField()
    interest_rate = serializers.FloatField()
    requested_amount = serializers.IntegerField()
    requested_term = serializers.IntegerField()
    trade_mark = serializers.CharField()
    vehicle_cost = serializers.IntegerField()


class SearchHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchHistory
        exclude = ['user']


class LoanHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanHistory
        exclude = ['user']


class ExtraUserDataSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(allow_blank=True, allow_null=True, required=False)
    income_amount = serializers.IntegerField(allow_null=True, required=False)
    birth_date_time = serializers.CharField(allow_blank=True, required=False)
    birth_place = serializers.CharField(allow_blank=True, required=False)
    family_name = serializers.CharField(allow_blank=True, required=False)
    first_name = serializers.CharField(allow_blank=True, required=False)
    gender = serializers.ChoiceField(choices=genders, allow_blank=True, required=False)
    middle_name = serializers.CharField(allow_blank=True, required=False)
    nationality_country_code = serializers.CharField(allow_blank=True, required=False)
    phone = serializers.CharField(allow_blank=True, required=False)

    class Meta:
        model = ExtraUserData
        exclude = ['user']


class SpecsSerializer(serializers.Serializer):
    speedLimit: serializers.CharField()
    acceleration: serializers.CharField()
    fuelConsumtion: serializers.CharField()
    horsePowers: serializers.CharField()


class CarInfoSerializer(serializers.Serializer):
    make = serializers.CharField()
    model = serializers.CharField()
    types = serializers.ListField(child = serializers.CharField())
    imageUrl = serializers.CharField()
    minPrice = serializers.IntegerField()
    maxPrice = serializers.IntegerField()
    specs = SpecsSerializer()