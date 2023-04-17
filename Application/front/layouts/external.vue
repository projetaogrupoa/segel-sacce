<template>
  <v-app class="body" :dark="$vuetify.theme.dark" style="background: var(--v-primary-base)">
    <div class="img">
      <img src="" />
    </div>
    <v-main>
      <Nuxt />
    </v-main>
  </v-app>
</template>


<style scoped>
.body {
  overflow: hidden;
  height: 100vh;
}
.img {
  padding: 24px;
  height: 12%;
}
</style>