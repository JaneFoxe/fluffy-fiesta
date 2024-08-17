from rest_framework import serializers
from network.models import Network, Contact, Product


class NetworkSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Network
    Атрибуты:
        Meta:
            model (Network): Модель, с которой работает сериализатор.
            fields (str): Поля модели, которые будут включены в сериализацию. В данном случае используются все поля.
            read_only_fields (list): Поля, доступные только для чтения. Поле 'arrears' доступно только для чтения.

    """

    class Meta:
        model = Network
        fields = "__all__"
        read_only_fields = ["arrears"]


class ContactSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Contact.
         Атрибуты:
        Meta:
            model (Contact): Модель, с которой работает сериализатор.
            fields (str): Поля модели, которые будут включены в сериализацию. В данном случае используются все поля.
    """

    class Meta:
        model = Contact
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Product.

        Атрибуты:
        Meta:
            model (Product): Модель, с которой работает сериализатор.
            fields (str): Поля модели, которые будут включены в сериализацию. В данном случае используются все поля.
    """

    class Meta:
        model = Product
        fields = "__all__"
