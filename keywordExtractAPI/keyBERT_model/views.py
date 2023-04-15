from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import KeyBERTModelSerializer
from .models import KeyBERTModel
from django.http import Http404
from .keybert import showForKeyBERT


global id_, input_text


class KeyBERTModelList(APIView):
    def get(self, request, *args, **kwargs):
        textObj = KeyBERTModel.objects.all()
        serializer = KeyBERTModelSerializer(textObj, many=True)
        #이 파일에서 사용할 코드(id, input_text)
        ordered_dic = serializer.data[len(serializer.data) - 1].items()
        arr = []
        for key, val in ordered_dic:
            arr.append(val)
        global id_
        id_ = arr[0]
        global input_text
        input_text = arr[1]
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = KeyBERTModelSerializer(
            data=request.data)
        if serializer.is_valid():
            serializer.save()
            #print(request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class KeyBERTModelDetail(APIView):
    def get_object(self, pk):
        try:
            return KeyBERTModel.objects.get(pk=pk)
        except KeyBERTModel.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        text_model = self.get_object(pk)
        serializer = KeyBERTModelSerializer(text_model)
        return Response(serializer.data)

    def put(self, request, pk):
        text_model = self.get_object(pk)
        hashtag = showForKeyBERT(input_text)

        data = {
            "input_text": input_text,
            "hashtag": hashtag
        }
        serializer = KeyBERTModelSerializer(text_model, data=data)
        if serializer.is_valid():
            serializer.save()
            #print(serializer.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        text_model = self.get_object(pk)
        text_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
