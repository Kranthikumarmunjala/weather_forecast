# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status

# from datarepo.models import State,District

# # Create your views here.


# @api_view(['POST'])
# def add_district(request):
#     state_id=request.POST.get('state_id',None)
#     name=request.POST.get('name',None)
#     rainfall_type=request.POST.get('rainfall_type',None)
#     if state_id is None or name is None or rainfall_type is None:
#         context={
#             'message':'state_id/name/rainfall_id is missing'
#         }
#         return Response(context,status=status.HTTP_400_BAD_REQUEST)
#     else:
#         try:
#             new_record=District.objects.create(
#                 state_id=state_id,
#                 name=name,
#                 rainfall_type=rainfall_type
#             )
#             new_record.save()
#             context={
#                 'message':'district added successfully',
#                 'data':{
#                     'state_id':new_record.state_id,
#                     'state_name':new_record.state.name,
#                     'district_id':new_record.id,
#                     'name':new_record.name,
#                     'rainfall_type':new_record.rainfall_type,
#                     'created_at':new_record.created_at,
#                     'updated_at':new_record.updated_at
#                 }
#             }
#             return  Response(context,status=status.HTTP_200_OK)
#         except ValueError:
#             context={
#                 'message':'invalid district_id'
#             }
#             return Response(context,status=status.HTTP_400_BAD_REQUEST)
#         except IntegrityError:
#             context={
#                 'message':'invalid state_id'
#             }
#             return Response(context,status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def list_district(request):
#     all_district=District.objects.all()
#     data=[]
#     for district in all_district:
#         temp={
#             'state_id':district.state_id,
#             'district_id':district.id,
#             'name':district.name,
#             'rainfall_type':district.rainfall_type,
#         }
#         data.append(temp)
#         context={
#             'data':data
#         }
#     return Response(context,status=status.HTTP_200_OK)
# @api_view(['PATCH'])
# def update_district(request):
#     state_id=request.POST.get('state_id',None)
#     district_id=request.POST.get('district_id',None)
#     name=request.POST.get('name',None)
#     rainfall_type=request.POST.get('rainfall_type',None)
#     if state_id is None or district_id is None or name is None or rainfall_type is None:
#         context={
#             'message':'state_id/district_id/name/rainfall_type is missing'
#         }
#         return Response(context,status=status.HTTP_400_BAD_REQUEST)
#     else:
#         try:
#             new_record=District.objects.get(id=district_id)
#             new_record.state_id=state_id if state_id is not None else new_record.state_id
#             new_record.district_id=district_id if district_id is not None else new_record.id
#             new_record.name=name if name is not None else new_record.name
#             new_record.rainfall_type=rainfall_type if rainfall_type is not None else new_record.rainfall_type
#             new_record.save()
#             context={
#                 'message':'district updated successfully'
#             }
#             return Response(context,status=status.HTTP_200_OK)
#         except District.DoesNotExist:
#             context={
#                 'message':'invalid district_id'
#             }
#             return Response(context,status=status.HTTP_400_BAD_REQUEST)
#         except ValueError:
#             context={
#                 'message':'invalid...'
#             }
#             return Response(context,status=status.HTTP_400_BAD_REQUEST)

# @api_view(['DELETE'])
# def delete_district(request):
#     district_id=request.POST.get('district_id',None)
#     if district_id is None:
#         context={
#             'message':'district_id is missing'
#         }
#         return Response(context,status=status.HTTP_400_BAD_REQUEST)
#     else:
#         try:
#             district=District.objects.get(id=district_id)
#             district.delete()
#             context={
#                 'message':'successfully deleted'
#             }
#             return Response(context,status=status.HTTP_200_OK)
#         except ValueError:
#             context={
#                 'message':'invalid district_id'
#             }
#             return Response(context,status=status.HTTP_400_BAD_REQUEST)
#         except District.DoesNotExist:
#             context={
#                 'message':'invalid district_id'
#             }
#             return Response(context,status=status.HTTP_400_BAD_REQUEST)
# @api_view(['POST'])
# def add_state(request):
#     name=request.POST.get('name',None)
#     if name is None:
#         context={
#             'message':'name is missing'
#         }
#         return Response(context,status=status.HTTP_400_BAD_REQUEST)
#     else:
#         try:
#             new_record=State.objects.create(
#                 name=name
#             )
#             new_record.save()
#             context={
#                 'message':'state added successfully',
#                 'data':{
#                     "name":new_record.name
#                 }
#             }
#             return Response (context,status=status.HTTP_200_OK)
#         except ValueError:
#             context={
#                 'message':'invalid state'
#             }
#             return Response(context,status=status.HTTP_400_BAD_REQUEST)
# @api_view(['GET'])
# def list_state(request):
#     all_state=State.objects.all()
#     data=[]
#     for state in all_state:
#         temp={
#             'state_id':state.id,
#             'name':state.name
#         }
#         data.append(temp)
#         context={
#             'data':data
#         }
#     return Response(context,status=status.HTTP_200_OK)
# @api_view(['PATCH'])
# def update_state(request):
#     state_id=request.POST.get('state_id',None)
#     new_state_name=request.POST.get('new_state_name',None)
#     if state_id is None or new_state_name is None:
#         context={
#             'message':'state_id/new_state_name is missing'
#         }
#         return Response(context,status=status.HTTP_400_BAD_REQUEST)
#     else:
#         try:
#             get_state=State.objects.get(id=state_id)
#             get_state.name=new_state_name if new_state_name is not None else get_state.name
#             get_state.save()
#             context={
#                 'message':'state updated successfully'
#             }
#             return Response(context,status=status.HTTP_200_OK)
#         except State.DoesNotExist:
#             context={
#                 'message':'invalid state_id'
#             }
#             return Response(context,status=status.HTTP_400_BAD-REQUEST)
#         except ValueError:
#             context={
#                 'message':'invalid state_id'
#             }
#             return Response(context,satus=status.HTTP_400_BAD_REQUEST)
# @api_view(['DELETE'])
# def delete_state(request):
#     state_id=request.POST.get('state_id',None)
#     if state_id is None:
#         context={
#             'message':'state_id is missing'
#         }
#         return Response(context,status=status.HTTP_400_BAD_REQUEST)
#     else:
#         try:
#             state=State.objects.get(id=state_id)
#             state.delete()
#             context={
#                 'message':'successfully deleted'
#             }
#             return Response(context,status=status.HTTP_200_OK)
#         except ValueError:
#             context={
#                 'message':'invalid state_id'
#             }
#             return Response(context,status=status.HTTP_400_BAD_REQUEST)
#         except State.DoesNotExist:
#             context={
#                 'message':'invalid state_id'
#             }
#             return Response(context,status=status.HTTP_400_BAD_BAD_REQUEST)

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from datarepo.models import State, District

@api_view(['POST'])
def add_state(request):
    name = request.data.get('name')
    if not name:
        return Response({'message': 'name is missing'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        new_state = State.objects.create(name=name)
        return Response({
            'message': 'state added successfully',
            'data': {'state_id': new_state.id, 'name': new_state.name}
        }, status=status.HTTP_200_OK)
    except ValueError:
        return Response({'message': 'invalid state'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_state(request):
    states = State.objects.all()
    data = [{'state_id': s.id, 'name': s.name} for s in states]
    return Response({'data': data}, status=status.HTTP_200_OK)

@api_view(['PATCH'])
def update_state(request):
    state_id = request.data.get('state_id')
    new_name = request.data.get('new_state_name')
    if not state_id or not new_name:
        return Response({'message': 'state_id or new_state_name is missing'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        state = State.objects.get(id=state_id)
        state.name = new_name
        state.save()
        return Response({'message': 'state updated successfully'}, status=status.HTTP_200_OK)
    except State.DoesNotExist:
        return Response({'message': 'invalid state_id'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_state(request):
    state_id = request.data.get('state_id')
    if not state_id:
        return Response({'message': 'state_id is missing'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        State.objects.get(id=state_id).delete()
        return Response({'message': 'successfully deleted'}, status=status.HTTP_200_OK)
    except State.DoesNotExist:
        return Response({'message': 'invalid state_id'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_district(request):
    state_id = request.data.get('state_id')
    name = request.data.get('name')
    rainfall_type = request.data.get('rainfall_type')

    if not state_id or not name or not rainfall_type:
        return Response({'message': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        new_district = District.objects.create(state_id=state_id, name=name, rainfall_type=rainfall_type)
        return Response({
            'message': 'district added successfully',
            'data': {
                'district_id': new_district.id,
                'state_id': new_district.state_id,
                'state_name': new_district.state.name,
                'name': new_district.name,
                'rainfall_type': new_district.rainfall_type,
                'created_at': new_district.created_at,
                'updated_at': new_district.updated_at
            }
        }, status=status.HTTP_200_OK)
    except IntegrityError:
        return Response({'message': 'invalid state_id'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_district(request):
    districts = District.objects.all()
    data = [{
        'district_id': d.id,
        'state_id': d.state_id,
        'state_name': d.state.name if d.state else None,
        'name': d.name,
        'rainfall_type': d.rainfall_type
    } for d in districts]
    return Response({'data': data}, status=status.HTTP_200_OK)

@api_view(['PATCH'])
def update_district(request):
    district_id = request.data.get('district_id')
    state_id = request.data.get('state_id')
    name = request.data.get('name')
    rainfall_type = request.data.get('rainfall_type')

    if not district_id:
        return Response({'message': 'district_id is missing'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        district = District.objects.get(id=district_id)
        
        if state_id:
            district.state_id = state_id
        if name:
            district.name = name
        if rainfall_type:
            district.rainfall_type = rainfall_type
        
        district.save()

        # Prepare updated data to return
        updated_data = {
            'district_id': district.id,
            'name': district.name,
            'state_id': district.state_id,
            'state_name': district.state.name if district.state else None,
            'rainfall_type': district.rainfall_type
        }

        return Response({
            'message': 'district updated successfully',
            'updated_district': updated_data
        }, status=status.HTTP_200_OK)
    
    except District.DoesNotExist:
        return Response({'message': 'invalid district_id'}, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['PATCH'])
# def update_district(request):
#     district_id = request.data.get('district_id')
#     state_id = request.data.get('state_id')
#     name = request.data.get('name')
#     rainfall_type = request.data.get('rainfall_type')

#     if not district_id:
#         return Response({'message': 'district_id is missing'}, status=status.HTTP_400_BAD_REQUEST)
#     try:
#         district = District.objects.get(id=district_id)
#         if state_id:
#             district.state_id = state_id
#         if name:
#             district.name = name
#         if rainfall_type:
#             district.rainfall_type = rainfall_type
#         district.save()
#         return Response({'message': 'district updated successfully'}, status=status.HTTP_200_OK)
#     except District.DoesNotExist:
#         return Response({'message': 'invalid district_id'}, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['DELETE'])
# def delete_district(request):
#     district_id = request.data.get('district_id')
#     if not district_id:
#         return Response({'message': 'district_id is missing'}, status=status.HTTP_400_BAD_REQUEST)
#     try:
#         District.objects.get(id=district_id).delete()
#         return Response({'message': 'successfully deleted'}, status=status.HTTP_200_OK)
#     except District.DoesNotExist:
#         return Response({'message': 'invalid district_id'}, status=status.HTTP_400_BAD_REQUEST)
# def delete_district(request, district_id):
#     if not district_id:
#         return Response({'message': 'district_id is missing'}, status=status.HTTP_400_BAD_REQUEST)
#     try:
#         District.objects.get(id=district_id).delete()
#         return Response({'message': 'successfully deleted'}, status=status.HTTP_200_OK)
#     except District.DoesNotExist:
#         return Response({'message': 'invalid district_id'}, status=status.HTTP_400_BAD_REQUEST)
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

@csrf_exempt
@api_view(['DELETE'])
def delete_district(request, district_id):
    try:
        district = District.objects.get(id=district_id)
        deleted_data = {
            'district_id': district.id,
            'name': district.name,
            'state_id': district.state_id,
            'state_name': district.state.name if district.state else None,
            'rainfall_type': district.rainfall_type
        }
        district.delete()
        return Response({
            'message': 'District deleted successfully',
            'deleted_district': deleted_data
        }, status=status.HTTP_200_OK)
    except District.DoesNotExist:
        return Response({'message': 'Invalid district_id'}, status=status.HTTP_400_BAD_REQUEST)