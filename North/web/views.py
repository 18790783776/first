from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from web.models import Catagory,Detail
from django.http import JsonResponse
import pandas as pd
import numpy as np
import pymysql
from sqlalchemy import create_engine
import xlrd
from rest_framework import serializers
from rest_framework.response import Response



# Create your views here.

'''序列化器'''
#分类序列化器
class CategorySerialzer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    pcode = serializers.CharField(max_length=255)
    pname = serializers.CharField(max_length=255)


#商品详情页序列化器:Serializer
class DetailSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    skucode=serializers.CharField(max_length=255)
    code1=serializers.CharField(max_length=255)
    code2=serializers.CharField(max_length=255)
    price1 = serializers.CharField(max_length=255)
    price2 = serializers.CharField(max_length=255)
    price3 = serializers.CharField(max_length=255)
    price4 = serializers.CharField(max_length=255)


#商品详情页序列化器:ModelSerializer

class DetailModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        # 所有序列化输出的字段
        fields = "__all__"
















'''首页展示:展示商品的种类'''
class Index(APIView):
    def get(self,request):
        catelist=Catagory.objects.filter().all()
        res=CategorySerialzer(instance=catelist,many=True)
        print('ok')
        return Response({
            'code':200,
            'mes':res.data
        })




'''提取excle中的分类的数据插入数据库？？？？？？'''
class Category(View):
    def get(self,request):
        file=xlrd.open_workbook('./商品信息20200622095138_0(6325927).xlsx')
        print(file)
        # data=file.sheet_names('商品信息')
        # table=data.sheet_by_name('商品编码')
        # print(table)
        return JsonResponse({'CODE':200})


'''展示分类下的所有商品'''
class showDetail(View):
    # def get(self,request):
    #     id=request.GET.get("id")
    #     shoplist=Detail.objects.filter(c_id_id=id)
    #     print(shoplist)
    #
    #     for i in shoplist:
    #         print(i.id,i.skucode,i.price1,i.price2,i.price3,i.price4)
    #     return render(request,'shoplist.html',locals())








# class Category(View):
#     def get(self,request):
#
#         df_list = pd.read_excel('./商品信息20200622095138_0(6325927).xlsx')
#         cate_list=df_list[['商品编码','商品名称']]
#         cate_list1=cate_list.dropna(axis=0)
#         print(cate_list1)
#
#         # conn = create_engine('mysql+pymysql://root:mysql@localhost:3306/northblue', encoding='utf8')
#         # pd.io.sql.to_sql(cate_list1, "category", conn)
#         return JsonResponse({'msg':'200'})
    def post(self,request):
        cid=request.POST.get['cid']
        print(cid,"==========================================")
        shoplist = Detail.objects.filter()
        res = DetailModelSerializer(shoplist,many=True)
        print(res.data)
        # print('ok')
        return JsonResponse({
            'code': 200,
            'mes': res.data
        })




