from rest_framework import serializers
from PVLV_chatwars.models import (
    Game,
    Factory,
)
from PVLV_games.api.serializers import GamePassSerializer


class FactorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Factory
        exclude = ['id']


class BitsSerializer(serializers.ModelSerializer):

    bits = serializers.IntegerField(source='_bits', read_only=True)
    last_farm = serializers.DateTimeField(source='bits_last_farm', read_only=True)
    spent = serializers.IntegerField(source='bits_spent', read_only=True)
    earned = serializers.IntegerField(source='bits_earned', read_only=True)
    given_away = serializers.IntegerField(source='bits_given_away', read_only=True)

    class Meta:
        model = Game
        fields = ['bits', 'last_farm', 'spent', 'earned', 'given_away']


class GamesSerializer(serializers.ModelSerializer):

    account = BitsSerializer(source='*', read_only=True)
    plants = FactorySerializer(read_only=True)
    mines = FactorySerializer(read_only=True)

    class Meta:
        model = Game
        fields = [
            'game_pass',
            'user',
            'account',
            'created_at',
            'xp',
            'level',
            'plants',
            'mines',
        ]
        read_only_fields = [
            'created_at',
            'xp',
            'level',
        ]


class FullGamesSerializer(GamesSerializer):

    game_pass = GamePassSerializer(read_only=True)
    plants = FactorySerializer(required=False, read_only=False)
    mines = FactorySerializer(required=False, read_only=False)

    class Meta(GamesSerializer.Meta):
        read_only_fields = GamesSerializer.Meta.read_only_fields + [
            'game_pass',
            'user',
        ]

    def update(self, instance, validated_data):
        # loop to the data a update or create Factory objects
        for role in ['plants', 'mines']:

            try:
                data = validated_data.pop(role)
                if not data:  # there is the role key but is equal to null, skip
                    continue
            except KeyError:  # there isn't the role key in the validated_data
                continue

            # get the item from the instance
            factory = getattr(instance, role)

            if factory:
                serializer = FactorySerializer(factory, data=data, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
            else:
                factory = Factory.objects.create(**data)
                setattr(instance, role, factory)

        instance.save()
        return instance
