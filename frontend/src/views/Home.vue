<template>
  <div class="Home">
    <v-container fluid class="cyan lighten-4">
      <div class="ma-3 pa-3 white">
        
        <!-- dialog -->
        <v-dialog v-model="put_dialog" max-width="500px">
          <v-card>
            <v-card-title>
              <span class="headline">編集する</span>
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-form ref="put_form">
                <v-row>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field v-model="put.month" label="月" :rules=[required]>月</v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field v-model="put.money" label="給料" :rules=[required]></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field v-model="put.travel_cost" label="交通費" :rules=[required]></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" md="4">
                    <v-text-field v-model="put.difference" label="差分" :rules=[required]></v-text-field>
                  </v-col>
                </v-row>
                </v-form>
              </v-container>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="editClose">キャンセル</v-btn>
                <v-btn color="blue darken-1" text @click="putItem">更新</v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog><!-- dialog -->

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
                  <v-icon small class="mr-2" @click="editItem(item)">mdi-pencil</v-icon>
        <v-icon small @click="deleteItem(item)">mdi-delete</v-icon>
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
          <v-btn text @click="addItem">送信する</v-btn>
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
      put_Index: -1,
      put_dialog: false,
      put:{
        month:"",
        money:"",
        travel_cost:"",
        difference:"",
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
      // const path = "http://localhost:5000/users" //CORS用
      const path = "/users"
      await axios.get(path)
      .then(response => {
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
    async addItem(){
      if (this.$refs.add_form.validate()) {
        let params=new FormData()
        params.append("month",this.add.month)
        params.append("money",this.add.money)
        params.append("travel_cost",this.add.travel_cost)
        params.append("difference",this.add.difference)
        // const path = " http://localhost:5000/users" //CORS用
        const path = "/users"
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
    editItem(item){
      this.put_Index = this.items.indexOf(item)
      this.put = Object.assign({}, item)
      this.put_dialog = true
    },
    editClose(){
      this.put_dialog = false
      this.put_Index = -1
    },
    async putItem(){
      if (this.$refs.put_form.validate()) {
        let params=new FormData()
        params.append("month",this.put.month)
        params.append("money",this.put.money)
        params.append("travel_cost",this.put.travel_cost)
        params.append("difference",this.put.difference)
        // const path = "http://localhost:5000/users/"+this.put_Index //CORS用
        const path = "/users/"+this.put_Index
        await axios.put(path,params)
        .then(response => {
          console.log(response);
          this.editClose()
          this.getItem()
        })
        .catch(error => { console.log(error); });
      } else { alert("空欄を入力してください。"); }
    },
    async deleteItem(item){
      const deleteIndex = this.items.indexOf(item)
      if (confirm("本当に消してもいいですか？（"+this.items[deleteIndex].month+"月分）")) {
        // const path = "http://localhost:5000/users/"+deleteIndex //CORS用
        const path = "/users/"+deleteIndex
        await axios.delete(path)
        .then(response => {
          console.log(response);
          this.getItem()
        })
        .catch(error => { console.log(error); });
      }
    }
  },
  created(){
    this.getItem()
  }
};
</script>