from rest_framework.viewsets import ModelViewSet

from questions.models import Question
from questions.serializers import QuestionSerializer

class QuestionViewSet(ModelViewSet):
    """
    Question Modelviewset
    """

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer



"""
api/casas/ LIST GET
api/casas/ CREATE POST

api/casas/1/ GET
api/casas/1/ DELETE
api/casas/1/ EDIT PUT
api/casas/1/ EDIT Parcial PATCH
"""