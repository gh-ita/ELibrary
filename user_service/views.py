from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import RegisterSerializer
from .services import UserService

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        # Deserialize the request data using the RegisterSerializer
        serializer = RegisterSerializer(data=request.data)
        
        if serializer.is_valid():
            # Extract data from the serializer
            username = serializer.validated_data['username']
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            first_name = serializer.validated_data['first_name']
            last_name = serializer.validated_data['last_name']

            # Use the service layer to register the user
            try:
                user = UserService.register_user(
                    username=username,
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name
                )
                return Response({"message": "User created successfully!"}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
