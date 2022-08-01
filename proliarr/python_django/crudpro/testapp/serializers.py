from rest_framework import serializers

from testapp.models import form

class formserializer(serializers.ModelSerializer):
    class Meta:
        model = form
        fields = "__all__"
