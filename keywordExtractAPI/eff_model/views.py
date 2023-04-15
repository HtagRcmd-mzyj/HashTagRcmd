import os
import sys

from .inference import transWord

from efficientnet.tfkeras import EfficientNetB7
from keras.applications.imagenet_utils import decode_predictions

import segmentation_models as sm #module 'keras.utils' has no attribute 'get_file' error 수정

from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from .serializers import EffmodelSerializer
from .models import Effmodel
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import SaveImageModelSerializer
from .models import SaveImageModel

from rest_framework.permissions import IsAuthenticated

sm.set_framework('tf.keras')
sm.framework()

model = EfficientNetB7(weights='imagenet')
image_path=""

class SaveImageList(APIView):
    parser_classes = (MultiPartParser, FormParser)
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        saveImg = SaveImageModel.objects.all()
        serializer = SaveImageModelSerializer(saveImg, many=True)
        ordered_dic = serializer.data[len(serializer.data)-1].items()
        global image_path
        for key, val in ordered_dic:
            image_path = "." + val 
        print("이미지 저장 경로 ")
        print(image_path)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = SaveImageModelSerializer(data=request.data)
        #print("@@@@ serializer")
        #print(serializer)
        if serializer.is_valid():
            serializer.save()
            #print("일단 save()는 됨")
            #print(request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', serializer.errors,)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EffmodelList(APIView):
    def get(self, request, *args, **kwargs):
        effmodel = Effmodel.objects.all()
        serializer = EffmodelSerializer(effmodel, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        #print("@@@@EffmodelList post()")
        #print(request)
        #print(image_path)
        #print("keyword")
        keyword = transWord(model, image_path)
        #print("------")
        print("이미지에서 키워드 추출")
        print(keyword)
        data = {"title": keyword, "content": "content blabla"}
        serializer = EffmodelSerializer(
            data=data)
        #print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', serializer.errors,)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
