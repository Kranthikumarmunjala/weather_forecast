from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from datarepo.models import State,District

# Create your views here.


@api_view(['POST'])
def add_district(request):
    state_id=request.POST.get('state_id',None)
    name=request.POST.get('name',None)
    rainfall_type=request.POST.get('rainfall_type',None)
    if state_id is None or name is None or rainfall_type is None:
        context={
            'message':'state_id/name/rainfall_id is missing'
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            new_record=District.objects.create(
                state_id=state_id,
                name=name,
                rainfall_type=rainfall_type
            )
            new_record.save()
            context={
                'message':'district added successfully',
                'data':{
                    'state_id':new_record.state_id,
                    'state_name':new_record.state.name,
                    'district_id':new_record.id,
                    'name':new_record.name,
                    'rainfall_type':new_record.rainfall_type,
                    'created_at':new_record.created_at,
                    'updated_at':new_record.updated_at
                }
            }
            return  Response(context,status=status.HTTP_200_OK)
        except ValueError:
            context={
                'message':'invalid district_id'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            context={
                'message':'invalid state_id'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_district(request):
    all_district=District.objects.all()
    data=[]
    for district in all_district:
        temp={
            'state_id':district.state_id,
            'district_id':district.id,
            'name':district.name,
            'rainfall_type':district.rainfall_type,
        }
        data.append(temp)
        context={
            'data':data
        }
    return Response(context,status=status.HTTP_200_OK)
@api_view(['PATCH'])
def update_district(request):
    state_id=request.POST.get('state_id',None)
    district_id=request.POST.get('district_id',None)
    name=request.POST.get('name',None)
    rainfall_type=request.POST.get('rainfall_type',None)
    if state_id is None or district_id is None or name is None or rainfall_type is None:
        context={
            'message':'state_id/district_id/name/rainfall_type is missing'
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            new_record=District.objects.get(id=district_id)
            new_record.state_id=state_id if state_id is not None else new_record.state_id
            new_record.district_id=district_id if district_id is not None else new_record.id
            new_record.name=name if name is not None else new_record.name
            new_record.rainfall_type=rainfall_type if rainfall_type is not None else new_record.rainfall_type
            new_record.save()
            context={
                'message':'district updated successfully'
            }
            return Response(context,status=status.HTTP_200_OK)
        except District.DoesNotExist:
            context={
                'message':'invalid district_id'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            context={
                'message':'invalid...'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_district(request):
    district_id=request.POST.get('district_id',None)
    if district_id is None:
        context={
            'message':'district_id is missing'
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            district=District.objects.get(id=district_id)
            district.delete()
            context={
                'message':'successfully deleted'
            }
            return Response(context,status=status.HTTP_200_OK)
        except ValueError:
            context={
                'message':'invalid district_id'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)
        except District.DoesNotExist:
            context={
                'message':'invalid district_id'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def add_state(request):
    name=request.POST.get('name',None)
    if name is None:
        context={
            'message':'name is missing'
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            new_record=State.objects.create(
                name=name
            )
            new_record.save()
            context={
                'message':'state added successfully',
                'data':{
                    "name":new_record.name
                }
            }
            return Response (context,status=status.HTTP_200_OK)
        except ValueError:
            context={
                'message':'invalid state'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def list_state(request):
    all_state=State.objects.all()
    data=[]
    for state in all_state:
        temp={
            'state_id':state.id,
            'name':state.name
        }
        data.append(temp)
        context={
            'data':data
        }
    return Response(context,status=status.HTTP_200_OK)
@api_view(['PATCH'])
def update_state(request):
    state_id=request.POST.get('state_id',None)
    new_state_name=request.POST.get('new_state_name',None)
    if state_id is None or new_state_name is None:
        context={
            'message':'state_id/new_state_name is missing'
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            get_state=State.objects.get(id=state_id)
            get_state.name=new_state_name if new_state_name is not None else get_state.name
            get_state.save()
            context={
                'message':'state updated successfully'
            }
            return Response(context,status=status.HTTP_200_OK)
        except State.DoesNotExist:
            context={
                'message':'invalid state_id'
            }
            return Response(context,status=status.HTTP_400_BAD-REQUEST)
        except ValueError:
            context={
                'message':'invalid state_id'
            }
            return Response(context,satus=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def delete_state(request):
    state_id=request.POST.get('state_id',None)
    if state_id is None:
        context={
            'message':'state_id is missing'
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            state=State.objects.get(id=state_id)
            state.delete()
            context={
                'message':'successfully deleted'
            }
            return Response(context,status=status.HTTP_200_OK)
        except ValueError:
            context={
                'message':'invalid state_id'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)
        except State.DoesNotExist:
            context={
                'message':'invalid state_id'
            }
            return Response(context,status=status.HTTP_400_BAD_BAD_REQUEST)

