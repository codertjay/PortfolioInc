from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import get_template
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from rest_framework.views import APIView
from .serializers import UserSerializer, ChangePasswordSerializer

from .forms import ContactUserForm
from .models import User, ContactUser


class UserUpdateAPIView(UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    queryset = User.objects.all()

    def get_serializer_context(self):
        context = super(UserUpdateAPIView, self).get_serializer_context()
        context.update({"request": self.request})
        return context


class ChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        old_password = serializer.data.get('old_password')
        new_password = serializer.data.get('new_password')
        user = request.user
        if user:
            if old_password == new_password:
                return Response({'message': 'Your new password cannot be the same as the old password'}, status=400)
            if user.check_password(old_password):
                user.set_password(new_password)
                user.save()
                return Response({'message': ' You have successfully changed your password'}, status=200)
            elif not user.check_password(old_password):
                return Response({'message': 'Your old password is incorrect'},
                                status=400)
        return Response({'message': 'There was an error performing your request '}, status=400)


class ContactUserView(APIView):

    def post(self, *args, **kwargs):
        form = ContactUserForm(self.request.data)
        to_email = User.objects.filter(email=form['to_email'].value()).first()
        host_url = self.request.data.get('url')
        print('these are the data', self.request.data)
        print('these are the data', host_url)
        print('the form error', form.errors)
        if not to_email:
            return Response(status=HTTP_400_BAD_REQUEST)
        if form.is_valid():
            print('the form was valid')
            template = get_template('EmailTemplates/contact.txt')
            contact = ContactUser(contact_name=form['contact_name'].value(),
                                  contact_email=form['contact_email'].value(),
                                  contact_subject=form['contact_subject'].value(),
                                  contact_message=form['contact_message'].value(),
                                  to_email=to_email)
            contact.save()
            context = {
                'contact_name': contact.contact_name,
                'contact_email': contact.contact_email,
                'contact_subject': contact.contact_subject,
                'contact_message': contact.contact_message,
                'to_email': contact.to_email
            }
            content = template.render(context)
            if context:
                send_mail(
                    contact.contact_subject,
                    content,
                    settings.EMAIL_HOST_USER,
                    [to_email],
                    fail_silently=True,
                )
                print('the message was sent')
                messages.success(self.request, 'Your messsage has  being sent')
                return Response(status=HTTP_201_CREATED)

        print('the message was not sent')
        messages.warning(self.request, 'There was an error sending your message')
        return Response(status=HTTP_400_BAD_REQUEST)
