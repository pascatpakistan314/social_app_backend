from rest_framework import viewsets
from .models import Business
from .serializers import BusinessSerializer

class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

@api_view(['POST'])
def generate_post(request):
    try:
        # Check if 'business' is present in the request data
        if 'business' not in request.data:
            raise ValidationError("The 'business' object is missing from the request data.")

        data = request.data['business']

        # Check if necessary keys are in the 'business' data
        required_keys = ['city', 'services', 'name']
        for key in required_keys:
            if key not in data:
                raise ValidationError(f"'{key}' is missing in 'business' data.")
            # Also, check if the value for the key is not empty if it's critical
            if not data[key] and key != 'services': # services can be an empty array
                raise ValidationError(f"'{key}' in 'business' data cannot be empty.")
            if key == 'services' and not isinstance(data[key], list):
                raise ValidationError(f"'{key}' in 'business' data must be a list.")


        city = data['city']
        # Ensure services is a list and has at least one element for use
        service = data['services'][0] if data['services'] else 'general services' # Fallback for empty services list
        name = data['name']

        # Create post ideas
        post1 = f"Just finished a {service} job in {city}! Call {name} today to schedule your next service."
        post2 = f"{name} proudly offers expert {service} in {city}. Fast, professional, and local!"
        post3 = f"Looking for {service} in {city}? {name} is your go-to provider. Call us now!"

        return Response({"posts": [post1, post2, post3]})

    except KeyError as e:
        # This will catch if request.data['business'] doesn't exist, though the
        # initial check should prevent most of these.
        return Response({"error": f"Missing expected data field: {str(e)}"}, status=400)

    except ValidationError as e:
        # Handle custom validation errors from our checks
        return Response({"error": str(e)}, status=400)

    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}") # Log the error for debugging
        return Response({"error": f"An internal server error occurred. Please try again later."}, status=500)