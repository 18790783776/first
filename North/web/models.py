from django.db import models

# Create your models here.

class Catagory(models.Model):
    id=models.AutoField(primary_key=True)
    pcode=models.CharField(max_length=255,verbose_name="商品编号")
    pname=models.CharField(max_length=255,verbose_name="商品名称")

    class Meta:
        db_table="category"

class Detail(models.Model):
    id=models.AutoField(primary_key=True)
    skucode=models.CharField(max_length=255,verbose_name="规格编码",null=True)
    code1=models.CharField(max_length=255,verbose_name="规格值1",null=True)
    code2=models.CharField(max_length=255,verbose_name="规格值2",null=True)
    barcode=models.CharField(max_length=255,verbose_name="条码",null=True)       #可能是一个图片？？？？？？？？？？？？？？？？？
    pnumber=models.CharField(max_length=255,verbose_name="货号",null=True)
    weight=models.CharField(max_length=255,verbose_name="重量(kg)",default='0.0')
    longth=models.CharField(max_length=255,verbose_name="长度(cm)",default='0.0')
    width=models.CharField(max_length=255,verbose_name="宽度(cm)",default='0.0')
    heigh=models.CharField(max_length=255,verbose_name="高度(cm)",default='0.0')
    volume=models.CharField(max_length=255,verbose_name="体积(m^3)",default='0.0')
    inventory1=models.CharField(max_length=255,verbose_name="初期库存",null=True)
    const1=models.CharField(max_length=255,verbose_name="初期成本价",null=True)
    locatcode=models.CharField(max_length=255,verbose_name="货位编码",null=True)
    fenlei=models.CharField(max_length=255,verbose_name="分类",null=True)
    brand=models.CharField(max_length=255,verbose_name="品牌",null=True)
    invoicename=models.CharField(max_length=255,verbose_name="开票名称",null=True)
    taxrax=models.CharField(max_length=255,verbose_name="税率",null=True)
    price1=models.CharField(max_length=255,verbose_name="标准售价")
    price2=models.CharField(max_length=255,verbose_name="批发价")
    price3=models.CharField(max_length=255,verbose_name="参考价")
    price4=models.CharField(max_length=255,verbose_name="吊牌价",null=True)
    danwei=models.CharField(max_length=255,verbose_name="单位",null=True)
    pic1=models.CharField(max_length=255,verbose_name="图片1",null=True)
    pic2=models.CharField(max_length=255,verbose_name="图片2",null=True)
    pic3=models.CharField(max_length=255,verbose_name="图片3",null=True)
    pic4=models.CharField(max_length=255,verbose_name="图片4",null=True)
    remarks=models.CharField(max_length=255,verbose_name="备注",null=True)
    invendays=models.CharField(max_length=255,verbose_name="消耗周期（天）",null=True)
    manufacturer=models.CharField(max_length=255,verbose_name="生产商",null=True)
    supplier=models.CharField(max_length=255,verbose_name="默认供应商",null=True)
    baozhiqi=models.CharField(max_length=255,verbose_name="保质期（天）",null=True)
    purtype=models.CharField(max_length=255,verbose_name="采购类型",null=True)
    '''
    这些字段暂时不需要
    # pcount=models.CharField(max_length=255,verbose_name="数量",null=True)
    # specifiactions=models.CharField(max_length=255,verbose_name="规格")
    # pkind=models.CharField(max_length=255,verbose_name="种类")
    # flavor=models.CharField(max_length=255,verbose_name="口味")
    # leixing=models.CharField(max_length=255,verbose_name="类型")
    # netcontent=models.CharField(max_length=255,verbose_name="净含量")
    # texture=models.CharField(max_length=255,verbose_name="材质")
    # segnum=models.CharField(max_length=255,verbose_name="段数")
    # segment=models.CharField(max_length=255,verbose_name="段位")
    # packmeth=models.CharField(max_length=255,verbose_name="包装方式")
    # capacity=models.CharField(max_length=255,verbose_name="容量")
    # origin=models.CharField(max_length=255,verbose_name="产地")
    # vality=models.CharField(max_length=255,verbose_name="有效期")
    
    '''
    c_id=models.ForeignKey('Catagory',on_delete=models.CASCADE,null=True,blank=True)

    class Meta:
        db_table="detail"








































































































































































