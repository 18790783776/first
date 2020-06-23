<template>
    <div>
        <h2>商品详情页</h2>
        <table border="1">
            <tr>
                <td>规格编码</td>
                <td>规格值1</td>
                <td>规格值2</td>
                <td>标准售价</td>
                <td>批发价</td>
                <td>参考进价</td>
                <td>吊牌价</td>
            </tr>
            <tr v-for = "i in list">
                <td>{{i.skucode}}</td>
                <td>{{i.code1}}</td>
                <td>{{i.code2}}</td>
                <td>{{i.price1}}</td>
                <td>{{i.price2}}</td>
                <td>{{i.price3}}</td>
                <td>{{i.price4}}</td>
            </tr>
        </table>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    data(){
        return{
            list:[],
        }
    },
    mounted(){
        // cid=this.$router.query.cid
        axios({
            url:'http://127.0.0.1:8000/shoplist/',
            method:'post',
            data:{cid:1}
        }).then(res=>{
            this.list=res.data.mes
            Console.log(this.list)
        })
    },
}
</script>



