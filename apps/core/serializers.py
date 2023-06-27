from rest_framework import serializers


class EmployesRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    image_url = serializers.CharField(required=False)

    def to_representation(self, instance):
        # В случае отсутствия какого-либо из полей присылать пустую строку в этом месте.
        my_fields = {'id', 'name', 'last_name', 'phone', 'image_url'}
        data = super().to_representation(instance)
        for field in my_fields:
            if not data.get(field):
                data[field] = ""
        return data
