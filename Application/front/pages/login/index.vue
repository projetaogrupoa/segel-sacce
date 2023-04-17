<template>
  <div class="body">
    <v-app style="background-color: white; color: white">
      <v-layout justify-center>
        <v-flex xs12 sm8 md4>
          <v-card class="d-flex flex-column text-center" color="grey lighten-5">
            <v-toolbar color="grey darken-1">
              <v-toolbar-title>Área de Acesso</v-toolbar-title>
            </v-toolbar>
            <v-card-text>
              <form ref="form">
                <v-text-field
                  v-model="user.email"
                  height="40"
                  dense
                  light
                  persistent-hint
                  :rules="[
                    (v) => !!v || 'E-mail obrigatório',
                    (v) => /.+@.+\..+/.test(v) || 'E-mail inválido',
                  ]"
                  outlined
                  @keypress.enter="login"
                >
                  <template v-slot:prepend-inner>
                    <v-tooltip bottom>
                      <template v-slot:activator="{ on }">
                        <v-icon color="black" v-on="on"
                          >mdi-account-outline</v-icon
                        >
                      </template>
                      Email
                    </v-tooltip>
                  </template>
                </v-text-field>

                <v-text-field
                  v-model="user.password"
                  autocomplete="password-field"
                  height="40"
                  dense
                  light
                  persistent-hint
                  :rules="[(v) => !!v || 'Senha obrigatória']"
                  :append-icon="
                    show ? 'mdi-eye-outline' : 'mdi-eye-off-outline'
                  "
                  outlined
                  :type="show ? 'text' : 'password'"
                  @click:append="show = !show"
                  @keypress.enter="login"
                >
                  <template v-slot:prepend-inner>
                    <v-tooltip bottom>
                      <template v-slot:activator="{ on }">
                        <v-icon color="black" v-on="on"
                          >mdi-lock-outline</v-icon
                        >
                      </template>
                      Senha
                    </v-tooltip>
                  </template>
                </v-text-field>
                <div class="text-center justify-center">
                  <v-btn
                    color="grey darken-1"
                    @click="signIn()"
                    >Acessar</v-btn
                  >
                  <div class="text-center justify-center">
                    <v-btn to="/register" class="mt-4" color="grey darken-1"
                      >Registrar</v-btn
                    >
                  </div>
                </div>

                <div
                  class="text-center justify-center"
                  style="margin-top: 10px"
                >
                  <router-link
                    to="login/forgot-password"
                    align-center
                    color="white"
                    >Esqueceu a Senha?</router-link
                  >
                </div>
              </form>
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-app>
  </div>
</template>



<script>
export default {
  name: "Login",

  data() {
    return {
      user: {
        email: "",
        password: "",
      },
      show: false,
    };
  },
  methods: {
    async signIn() {

      const User = new FormData();

      User.append('username', this.user.email)
      User.append('password', this.user.password)
        
      await this.$auth
        .loginWith("local", {data: User})
        .then((response) => {
            
            this.$auth.setUser(response.data.user);
            this.$toast.success("Acesso permitido!"),
            this.$router.push("dashboard");
    
        })
        .catch(() => {});
    },
  },
};
</script>

<style scoped>
.body {
  padding: 80px;
}
</style>