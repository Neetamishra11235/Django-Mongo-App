from rest_framework import serializers 
from jsonapi.models import Members
from jsonapi.models import Period_details

class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period_details
        fields = ('start_time', 'end_time')

class MemberSerializer(serializers.ModelSerializer):
    activity_periods = PeriodSerializer(many=True)
    print("######")
    print(activity_periods)
    class Meta:
        model = Members
        fields = ('id','real_name','tz','activity_periods')
    def create(self, validated_data):
        print(validated_data)
        print(type(validated_data))
        periods_data = validated_data.pop('activity_periods')
        print(periods_data)
        print(type(periods_data))
        member = Members.objects.create(**validated_data)
        print(member)
        for period in periods_data:
            #Period_details.objects.create(all_members=member, **period)
            member.activity_periods.create(**period)
        return member