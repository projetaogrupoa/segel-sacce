<template>
  <v-app class="body" :dark="$vuetify.theme.dark" style="background: var(--v-primary-base)">
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
</style>