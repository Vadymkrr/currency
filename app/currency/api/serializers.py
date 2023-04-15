from rest_framework import serializers

from currency.models import Source, ContactUs
from currency.tasks import send_mail


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = (
            'id',
            'name',
            'country'
        )


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'

    def create(self, validated_data):
        new_object = ContactUs.objects.create(
            email_from=validated_data['email_from'],
            subject=validated_data['subject'],
            message=validated_data['message']
        )

        subject = validated_data['subject']
        message = validated_data['message']
        send_mail(subject, message)

        return new_object
