from rest_framework import generics, permissions
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer,LoginSerializer
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
# Register API
class RegisterAPIGET(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'formulario.html'
    
    def get(self, request, format=None):

        serializer = RegisterSerializer()
        return Response({'serializer': serializer})
   
# Register API
class RegisterAPIPOST(generics.GenericAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'mensaje.html'
    serializer_class = RegisterSerializer
    def post(self, request, *args, **kwargs):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
            })
    
        

class LoginAPIGET(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'login.html'
    
    def get(self, request, format=None):

        serializer = LoginSerializer()
        return Response({'serializer': serializer})
class LoginAPIPOST(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'mensaje.html'
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPIPOST, self).post(request, format=None)       