from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .showtop import showTop
from .geo import get_geo_info

from .serializers import CrawlingmodelSerializer
from .models import Crawlingmodel
from .serializers import SaveImageModelSerializer2
from .models import SaveImageModel2

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.
id_=""
keyword=""
image_path_=""
class SaveImgList2(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        save_img2 = SaveImageModel2.objects.all()
        serializer2 = SaveImageModelSerializer2(save_img2, many=True)
        ordered_dic2 = serializer2.data[len(serializer2.data) - 1].items()
        arr2 = []
        global image_path_
        for key, val in ordered_dic2:
            arr2.append(val)
        image_path_ = "." + arr2[1]
        #print(image_path_)
        return Response(serializer2.data)

    def post(self, request, *args, **kwargs):
        serializer = SaveImageModelSerializer2(
            data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', serializer.errors, )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CrawlingList(APIView):
    def get(self, request, *args, **kwargs):
        crawling_model = Crawlingmodel.objects.all()
        serializer = CrawlingmodelSerializer(crawling_model, many=True)
        ordered_dic = serializer.data[len(serializer.data) - 1].items()
        arr = []
        for key, val in ordered_dic:
            arr.append(val)
        global id_
        id_ = arr[0]
        global keyword
        keyword= arr[1]
        # hashtag = showTop(keyword)
        # hashtag = "tag1 tag2 tag3"
        print("id 와 keyword")
        print(id_, keyword)
        print(type(id_))

        # 알아서 링크 이동 가능 ??????

        return Response(serializer.data)
    def post(self, request, *args, **kwargs):
        #print("@@@@@@@@@@@@@ post 실행해 serializer로 저장")
        serializer = CrawlingmodelSerializer(
            data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', serializer.errors, )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CrawlingDetail(APIView):
    def get_object(self, pk):
        try:
            return Crawlingmodel.objects.get(pk=pk)
        except Crawlingmodel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        crawling_model = self.get_object(pk)
        serializer = CrawlingmodelSerializer(crawling_model)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        crawling_model = self.get_object(pk)
        # 위치정보 수정 중
        #만약 "hashtag":"hashtag" 면 shotop+ ㅎgeo 실행 
        # 아니면 원래 데이터 가져와서 + geo만 실행
        serializer = CrawlingmodelSerializer(crawling_model)
        print("serializer.data")
        #serializer에서 데이터를 가져와야함!
        serializer_data = serializer.data
        print(serializer_data)
        if(serializer_data["hashtag"]=="hashtag"):
            print("추천해시태그 추출 중 ...")
            hashtag = showTop(keyword)
            geo = get_geo_info(image_path_)
            modify_geo = geo[:-1]
            data = {
                "id": id_,
                "keyword": keyword,
                "hashtag": hashtag + " " + modify_geo + keyword + " " + modify_geo,
            }
        
        else:
            print("위치 정보만 추출 중 ...")
            hashtag = serializer_data["hashtag"]
            hashtag_1 = hashtag.split()
            hashtag_2 = hashtag_1[:3]
            hashtag_3 = ' '.join(hashtag_2)
            print("hashtag_3")
            print(hashtag_3)
            geo = get_geo_info(image_path_)
            modify_geo = geo[:-1]
            data = {
                "id": id_,
                "keyword": keyword,
                "hashtag": hashtag_3 + " " + modify_geo + keyword + " " + modify_geo,
            }
        serializer = CrawlingmodelSerializer(crawling_model, data=data)
        #print(serializer)
#        # ----------
#        serializer_check = CrawlingmodelSerializer(crawling_model)
#        dic=serializer_check.data
#        # 만약 그 모델의 hashtag값이 임의의 값이라면
#        if(list(dic.items())[2][1]=="hashtag"):
#            hashtag = showTop(keyword)
#            geo = get_geo_info(image_path_)
#            data = {
#                "id": id_,
#                "keyword": keyword,
#                "hashtag": hashtag + " " + geo + keyword,
#            }
#            serializer = CrawlingmodelSerializer(crawling_model, data=data)
#            print("@@@ 크롤링!")
#            print(serializer)
#        #임의의 값이 아니라 추천해시태그가 들어가 있다면
#        else:
#            print("@@@ 원래 값 그대로 넣음")
#            serializer = CrawlingmodelSerializer(crawling_model, data=)
        #------------
#        print(pk)
#        print(type(pk))
#        print("@@@@@@@@@@@@@@ 크롤링 함수 사용!")
#        hashtag = showTop(keyword)
#        geo = get_geo_info(keyword)
#        data = {
#            "id": id,
#            "keyword": keyword,
#            "hashtag": hashtag + " " + geo,
#            #"hashtag_loc": "hashtag_loc" #get_geo_info(keyword)
#        }
#        print("data")
#        print(data)
#        serializer = CrawlingmodelSerializer(crawling_model, data=data)
        if serializer.is_valid():
            serializer.save()
            #print(serializer.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, pk, format=None):
        crawling_model = self.get_object(pk)
        crawling_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

################
#class ShowTopHashtag(APIView):
#    word = "치즈버거"
#    data = {
#        "Recommend Hashtags" : showTop(word),
#        "Recommend Hashtags" : get_geo_info(word)
#    }
#    def get(self, request, *args, **kwargs):
#        return render(request, 'crawling/crawling.html', {'data':data})
