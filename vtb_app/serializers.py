from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *
from django.utils import timezone

genders = [('male', 'male'), ('female', 'female'), ('unknown', 'unknown')]


class TestSerializer(serializers.Serializer):
    text = serializers.CharField()


class CarRecognizeSerializer(serializers.Serializer):
    photo = serializers.ImageField()


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
