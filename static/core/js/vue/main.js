import Vue from 'vue'
import HomePage from './HomePage.vue'
import QuickSearchPage from './QuickSearchPage.vue'


window.onload = function () {
  Vue.prototype.gettext = window.gettext;
  Vue.prototype.$eventBus = new Vue(); // Global event bus

  if (document.querySelector('#v-home-page')) {
    new Vue({
      el: '#v-home-page',
      components: {HomePage},
      template: '<HomePage/>'
    })
  }
  if (document.querySelector('#v-quick-search-page')) {
    new Vue({
      el: '#v-quick-search-page',
      components: {QuickSearchPage},
      template: '<QuickSearchPage/>'
    })
  }
};


