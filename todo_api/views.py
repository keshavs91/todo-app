from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.request import Request as RESTRequest
from rest_framework.response import Response as RESTResponse
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer


@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def task_list(request: RESTRequest) -> RESTResponse:
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return RESTResponse(serializer.data, status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def get_task(request: RESTRequest, id: str) -> RESTResponse:
    data = request.data

    if not Task.objects.filter(id=id).exists():
        return RESTResponse("failed", status.HTTP_200_OK)

    task = Task.objects.get(id=id)
    serializer = TaskSerializer(task, many=False)
    return RESTResponse(serializer.data, status.HTTP_200_OK)


@api_view(["PUT"])
@permission_classes([permissions.IsAuthenticated])
def create_task(request: RESTRequest) -> RESTResponse:
    print("creating task")
    data = request.data
    Task.objects.create(
        title=data.get("title"),
        completed=False
    )
    return RESTResponse("success", status.HTTP_200_OK)


@api_view(["DELETE"])
@permission_classes([permissions.IsAuthenticated])
def delete_task(request: RESTRequest) -> RESTResponse:
    data = request.data
    id = data.get("id")
    if not Task.objects.filter(id=id).exists():
        return RESTResponse("success", status.HTTP_200_OK)

    Task.objects.get(id=id).delete()
    return RESTResponse("success", status.HTTP_200_OK)
