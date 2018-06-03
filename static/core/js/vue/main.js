import Vue from 'vue'
import HomePage from './HomePage.vue'
import TeachersPage from './TeachersPage.vue'
import SubjectsPage from './SubjectsPage.vue'
import SchoolsPage from './SchoolsPage.vue'
import LoginPage from './LoginPage.vue'
import AccountPage from './AccountPage.vue'
import QuickSearchPage from './QuickSearchPage.vue'


window.onload = function () {
  Vue.prototype.staticUrl = window.static
  Vue.prototype.gettext = function(text) {return text} // TODO gettext
  Vue.prototype.$eventBus = new Vue() // Global event bus

  if (document.querySelector('#v-home-page')) {
    new Vue({
      el: '#v-home-page',
      components: {HomePage},
      template: '<HomePage/>'
    })
  }

  if (document.querySelector('#v-teachers-page')) {
    new Vue({
      el: '#v-teachers-page',
      components: {TeachersPage},
      template: '<TeachersPage/>'
    })
  }

  if (document.querySelector('#v-subjects-page')) {
    new Vue({
      el: '#v-subjects-page',
      components: {SubjectsPage},
      template: '<SubjectsPage/>'
    })
  }

  if (document.querySelector('#v-schools-page')) {
    new Vue({
      el: '#v-schools-page',
      components: {SchoolsPage},
      template: '<SchoolsPage/>'
    })
  }

  if (document.querySelector('#v-login-page')) {
    new Vue({
      el: '#v-login-page',
      components: {LoginPage},
      template: '<LoginPage/>'
    })
  }

  if (document.querySelector('#v-account-page')) {
    new Vue({
      el: '#v-account-page',
      components: {AccountPage},
      template: '<AccountPage/>'
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


