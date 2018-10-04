import HighchartsVue from 'highcharts-vue';
import BootstrapVue from 'bootstrap-vue';
import Vue from 'vue';
import './registerServiceWorker';
import App from './App.vue';
import router from './router';
import store from './store';

Vue.config.productionTip = false;

Vue.use(BootstrapVue);
Vue.use(HighchartsVue);

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');
