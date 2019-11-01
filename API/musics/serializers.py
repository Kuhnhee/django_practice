from rest_framework import serializers
from .models import Music, Artist, Comment

# forms.ModelForm과 비슷한 느낌
class MusicSerializer(serializers.ModelSerializer):
    # MusicSerializer가 어떻게 생겼는지를 정의할 것
    class Meta:
        model = Music #어떤 모델을 직렬화 하려고 하는가?
        fields = ('id', 'title', 'artist_id',)

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name',)

class ArtistDetailSerializer(serializers.ModelSerializer):
    #music_set: 이 아티스트가 가지고 있는 music_set을 가지고 있는 변수
    music_set = MusicSerializer(many=True)
    class Meta(ArtistSerializer.Meta):
        #앞서 선언한 serializer를 상속받음. model 추가적으로 지정해줄 필요 없음
        fields = ArtistSerializer.Meta.fields + ('music_set',)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'music_id',)
        # fields = '__all__'

class MusicDetailSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True)
    class Meta(MusicSerializer.Meta):
        fields = MusicSerializer.Meta.fields + ('comment_set',)