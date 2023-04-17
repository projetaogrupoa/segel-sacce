<template>
  <div>
    <div class="img">
      <v-row justify="center" align="center">
        <img src="" />
      </v-row>
    </div>

    <v-navigation-drawer
      absolute
      v-model="drawer"
      :mini-variant.sync="mini"
      permanent
      light
    >
      <v-list-item class="px-2">
        <v-list-item-avatar>
          <v-img src="https://randomuser.me/api/portraits/men/85.jpg"></v-img>
        </v-list-item-avatar>

        <v-list-item-title>John Leider</v-list-item-title>

        <v-btn icon @click.stop="mini = !mini">
          <v-icon>mdi-chevron-left</v-icon>
        </v-btn>
      </v-list-item>

      <v-divider></v-divider>

      <v-list dense>
        <v-list-item v-for="item in items" :key="item.title" link :to="item.route">
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>

<script>
export default {
  data() {
    return {
      drawer: true,
      items: [
        { title: "Início", icon: "mdi-home-city" },
        { title: "Minha Conta", icon: "mdi-account" },
        { title: "Produtos", icon: "mdi-package" },
        { title: "Vendas", icon: "mdi-tag" },
        { title: "Usuários", icon: "mdi-account-group-outline" },
        {title: "Sair", icon: "mdi-logout", route: "/login"}
      ],
      mini: true,
    };
  },
};
</script>

<style scoped>

.img {
  padding: 24px;
  height: 12%;
  align-content: center;
  justify-content: center;
}
</style>