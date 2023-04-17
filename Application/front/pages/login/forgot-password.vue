<template>
  <div>
    <v-app style="background-color: white; color: white">
      <v-layout justify-center>
        <v-flex xs12 sm8 md4>
          <v-card
            class="d-flex flex-column justify-center text-center"
            color="grey lighten-5"
            max-width="344"
            title="User Registration"            
          >
            <v-toolbar height="55" color="grey darken-1">
              <v-toolbar-title>Esqueci a Senha</v-toolbar-title>
            </v-toolbar>
            <v-container>
              <v-text-field
                v-model="register.email"
                color="black"
                light
                label="Email"
                variant="underlined"
                outlined
                :rules="[
                    (v) => !!v || 'E-mail obrigatório',
                    (v) => /.+@.+\..+/.test(v) || 'E-mail inválido',
                  ]"
              ></v-text-field>
            </v-container>

            <v-divider></v-divider>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn to="/login" color="grey darken-1">
                Enviar
                <v-icon icon="mdi-chevron-right" end></v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-app>
  </div>
  
</template>

<script>
export default {
  name: "ForgotPassword",
  data(){
    return{
      register:{
        email: "",
      }
    }
  }
};
</script>


<style scoped>

.text-black  {
  color: black !important;
}

</style>

