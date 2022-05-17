from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UploadFileSerializer
import pandas
from typing import List
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import parser_classes
from drf_yasg import openapi
from django.http import HttpResponse


# Create your views here.
def parse_file(file, columns_list: List):
    return_dictionary = {
        "file": file.name,
        "summary": []
    }

    excel_file = pandas.ExcelFile(file)
    df = excel_file.parse(0)
    for column in columns_list:
        for col in df.columns:
            col_name = str(col).replace('Unnamed: ', '')

            if col_name == str(column):
                numeric_col = pandas.to_numeric(df[col], 'coerce')
                sum_value = numeric_col.sum(skipna=True)
                mean_value = numeric_col.mean(skipna=True)
                return_dictionary['summary'].append({"column": str(col_name), "sum": str(sum_value), "avg": str(mean_value)})
    return return_dictionary


class FileSummary(APIView):
    """
    Returns a summary of the given columns in uploaded xls file
    """
    serializer_class = UploadFileSerializer

    @staticmethod
    def get(request):
        return Response(status=status.HTTP_200_OK)

    register_parameters = [openapi.Parameter(
        'uploaded_file', in_=openapi.TYPE_FILE, description='Upload file', type=openapi.TYPE_FILE,
        required=True),
        openapi.Parameter(
            'columns_list', in_=openapi.TYPE_STRING, description='Columns list', type=openapi.TYPE_STRING,
            required=True)
    ]

    @swagger_auto_schema(request_body=UploadFileSerializer, manual_parameters=register_parameters)
    @parser_classes((FormParser, MultiPartParser,))
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            uploaded_file = request.data['uploaded_file']
            result = parse_file(uploaded_file, list(request.data['columns_list']))
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


def home(response):
    return HttpResponse("Welcome to Unversal Test Project")
