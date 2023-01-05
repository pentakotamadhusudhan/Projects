import base64

from rest_framework import serializers
from .models import barmodel,barreaddb
from barcode_generator.bar import logic

class barserializer(serializers.ModelSerializer):
    class Meta:
        model = barmodel
        fields = 'product_name','product_code' ,'pack_code'

    def create(self, validated_data):
        product_name = validated_data['product_name']
        product_code = validated_data['product_code']
        pack_code = validated_data['pack_code']
        code_genaration = product_code+" "+pack_code
        combined = logic(code_genaration,product_name)
        with open(combined,'rb') as img:
            encoded = base64.b64encode(img.read())
            print(encoded)
            user = barmodel.objects.create(product_name=product_name, product_code=product_code, pack_code=pack_code,bar_code=encoded)
            user.save()
            return user





class retrieveserializer(serializers.ModelSerializer):
    class Meta:
        model = barreaddb
        fields = '__all__'

