from rest_framework import viewsets

from core.models import Review
from api.serializers.review_serializer import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer