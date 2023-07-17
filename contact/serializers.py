from django.http import HttpResponse
from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .models import Contact
from account.models import Account


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'author', 'name', 'phone_number', 'is_script', 'created_date']

    def validate(self, attrs):

        phone_number = attrs.get('phone_number')
        contacts_phone_number = Contact.objects.values_list('phone_number')
        all_numbers = Account.objects.values_list('phone')
        request = self.context['request']
        author = attrs.get('author')

        for contact_phone_number in contacts_phone_number:
            for contact_phone_number_isOne in contact_phone_number:
                if contact_phone_number_isOne == phone_number:
                    raise ValidationError({'message': 'this number has an account'})

        if author.phone == phone_number:
            return attrs
        else:
            raise ValidationError({'message': 'no account has been opened for the number'})

        # for account in all_numbers:
        #     for account_number in account:
        #         if account_number == phone_number:
        #             return attrs
        #         # return HttpResponse('no account has been opened for the number')
        #         # raise ValidationError({'message': 'no account has been opened for the number'})
        #         return Response({'detail': 'no account has been opened for the number'})

        # account_numbers = Contact.objects.values_list('phone_number')
        # instance = request.data.get('phone_number')
        # if not instance in all_numbers:
        #     return Response({'detail': 'no account has been opened for the number'})
        #
        # return attrs
