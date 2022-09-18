from typing import Union
from rest_framework import serializers
from .models import Category


class TrackSerializer(serializers.Serializer):
    role = serializers.CharField()
    instruments = serializers.ListField(child=serializers.CharField(), allow_empty=False)
    is_primary = serializers.BooleanField()

    def validate_role(self, role: str) -> str:
        if role not in Category().role:
            raise serializers.ValidationError("{} is not a valid genre option".format(role))
        return role
    
    def validate_instruments(self, instruments: list[str]) -> list[str]:
        for instrument in instruments:
            if instrument not in Category().instrument:
                raise serializers.ValidationError("{} is not a valid genre option".format(instruments))
        return instruments


class SampleRequestSerializer(serializers.Serializer):
    genre = serializers.CharField()
    bpm = serializers.ListField(child=serializers.IntegerField(min_value=30, max_value=200), min_length=1, max_length=2)
    keys = serializers.ListField(child=serializers.CharField(), allow_empty=False)
    time_signatures = serializers.ListField(child=serializers.CharField(), allow_empty=False)
    tracks = TrackSerializer(many=True, allow_empty=False)

    def validate_genre(self, genre: str) -> str:
        if genre not in Category().genre:
            raise serializers.ValidationError("{} is not a valid genre option".format(genre))
        return genre

    def validate_keys(self, keys: list[str]) -> list[str]:
        for key in keys:
            if key not in Category().key:
                raise serializers.ValidationError("{} is not a valid key option".format(key))
        return keys
    
    def validate_time_signatures(self, time_signatures: list[str]) -> list[str]:
        for time_signature in time_signatures:
            if time_signature not in Category().time_signature:
                raise serializers.ValidationError("{} is not a valid time signature option".format(time_signature))
        return time_signatures

    def validate_tracks(self, tracks: list[object]) -> list[object]:
        primary_count: int = 0
        for track in tracks:
            if track['is_primary'] == True:
                primary_count += 1
                if track['role'] == 'drums':
                    raise serializers.ValidationError("track with 'drums' as role can't be primary track")
        if primary_count > 1:
            raise serializers.ValidationError("primary track can't be more than one")
        elif primary_count == 0:
            raise serializers.ValidationError("there is no primary track")
        return tracks