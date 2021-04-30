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
            <template v-slot:item.difference="{ item }">
              <div class="pa-1">
                {{item.difference}}
                <div class="ma-1"><v-btn small color="primary" dark>更新</v-btn></div>
              </div>
            </template>
            <template v-slot:item.thismonth_money="{ item }">
              <div>{{ arr_lm_moneys[dataIndex(item)] }}</div>
            </template>
          </v-data-table>
        </div>
      </div>
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
      ],
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
      const path = "/users"
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
    }
  },
  created(){
    this.getItem()
  }
};
</script>