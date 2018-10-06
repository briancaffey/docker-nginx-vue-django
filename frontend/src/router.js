import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/subdomain',
      name: 'home',
      component: () => {
        const reg = new RegExp('www|sitename|test|localhost:8000');
        const parts = window.location.host.split('.');
        return reg.test(parts[0]) ? import('./views/Home') : import('./views/Charts');
      },
    },
    {
      path: '/charts',
      name: 'charts',
      component: () => import(/* webpackChunkName: "charts" */ './views/Charts.vue'),
    },
    {
      path: '/posts',
      name: 'posts',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "posts" */ './views/Posts.vue'),
    },
    {
      path: '/login',
      name: 'login',
      component: () => import(/* webpackChunkName: "login" */ './views/Login.vue'),
    },
    {
      path: '/docs',
      name: 'documents',
      component: () => import(/* webpackChunkName: "documents" */ './views/Documents.vue'),
    },
  ],
});
