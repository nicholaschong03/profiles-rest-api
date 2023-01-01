from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAppView(APIView):
    """Test API View"""
    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
            "Uses Http method as functions (get, post, patch, put, delete)",
            "Is similar to traditional django view",
            "Gives you the most control over your application logic",
            "Is mapped manually to URLs"
        ]

        return Response({"message":"Hello World!","an_apiview":an_apiview})