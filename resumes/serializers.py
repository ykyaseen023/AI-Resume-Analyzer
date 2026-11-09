from rest_framework import serializers
from .models import Resume


class ResumeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resume

        fields = ['id', 'file', 'uploaded_at']

        read_only_fields = ['id', 'uploaded_at']

    def validate_file(self, value):

        allowed_extensions = ['pdf', 'docx']

        extension = value.name.split('.')[-1].lower()

        if extension not in allowed_extensions:

            raise serializers.ValidationError(
            "Only PDF and DOCX files are allowed."
        )

        if value.size > 5 * 1024 * 1024:

            raise serializers.ValidationError(
            "File size must not exceed 5 MB."
        )

        return value