import datetime
from django.http import JsonResponse
from django.shortcuts import render
 
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import announcementsSerializer, assignmentsSerializer, classtestsSerializer, helpwewantSerializer


from .models import announcements, class_tests, assignments, helpwewant



####################### OTHERS #######################################################################################


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : '/announcement-list/',
        'Detail View': '/announcement-detail/<str:pk>/',
        'Create' : '/announcement-create/',
        'Delete' : '/announcement-delete/',
    }
    return Response(api_urls)

@api_view(['GET'])
def counterAPI(request):
    curr_week = 0
    thisweeks_assignments = []
    thisweeks_cts = []

    my_date = datetime.date.today()
    year, week_num, day_of_week = my_date.isocalendar()

    curr_week = week_num - 3 

    asses = assignments.objects.all()
    
    for i in asses:
        i_date = i.due
        i_year, i_week_num, i_day_of_week = i_date.isocalendar()

        if i_week_num == week_num:
            thisweeks_assignments.append(i)

    thisweeks_assignments_count = len(thisweeks_assignments)
    

    cts = class_tests.objects.all()
    
    for i in cts:
        i_date = i.occurring
        i_year, i_week_num, i_day_of_week = i_date.isocalendar()

        if i_week_num == week_num:
            thisweeks_cts.append(i)

    thisweeks_cts_count = len(thisweeks_cts)

    total_assignments_count = len(asses)
    total_cts_count = len(cts)

    counter = {
        'current_week_no' : curr_week,
        'this_weeks_assignments_count' : thisweeks_assignments_count,
        'this_weeks_cts_count' : thisweeks_cts_count,
        'total_assignments_count' : total_assignments_count,
        'total_cts_count' : total_cts_count,
    }

    return Response(counter)



###### LIST ##############

@api_view(['GET'])
def announcementList(request):

    announces = announcements.objects.all()
    serializer = announcementsSerializer(announces, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def assignmentList(request):

    assignment = assignments.objects.all()
    serializer = assignmentsSerializer(assignment, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def classtestsList(request):

    cts = class_tests.objects.all()
    serializer = classtestsSerializer(cts, many = True)
    return Response(serializer.data)


@api_view(['GET'])
def helpList(request):

    helps = helpwewant.objects.all()
    serializer =  helpwewantSerializer(helps, many = True)
    return Response(serializer.data)

# POST # 

###### CREATE ########################################################################################################################################
@api_view(['POST'])
def announcementCreate(request):

    serializer = announcementsSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def assignmentCreate(request):

    serializer = assignmentsSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def classtestCreate(request):

    serializer = classtestsSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def helpCreate(request):

    serializer = helpwewantSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

######################################################################UPDATE POST#########################################################################

@api_view(['POST'])
def announcementUpdate(request, pk):
    announce = announcements.objects.get(id = pk) 
    serializer = announcementsSerializer(instance = announce, data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def classtestUpdate(request, pk):
    announce = class_tests.objects.get(id = pk) 
    serializer = classtestsSerializer(instance = announce, data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def assignmentUpdate(request, pk):
    announce = assignments.objects.get(id = pk) 
    serializer = assignmentsSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def helpUpdate(request, pk):
    announce = helpwewant.objects.get(id = pk) 
    serializer = helpwewantSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

#########################################################################Delete Post###################################################################

@api_view(['DELETE'])
def announcementDelete(request, pk):
    announce = announcements.objects.get(id = pk) 
    announce.delete()
    
    return Response("That things you want to delete has been deleted Bujhsen???! !")


@api_view(['DELETE'])
def classtestDelete(request, pk):
    announce = class_tests.objects.get(id = pk) 
    announce.delete()
    
    return Response("That things you want to delete has been deleted Bujhsen???! !")

@api_view(['DELETE'])
def assignmentDelete(request, pk):
    announce = assignments.objects.get(id = pk) 
    announce.delete()
    
    return Response("That things you want to delete has been deleted Bujhsen???! !")


@api_view(['DELETE'])
def helpDelete(request, pk):
    announce = helpwewant.objects.get(id = pk) 
    announce.delete()
    
    return Response("That things you want to delete has been deleted Bujhsen???! !")

############################
# @api_view(['GET'])
# def DemoList(request):
#     demos = Demo.objects.all()
#     serializer = DemoSerializer(demos, many = True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def DemoCreate(request):

#     serializer = DemoSerializer(data = request.data)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)

# @api_view(['POST'])
# def DemoUpdate(request, pk):
#     announce = Demo.objects.get(id = pk) 
#     serializer = classtestsSerializer(instance = announce, data = request.data)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)

# @api_view(['DELETE'])
# def DemoDelete(request, pk):
#     announce = Demo.objects.get(id = pk) 
#     announce.delete()
    
#     return Response("That things you want to delete has been deleted Bujhsen???! !")