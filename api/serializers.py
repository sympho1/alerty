from rest_framework import serializers
from api.models import Abus, Alert, Alerter, Author, Victim


class AlerterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alerter
        fields = ("name", "phone", "residence")


class AlertSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alert
        fields = (
            "created_at",
        )


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ("name", "author_residence")


class VictimSerializer(serializers.ModelSerializer):

    class Meta:
        model = Victim
        fields = ("name", "victim_residence" )


class AbusSerializer(serializers.ModelSerializer):
    # alert_abuse = AlertSerializer(many=True)
    victim_abuse = VictimSerializer(many=True)
    author_abuse = AuthorSerializer(many=True)
    alerter_abuse = AlerterSerializer(many=True)

    class Meta:
        model = Abus
        fields = (
            "description", "localisation", "alerted_at", "photo",
            "victim_abuse", "author_abuse", "alerter_abuse",
        )
        
    def create(self, validated_data):
        # alert_data = validated_data.pop("alert_abuse")
        victim_data = validated_data.pop("victim_abuse")
        author_data = validated_data.pop("author_abuse")
        alerter_data = validated_data.pop("alerter_abuse")
        
        abuse = Abus.objects.create(**validated_data)

        # for alert in alert_data:
        #     Alert.objects.create(abuse=abuse, **alert)

        for victim in victim_data:
            Victim.objects.create(abuse=abuse, **victim)
            
        for author in author_data:
            Author.objects.create(abuse=abuse, **author)
            
        for alerter in alerter_data:
            Alerter.objects.create(abuse=abuse, **alerter)

        return abuse
