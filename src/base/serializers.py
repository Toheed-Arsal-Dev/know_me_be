from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    def _get_authenticated_user_id(self):
        request = self.context.get("request")
        if request and request.user and request.user.is_authenticated:
            return request.user.id
        return None

    def create(self, validated_data):
        validated_data["created_by"] = self._get_authenticated_user_id()
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data["updated_by"] = self._get_authenticated_user_id()
        return super().update(instance, validated_data)

    class Meta:
        abstract = True
