<template>
  <div class="Home">
    <v-container fluid>
      <div class="mx-3">
        <h1 class="pa-2 text-center">お金管理ツール</h1>
        <div class="mt-10">
          <v-data-table :headers="headers" :items="items" class="elevation-1">
          </v-data-table>
        </div>
      </div>
    </v-container>
  </div>
</template>

<script>
import data from '../assets/test.csv'
export default {
  data() {
    return {
      headers: [
        { text: "月", align: "center", value: "month" },
        { text: "給料", align: "center", value: "money" },
        { text: "交通費", align: "center", value: "travel_cost" }
      ],
      items:[],
      datacsv:data
    };
  },
  methods:{
    async getCsv(){
      //tableに表示できる形式にする。(json)
      const key = ["month","money","travel_cost"] //key
      for(let i=0;i<this.datacsv.length - 1;i++){ //配列数だけ (配列が無駄に一個多い)
        let tmp = new Object()
        let vnum = 0 //valueカウント
        for(let j=0;j<3;j++){ //要素数だけ
          tmp[key[j]] = this.datacsv[i][vnum]; //i番目の配列の要素を順に連想配列に格納
          vnum = vnum + 1  //value++
        } //j for
        this.items.push(tmp); //push
      } //i for
    console.log(this.items);
    } //getCsv()
  },
  created(){
    this.getCsv();
  }
};
</script>