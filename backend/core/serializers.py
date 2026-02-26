from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Table, Quiz, Reservation, EmailLog, ActivityLog

User = get_user_model()


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Reservation
        fields = "__all__"
        read_only_fields = ("status", "created_at")
        validators = []  

    def validate(self, data):
        """
        Validacija koja radi i za POST i za PATCH:
        - party_size <= capacity
        - (quiz, table) mora biti jedinstveno za aktivne rezervacije
        """

        
        table = data.get("table") or getattr(self.instance, "table", None)
        quiz = data.get("quiz") or getattr(self.instance, "quiz", None)
        party_size = data.get("party_size") or getattr(self.instance, "party_size", None)

      
        status_value = getattr(self.instance, "status", None)
        if "status" in data:
            status_value = data.get("status")

        
        if table is not None and party_size is not None:
            if party_size > table.capacity:
                raise serializers.ValidationError(
                    {"party_size": "Broj clanova prelazi dozvoljen broj ljudi za stolom"}
                )

        
        ACTIVE_VALUE = "aktivna"

        if quiz is not None and table is not None and status_value == ACTIVE_VALUE:
            qs = Reservation.objects.filter(
                quiz=quiz,
                table=table,
                status=ACTIVE_VALUE,
            )
            if self.instance:
                qs = qs.exclude(pk=self.instance.pk)

            if qs.exists():
                raise serializers.ValidationError(
                    {"table": "Ovaj sto je vec rezervisan za izabrani kviz."}
                )

        return data


class EmailLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailLog
        fields = "__all__"
        read_only_fields = ("created_at",)


class ActivityLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityLog
        fields = "__all__"
        read_only_fields = ("created_at",)
