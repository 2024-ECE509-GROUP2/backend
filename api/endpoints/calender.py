from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from api.models import SchoolCalender



#######################################################
#
# Academic 
# 
# ../api/v1/calender/
#
#######################################################


# ../api/v1/calender/
@csrf_exempt
def all(request):
    
    if request.method == 'GET':
        
        # Get parameter from request
        programme = request.GET.get('programme', '')

        if programme:

            try:
                # If Programme is specfied, filter out the rest
                calender = SchoolCalender.objects.get(programme=programme)
            except SchoolCalender.DoesNotExist:
                return JsonResponse({'message': 'Programme Not Active'} ,status=404)
        
            return JsonResponse({'message': 'Specify Programme'}, status=400)
        
        programme = SchoolCalender.objects.all()
        
        serializer = SchoolCalender(programme, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    # since no other method supported, return error
    return JsonResponse({'message': 'No such method at endpoint'}, status=400)