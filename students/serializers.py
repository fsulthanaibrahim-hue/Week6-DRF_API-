from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'

    def validate_course(self, value):
        allowed_course = ['Python', 'Django', 'React', 'React', 'JavaScript']
        if value not in allowed_course:
            raise serializers.ValidationError(f"Course must be one of {allowed_course}")
        return value


class StudentCustomSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    course = serializers.CharField(max_length=100)
    created_at = serializers.DateTimeField(read_only=True)

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty or spaces")
        return value
    
    def validate_email(self, value):
        qs = Student.objects.filter(email=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("This email is already registered")
        return value
    
    def validate_course(self, value):
        allowed_courses = ['Python', 'Django', 'React', 'JavaScript']
        if value not in allowed_courses:
            raise serializers.ValidationError(f"Course must be one of {allowed_courses}")
        return value
    
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.course = validated_data.get('course', instance.course)
        instance.save()
        return instance
