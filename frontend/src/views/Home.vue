<template>
  <div class="Home">
    <v-container fluid class="cyan lighten-4">
      <div class="ma-3 pa-3 white">
        <h1 class="pa-2 text-center">お金管理ツール</h1>
        <div class="mt-10">
          <v-data-table :headers="headers" :items="items" class="elevation-1">
            <template v-slot:item.lastmonth_money="{ item }">
              <div v-if="dataIndex(item) == 0">0</div>
              <div v-else>{{ arr_lm_moneys[dataIndex(item) - 1] }}</div>
            </template>
            <template v-slot:item.thismonth_money="{ item }">
              <div>{{ arr_lm_moneys[dataIndex(item)] }}</div>
            </template>
            <template v-slot:item.menu="{ item }">
                  <v-btn small class="ma-1 pa-1" color="primary" dark @click=put_item(item)>更新</v-btn>
                  <v-btn small class="ma-1 pa-1" color="purple" dark @click=delete_item(item)>削除</v-btn>
            </template>
          </v-data-table>
        </div>
      </div> <!-- ma-3 pa-3 -->
      <!-- addform -->
      <v-card class="ma-15">
        <v-card-title>データ追加</v-card-title>
        <v-form ref="add_form">
          <v-card-text>
            <v-select v-model="add.month" :items="monthitems" label="月" :rules=[required] ></v-select>
            <v-text-field v-model="add.money" label="給料" :rules=[required] ></v-text-field>
            <v-text-field v-model="add.travel_cost" label="交通費" :rules=[required]></v-text-field>
            <v-text-field v-model="add.difference" label="差分" :rules=[required]></v-text-field>
          </v-card-text>
        </v-form>
        <v-divider></v-divider>
        <v-card-actions>
          <v-btn text @click="add_item">送信する</v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      headers: [
        { text: "月", align: "center", value: "month" },
        { text: "前残高", align: "center", value: "lastmonth_money" },
        { text: "給料", align: "center", value: "money" },
        { text: "交通費", align: "center", value: "travel_cost" },
        { text: "差分", align: "center", value: "difference" },
        { text: "今残高", align: "center", value: "thismonth_money" },
        { text: "menu", align: "center", value: "menu" },
      ],
      add:{
        month:null,
        money:null,
        travel_cost:null,
        difference:null,
      },
      required: value => !!value || "テキストが空欄です。",
      monthitems: [ 1,2,3,4,5,6,7,8,9,10,11,12 ],
      datacsv:[],
      items:[],
      arr_lm_moneys:[],
    }
  },
  computed:{
    dataIndex(){
      return ((item) => {
        return this.items.indexOf(item);
      })
    }
  },
  methods:{
    async getItem(){
      const path = "http://localhost:5000/users" //CORS用
      // const path = "/users"
      await axios.get(path)
      .then(response => {
        console.log(response);
        this.items = response.data;
        })
      .catch(error => {console.log(error);});
      this.getLmMoneys()
    },
    getLmMoneys(){
      let arr = [];
      for(let i = 0; i<this.items.length; i++){
        if(i == 0){ arr.push(Number(this.items[i].money - this.items[i].travel_cost - this.items[i].difference))
        }else{ arr.push(Number(arr[i-1]) + Number(this.items[i].money - this.items[i].travel_cost - this.items[i].difference)) }
      }
      this.arr_lm_moneys = arr;
    },
    async add_item(){
      if (this.$refs.add_form.validate()) {
        let params=new FormData()
        params.append("month",this.add.month)
        params.append("money",this.add.money)
        params.append("travel_cost",this.add.travel_cost)
        params.append("difference",this.add.difference)
        const path = " http://localhost:5000/users" //CORS用
        // const path = "/users"
        await axios.post(path,params)
        .then(response => {
          console.log(response);
          this.$refs.add_form.reset()
          this.getItem()
        })
        .catch(error => { console.log(error); });
      } else {
        alert("空欄を入力してください。"); }
    },
  },
  created(){
    this.getItem()
  }
};
</script>