from rest_framework import serializers
from .models import Actor, Movie, Review


class ActorListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Actor
        fields = '__all__'


class MovieTitle(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('title',)

class ActorSerializer(serializers.ModelSerializer):
    movies = MovieTitle(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'overview',)


class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title', 'content',)


class MovieActor(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('name',)


class MovieSerializer(serializers.ModelSerializer):
    actors = MovieActor(many=True, read_only=True)
    review_set = ReviewListSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieTitle(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'