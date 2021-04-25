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
export default {
  data() {
    return {
      headers: [
        { text: "月", align: "center", value: "month" },
        { text: "給料", align: "center", value: "money" },
        { text: "交通費", align: "center", value: "travel_cost" }
      ],
      items:[],
      datacsv:"",
    };
  },
  methods:{
    //
  },
  created(){
    //
  }
};
</script>