from django.contrib import auth
from rest_framework import generics, permissions, serializers
from rest_framework.response import Response
from knox.models import AuthToken
from .serializer import UserSerializer, RegisterSerializer, LoginSerializer,Post
from rest_framework import status

class SignUpAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = AuthToken.objects.create(user)
        return Response({
            "users": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token[1]
        })


class SignInAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class MainUser(generics.RetrieveAPIView):
  permission_classes = [
      permissions.IsAuthenticated
  ]
  serializer_class = UserSerializer

  def get_object(self):
    return self.request.user



class PostViews(APIView):
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data["tweet_post"])
            auth = tweepy.OAuthHandler(
            settings.API_KEY,settings.API_SECRET
            )
            auth.set_access_token(
            settings.ACCESS_TOKEN,
            settings.ACCESS_TOKEN_SECRET
            )
            api = tweepy.API(auth)
            media=api.media_upload(serializer.data["upload"])
            tweet=serializer.data["tweet_post"]
            post_result=api.update_status(status=tweet,media_ids=[media.media_id])
            data2 =api.update_status(serializer.data["tweet_post"] )
            print(data2)

            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)   
          

# Create your views here.
class TwitterKeyViews(APIView):
    def post(self, request):
        serializer = TwitterKeySerializer(data=request.data)
        if serializer.is_valid():
            print(request.data)
         
            #print(request.data)
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
               return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)   

            