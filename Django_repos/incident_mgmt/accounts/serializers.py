from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

from geopy.geocoders import Nominatim


def get_latitude_longitude(postal_code, country="IN"):
    geolocator = Nominatim(user_agent="incident_mgmt")
    try:
        location = geolocator.geocode(f"{postal_code}, {country}")
        if location:
            return location.latitude, location.longitude
    except Exception as e:
        print(f"Geocoding error: {e}")
    return None, None

def get_city_country(latitude, longitude):
    geolocator = Nominatim(user_agent="incident_mgmt")
    try:
        location = geolocator.reverse((latitude, longitude), language="en", exactly_one=True)
        if location:
            address = location.raw.get('address', {})
            city = address.get('city') or address.get('town') or address.get('village') or address.get('state_district')
            state = address.get('state')
            country = address.get('country')
            return city, state, country
    except Exception as e:
        print(f"Reverse geocoding error: {e}")
    return None, None, None


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'phone', 'address', 'pincode', 'city', 'country']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'phone', 'address', 'pincode']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        pincode = validated_data.get('pincode')

        latitude, longitude = get_latitude_longitude(pincode)
        city, state, country = get_city_country(latitude, longitude) if latitude and longitude else (None, None, None)

        # Add city and country to validated_data if found
        validated_data['city'] = city
        validated_data['country'] = country

        user = get_user_model().objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
    
class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

class ResetPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(write_only=True)
