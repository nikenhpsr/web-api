from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Project, Article
from .serializers import ProjectSerializer, ArticleSerializer, UserSerializer
from drf_spectacular.utils import extend_schema
from drf_spectacular.types import OpenApiTypes

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

@extend_schema(
    request=UserSerializer,
    responses={201: UserSerializer, 400: OpenApiTypes.OBJECT},
)
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)