import Vue from 'vue'
import Router from 'vue-router'

const routerOptions = [
  { path: '/', component: 'Landing_Page' },
  { path: '/home', component: 'Home_Page' },
  { path: '*', component: 'NotFound' },
  // eslint-disable-next-line standard/object-curly-even-spacing
  { path: '/profile', component: 'Profile'}
]
const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/components/${route.component}.vue`)
  }
})
Vue.use(Router)
export default new Router({
  routes,
  mode: 'history'
})
