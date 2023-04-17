<template>
  <body>
    <v-app id="screen">
      <div id="header">
        <h2 class="logo">Keener Io</h2>
      </div>
      <v-main>
        <v-container fluid fill-height>
          <v-layout align-center justify-center>
            <v-flex xs12 sm8 md4>
              <v-card class="elevation-12">
                <v-toolbar dark color="#105269">
                  <v-toolbar-title>Create User</v-toolbar-title>
                </v-toolbar>
                <v-card-text>
                  <form ref="form" @submit.prevent="create()">
                    <v-text-field
                      v-model="absence.name"
                      name="nome"
                      label="Nome"
                      type="text"
                      placeholder="nome"
                      required
                    ></v-text-field>
                    <v-text-field
                      v-model="absence.email"
                      name="email"
                      label="Email"
                      type="text"
                      placeholder="email"
                      required
                    ></v-text-field>

                    <v-text-field
                      v-model="absence.password"
                      name="password"
                      label="Password"
                      type="password"
                      placeholder="password"
                      required
                    ></v-text-field>
                    <v-col class="d-flex" cols="12" sm="6">
                      <v-select
                        :items="items"
                        v-model="input.id"
                        item-value="id"
                        item-text="name"
                        label="Administrador"
                        dense
                        outlined
                      >
                      </v-select>
                    </v-col>
                    <div>
                      <div>
                        <label>Foto</label>
                      </div>
                      <v-avatar size="48">
                        <span :src="image" alt="">
                          <v-img max-width="48" :src="image">
                            <input
                              id="file"
                              class="d-none"
                              @change="handleImage"
                              type="file"
                              accept="image/*"
                              ref="file"
                            />
                          </v-img>
                        </span>
                      </v-avatar>
                      
                      <v-btn @click="$refs.file.click()"
                        ><v-icon>mdi-cloud-upload</v-icon></v-btn
                      >
                    </div>
                    <v-btn
                      type="submit"
                      class="mt-4"
                      color="black-white"
                      value="log in"
                      >Create</v-btn
                    >
                    <div class="text-right">
                      <v-btn to="login" class="mt-4" color="black-white"
                        >Have an account? Login</v-btn
                      >
                    </div>
                  </form>
                </v-card-text>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
      </v-main>
    </v-app>
  </body>
</template>

<script>
export default {
  name: "InspirePage",
};
</script>
