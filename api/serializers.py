from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User

from .models import Item


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password',
                  # 'first_name', 'last_name', 'email'
                  ]

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        # email = validated_data['email']
        # first_name = validated_data['first_name']
        # last_name = validated_data['last_name']
        new_user = User(username=username,
                        # email= email, first_name = first_name, last_name = last_name
                        )
        new_user.set_password(password)
        new_user.save()
        return validated_data


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(allow_blank=True, read_only=True)

    def validate(self, data):
        my_username = data.get('username')
        my_password = data.get('password')

        try:
            user_obj = User.objects.get(username=my_username)

        except:
            raise serializers.ValidationError("This username does not exist")

        if not user_obj.check_password(my_password):
            raise serializers.ValidationError("Incorrect username/password")

#         except:
#         	pass

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user_obj)
        token = jwt_encode_handler(payload)

        data["token"] = token
        return data


class ItemDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = [
            'name',
            'image',
            'url',
            'id'
        ]


class ItemCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'


class ItemUpdateCheckerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)

    class Meta:
        model = Item
        fields = '__all__'


class ItemListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'
# List ser
# class ListSerializer(serializers.ModelSerializer):
    # author = UserSerializer()
#     class Meta:
#         model = ModelName
#         fields = ['field_1', 'field_2', 'field_3','author']

    # def get_written_by(self, obj):
    #     return "%s %s"%(obj.author.first_name, obj.author.last_name)

# class DetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ModelName
#         fields = ['field_1', 'field_2', 'field_3', 'field_4', 'field_5',]

# class CreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ModelName
#         fields = ['field_1', 'field_2', 'field_3', 'field_4',]
