from rest_framework import serializers
from network.models import Network, Contact, Product


class NetworkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Network
        fields = "__all__"
        read_only_fields = ["arrears"]


class ContactkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class ProductkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
