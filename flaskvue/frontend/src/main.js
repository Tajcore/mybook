// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import BootstrapVue from 'bootstrap-vue/dist/bootstrap-vue.esm'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import FlashMessage from '@smartweb/vue-flash-message'
import { AutoCompletePlugin } from '@syncfusion/ej2-vue-dropdowns'

Vue.use(AutoCompletePlugin)
Vue.use(BootstrapVue)
Vue.config.productionTip = false
Vue.use(FlashMessage)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
  render: h => h(App)
}).$mount('#app')
Vue.config.devtools = true
