<template>
  <v-app id="screen">
    <div id="header"></div>
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
                    v-model="asser.name"
                    name="nome"
                    label="nome"
                    type="text"
                    placeholder="nome"
                    required
                  ></v-text-field>
                  <v-text-field
                    v-model.number="asser.comission"
                    name="comission"
                    label="Commision"
                    type="number"
                    placeholder="comission"
                  ></v-text-field>

                  <v-text-field
                    v-model.number="asser.discount"
                    name="discount"
                    label="Discount"
                    type="number"
                    placeholder="discount"
                  ></v-text-field>
                  <v-text-field
                    v-model.number="asser.family"
                    name="family"
                    label="Family Plan"
                    type="number"
                    placeholder="Family Plan"
                    required
                  ></v-text-field>
                  <v-text-field
                    v-model="asser.link"
                    name="link"
                    label="link"
                    type="text"
                    placeholder="link"
                    required
                  ></v-text-field>

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
                     <v-avatar size="48">
                        
                          <v-img max-width="48" :src="imageGet">
                            <input
                              id="file"
                              class="d-none"
                              @change="handleImage"
                              type="file"
                              accept="image/*"
                              ref="file"
                            />
                          </v-img>
                      
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
                </form>
              </v-card-text>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-main>

    <div class="teste" style="border: 2px solid red">
      <figure class="image" v-for="item in list" :key="item.id">
        <img :src="showImage(item.image)" alt="">
      </figure>
    </div>
  </v-app>
</template>

<script>
import axios from "axios";
export default {
  name: "DefaultLayout",
  data: () => ({
    image: "",
    imageGet: "",
    asser: [
      {
      id: 0,
      name: "",
      comission: 0,
      discount: 0,
      family: 0,
      image: "",
      link: "",
    },
    ],
    list:[] 
  }),

created() {
  this.getImage()
},

  methods: {

    showImage(url){
      return "https://localhost:7238/" + url;
    },
  
    async getImage(){
      await axios({
        method: "get",
        url: "https://localhost:7238/Supplier/List",
        
      }).then((response) => {
          
          console.log(response.data);
          this.list = response.data.content
        })

    },
    async create() {
      console.log(this.asser);
      await axios({
        method: "post",
        url: "https://localhost:7238/Supplier/Add-Supplier",
        data: {
          supplier: {
            Id: 0,
            Name: this.asser.name,
            Image: this.image,
            Comission: this.asser.comission,
            Descont: this.asser.discount,
            FamilyPlan: this.asser.family,
            Link: this.asser.link,
          },
        },
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
          "Access-Control-Allow-Origin": "*",
        },
      })
        .then((response) => {
          console.log(this.asser);
          console.log(response);
        })
        .catch((error) => {
          console.log(error.response.data);
          console.log(error.response.status);
          console.log(error.response.headers);
          console.log(Object.values(error.response.data.errors).flat().join());
          console.log(JSON.stringify(error.response.data.errors));
        });
    },
    async handleImage(e) {
      const selectedImage = e.target.files[0];
      this.createBase64Image(selectedImage);
    },
    async createBase64Image(fileObject) {
      const reader = new FileReader();

      reader.onload = (e) => {
        this.image = e.target.result;
        console.log(this.image)
      };
      reader.readAsDataURL(fileObject);
    },
  },
};
</script>
