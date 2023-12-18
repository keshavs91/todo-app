from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.request import Request as RESTRequest
from rest_framework.response import Response as RESTResponse
from rest_framework import status

from django.conf import settings

db = settings.DB
table = db.Table("todo_tasks")


@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def task_list(request: RESTRequest) -> RESTResponse:
    response = table.scan()
    items = response["Items"]
    return RESTResponse(items, status.HTTP_200_OK)


@api_view(["PUT"])
@permission_classes([permissions.IsAuthenticated])
def create_task(request: RESTRequest) -> RESTResponse:
    print("creating task in dynamo")
    data = request.data
    print(data)
    table.put_item(
        Item={
            "title": data.get("title"),
            "completed": "False",
        }
    )
    return RESTResponse("success", status.HTTP_200_OK)


@api_view(["DELETE"])
@permission_classes([permissions.IsAuthenticated])
def delete_task(request: RESTRequest) -> RESTResponse:
    data = request.data
    response = table.get_item(Key={"title": data.get("title"), "completed": "False"})
    print(response)
    if not response.get("Item"):
        return RESTResponse("task not found", status.HTTP_200_OK)

    table.delete_item(Key={"title": data.get("title"), "completed": "False"})
    return RESTResponse("success", status.HTTP_200_OK)
