import Vue from 'vue'
import Router from 'vue-router'

const routerOptions = [
  { path: '/', name: 'Landing', component: 'Landing_Page' },
  { path: '/home', name: 'Home', component: 'Home_Page' },
  { path: '*', component: 'NotFound' },
  // eslint-disable-next-line standard/object-curly-even-spacing
  { path: '/profile/:id', name: 'Profile', component: 'Profile'},
  // eslint-disable-next-line standard/object-curly-even-spacing
  { path: '/groups', name: 'Groups', component: 'Groups_page'},
  // eslint-disable-next-line standard/object-curly-even-spacing
  { path: '/group/:id', name: 'Group', component: 'Group_page'},
  // eslint-disable-next-line standard/object-curly-even-spacing
  { path: '/search/:srch', name: 'SearchPage', component: 'UserSearch'}
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
