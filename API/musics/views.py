from django.shortcuts import render, get_object_or_404
from .models import *
from .serializers import MusicSerializer, MusicDetailSerializer, ArtistSerializer, ArtistDetailSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# view 함수 위에, 받아들일 HTTP 메소드를 데코레이터를 통해 명시해야 한다.
@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()

    #불러온 쿼리셋을 serilizer에게 넘겨준다.
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def music_detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    serializer = MusicDetailSerializer(music) #하나밖에 안보내니까, many=True 불필요
    return Response(serializer.data)


@api_view(['GET'])
def artist_list(request):
    artists = Artist.objects.all()
    serializer = ArtistDetailSerializer(artists, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def artist_detail(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = ArtistDetailSerializer(artist)
    return Response(serializer.data)


@api_view(['POST'])
def comments_create(request, music_pk):
    # form = CommentForm(request.POST) 와 유사하게
    serializer = CommentSerializer(data=request.data)
    # if form.is_valid() 와 유사하게
    if serializer.is_valid(raise_exception=True):
        serializer.save(music_id=music_pk)

    return Response(serializer.data)