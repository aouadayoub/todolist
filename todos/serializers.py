from .models import Todo
from rest_framework import serializers

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at']

    def validate_title(self, value):
        """Validate title length and content."""
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty.")
        if len(value) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long.")
        return value
    
    def validate_description(self, value):
        """Validate description length."""
        if value and len(value) > 500:
            raise serializers.ValidationError("Description cannot exceed 500 characters.")
        return value
    
    
    
    def validate_is_completed(self, value):
        """Prevent setting a task as completed when it's first created."""
        if self.instance is None and value is True:
            raise serializers.ValidationError("You cannot mark a new task as completed.")
        return value
    
    
    def validate(self, attrs):
        """Global validation for multiple fields."""
        user = attrs.get('user')
        title = attrs.get('title')

        if user and Todo.objects.filter(user=user, title=title).exists():
            raise serializers.ValidationError("You already have a to-do with this title.")

        return attrs