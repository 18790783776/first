<template>
    <div>
        <h2>首页展示</h2>
        <table border="1">
            <tr>
                <td>商品编号</td>
                <td>分类名称</td>
            </tr>
            <tr v-for = "i in list">
                <td>{{i.pcode}}</td>
                <!-- <td>{{i.pname}}</td> -->
                <!-- <td><router-link :to="{name: 'Detail', params: { cid: i.id }}"> {{i.pname}}</router-link></td> -->
                <td><router-link :to="{path: 'detail', query: { cid: i.id }}"> {{i.pname}}</router-link></td>
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
        axios({
            url:'http://127.0.0.1:8000/index/',
            method:'get',
        }).then(res=>{
            this.list=res.data.mes
            Console.log(this.list)
        })
    },
 
}
</script>
