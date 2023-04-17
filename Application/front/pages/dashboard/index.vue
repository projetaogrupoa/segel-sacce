<template>
  <div>
    <DashboardComponent />
   
    <v-row justify="center" align="center">
      <div class="text-center align-center justify-center">
        <v-btn to="/dashboard/register-product" class="mt-4" color="grey darken-1"
          >Registrar Produto</v-btn
        >
      </div>
      &nbsp;&nbsp;&nbsp;
      <div class="text-center align-center justify-center">
        <v-btn to="/dashboard/register-order" class="mt-4" color="grey darken-1"
          >Ordem de Venda</v-btn
        >
      </div>
    </v-row>
  </div>
</template>

<script>
export default {
  middleware: 'auth',
  data() {
    return {};
  },
};
</script>

<style scoped>

</style>