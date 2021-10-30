from allauth.account.adapter import get_adapter
from django.contrib.auth.models import User
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class StringSerializer(serializers.StringRelatedField):

    def to_internal_value(self, data):
        return value


class UserTokenDetailSerializer(serializers.ModelSerializer):
    """This serializer is used only when users login or register to get information"""

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'kid_code',
            'phone_number',
            'verified',
            'last_login',
        ]
        extra_kwargs = {'password': {'write_only': True, 'min_length': 4}, 'otp': {'write_only': True}}


class TokenSerializer(serializers.ModelSerializer):
    """
    In here i am checking if the user email has been verified before
    sending him his details
    """
    user = SerializerMethodField(read_only=True)
    access = SerializerMethodField(read_only=True)
    refresh = SerializerMethodField(read_only=True)

    class Meta:
        model = Token
        fields = ('access', 'refresh', 'user',)

    def get_access(self, obj):
        if obj.user.verified:
            refresh = RefreshToken.for_user(obj.user)
            return str(refresh.access_token)
        return None

    def get_refresh(self, obj):
        if obj.user.verified:
            refresh = RefreshToken.for_user(obj.user)
            return str(refresh)
        return None

    # in here i am sending an otp the the mobile number of the customer
    # if he is not verified
    def get_user(self, obj):
        try:
            if obj.user.verified:
                return UserTokenDetailSerializer(obj.user, read_only=True).data
            else:
                # user_otp = UserOTP.objects.get(user__email=obj.user.email)
                # user_otp.send_otp()
                return "Please verify your mail An OTP has been sent to your mobile number and mail for verification."
        except Exception as a:
            print(a)
            return 'error'


class CustomRegisterSerializer(RegisterSerializer):
    """
    Custom registration for the user serializer
    this add extra fields to the django default user
    """
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    first_name = serializers.CharField(max_length=50, required=False)
    last_name = serializers.CharField(max_length=50, required=False)

    class Meta:
        model = User
        fields = ('first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2',)

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
        }

    def save(self, request):
        """
        Due to adding extra fields to the user model we created an adapter
        in the users app to save the  kid extra field
        """
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        return user


class UserSerializer(ModelSerializer):
    """
    This serializer is used only to get the detail of the user but not all details  used in blog also to get user that
    commented and posted
    """
    first_name = serializers.CharField(max_length=50, required=False, allow_null=True, allow_blank=True)
    last_name = serializers.CharField(max_length=50, required=False, allow_null=True, allow_blank=True)
    email = serializers.EmailField(required=False, allow_null=True, allow_blank=True)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
        ]

    def validate_email(self, obj):
        logged_in_user = self.context['request'].user
        user = User.objects.filter(email=obj).first()
        if user:
            if logged_in_user.email != user.email:
                raise serializers.ValidationError('Please use a valid email that has not been used before')
        return obj


class VerifyEmailSerializer(serializers.Serializer):
    otp = serializers.CharField(max_length=4)
    email = serializers.EmailField()


class ChangePasswordWithOTPSerializer(serializers.Serializer):
    otp = serializers.CharField(max_length=4)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100)


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=100)
    new_password = serializers.CharField(max_length=100)
