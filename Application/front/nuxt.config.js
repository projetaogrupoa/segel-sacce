import colors from 'vuetify/es5/util/colors'

export default {
  // Target: https://go.nuxtjs.dev/config-target
  target: 'static',

  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    titleTemplate: '%s - src',
    title: 'src',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [

  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/vuetify
    ['@nuxtjs/vuetify']
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    '@nuxtjs/axios',
    '@nuxtjs/toast',
    '@nuxtjs/auth',
    ['v-currency-field/nuxt', {
      locale: 'pt-BR',
      decimalLength: 2,
      autoDecimalMode: true,
      min: null,
      max: null,
      defaultValue: 0,
      valueAsInteger: false,
      allowNegative: true
    }],
  ],

  axios: {
    baseURL: process.env.API_KEY, //Cant be used with proxy
    browserBaseURL: process.env.API_KEY, // client url
    common: {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Accept': 'application/json, text/plain, */*',
    },
  },

  auth: {
    redirect: {
      login: '/login',
      logout: '/login',  
    },
    strategies: {
      local: {
        endpoints: {
          login: {
            url: process.env.API_KEY+"/account/sign-in",
            method: "post",
            propertyName: "data.access_token",
          },
          logout: false,
          user: false,
        },
        tokenType: '',
        tokenName: 'x-auth',
        autoFetchUser: false
      },
    },
  },

//  router: {
    //middleware: ['auth']
  //},


  // Vuetify module configuration: https://go.nuxtjs.dev/config-vuetify
  vuetify: {
    customVariables: ['~/assets/variables.scss'],
    theme: {
      dark: true,
      themes: {
        dark: {
          primary: colors.blue.darken2,
          accent: colors.grey.darken3,
          secondary: colors.amber.darken3,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3
        }
      }
    }
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
  }
}
