<template lang="html">
  <div :style="{ marginTop: `${marginTop}px` }">
    <h2 class="login-title">{{ pageTitle }}</h2>

    <div
      v-if="errorMessages && errorMessages.length > 0"
      class="login-error error">
      <ul class="error__list error-list error-list--tooltip">
        <li
          v-for="(errorMessage, index) in errorMessages"
          :key="index"
          class="error-list__item">
          {{ errorMessage }}
        </li>
      </ul>
    </div>

    <div
      v-if="registration.show"
      class="registration">

      <div
        v-if="registration.step == 1"
        class="registration__roles-container">
        <button
          type="button"
          class="registration__btn registration__btn--image registration__btn--margin"
          @click="chooseRegistrationRole('student')">
          <img
            :src="`${staticUrl}core/img/roles/student.svg`"
            alt="Student"
          >
          <span class="registration__roles-description">Student</span>
        </button>

        <button
          type="button"
          class="registration__btn registration__btn--image registration__btn--margin"
          @click="chooseRegistrationRole('teacher')">
          <img
            :src="`${staticUrl}core/img/roles/teacher.svg`"
            alt="Teacher"
          >
          <span class="registration__roles-description">Teacher</span>
        </button>
      </div>

      <div
        v-else-if="registration.step == 2"
        class="registration__form-wrapper">

        <form
          class="registration__form"
          action="#">
          <div class="registration__row registration__row--mb5">
            <input
              :placeholder="gettext('Email')"
              v-model="registration.email"
              class="registration__input"
              type="text"
            >
          </div>
          <div class="registration__row registration__row--mb5">
            <input
              :placeholder="gettext('Password')"
              v-model="registration.password"
              class="registration__input"
              type="password"
            >
          </div>
          <div class="registration__row registration__row--mb5">
            <input
              :placeholder="gettext('First Name')"
              v-model="registration.firstName"
              class="registration__input"
              type="text"
            >
          </div>
          <div class="registration__row registration__row--mb10">
            <input
              :placeholder="gettext('Last Name')"
              v-model="registration.lastName"
              class="registration__input"
              type="text"
            >
          </div>

          <div class="registration__row registration__row--mb8">
            <button
              type="button"
              class="registration__btn"
              @click="registrationHandler">
              Create Account
            </button>
          </div>
        </form>

      </div>

      <div class="registration__row">
        <p class="registration__text registration__text--middle">I wanna
          <a
            href="javascript:"
            @click="switchLogin">
            use an existing account.
          </a>
        </p>
      </div>

    </div>

    <div
      v-else-if="forgot.show"
      class="login">

      <div class="login__row login__row--mb14 ">
        <p class="login__text">Enter your email address below and we'll send you a link to reset your password.</p>
      </div>

      <form
        class="login__form"
        action="#">
        <div class="login__row login__row--mb10">
          <input
            :placeholder="gettext('Email Address')"
            v-model="forgot.email"
            class="login__input"
            type="text"
          >
        </div>
        <div class="login__row login__row--mb14">
          <button
            type="button"
            class="login__btn"
            @click="forgotPasswordHandler">
            Submit
          </button>
        </div>
      </form>

      <div class="login__row">
        <p class="login__text login__text--middle">Nope, take me
          <a
            href="javascript:"
            @click="switchLogin">
            back to Login.
          </a>
        </p>
      </div>

    </div>

    <div
      v-else
      class="login">

      <form
        class="login__form"
        action="#">
        <div class="login__row login__row--mb5">
          <input
            :placeholder="gettext('Email')"
            v-model="login.email"
            class="login__input"
            type="text"
            name="email"
          >
        </div>
        <div class="login__row login__row--mb10">
          <input
            :placeholder="gettext('Password')"
            v-model="login.password"
            class="login__input"
            type="password"
            name="password"
          >
        </div>

        <div class="login__row login__row--mb8">
          <button
            type="button"
            class="login__btn"
            @click="loginHandler">
            Log In
          </button>
        </div>
      </form>

      <div class="login__row login__row--mb10">
        <p class="login__text login__text--small">I forgot
          <a
            href="javascript:"
            @click="switchForgotPassword">
            my password.
          </a>
        </p>
      </div>
      <div class="login__row">
        <p class="login__text login__text--middle">I don't have a
          <a
            href="javascript:"
            @click="switchRegistration">
            KittenTeach account.
          </a>
        </p>
      </div>

    </div>
  </div>

</template>

<script>
import axios from 'axios'

export default {
  name: 'LoginPage',

  data() {
    return {
      staticUrl: window.static,
      registration: {
        show: false,
        role: '',
        step: 1,
        email: '',
        password: '',
        firstName: '',
        lastName: ''
      },
      forgot: {
        show: false,
        email: ''
      },
      login: {
        email: '',
        password: ''
      },
      isLoading: false,
      marginTop: 170,
      errorMessages: []
    }
  },

  computed: {
    pageTitle: function () {
      if (this.isLoading) { // TODO spinner
        return 'Loading...'
      }

      if (this.registration.show) {
        if (this.registration.step == 1) {
          return 'Choose your role'
        } else if (this.registration.step == 2) {
          return `Create a Kitten-${this.capitalizeFirstLetter(this.registration.role)}`
        }
      } else {
        return 'Log in to KittenTeach'
      }
    }
  },

  created() {
    switch (window.location.hash) {
    case '#/auth':
      break
    case '#/signup':
      this.switchRegistration()
      break
    case '#/forgot':
      this.switchForgotPassword()
      break
    default:
      this.switchLogin()
    }
  },

  methods: {
    switchLogin() {
      history.pushState(null, null, '#/auth');
      this.errorMessages.length = 0
      this.forgot.show = false
      this.registration.show = false
      this.marginTop = 170
    },

    switchRegistration() {
      history.pushState(null, null, '#/signup');
      this.errorMessages.length = 0
      this.forgot.show = false
      this.registration.show = true
      this.registration.step = 1
      this.marginTop = 120
    },

    switchForgotPassword() {
      history.pushState(null, null, '#/forgot');
      this.errorMessages.length = 0
      this.forgot.show = true
      this.registration.show = false
    },

    chooseRegistrationRole(role) {
      this.registration.role = role
      this.registration.step = 2
      this.marginTop = 170
    },

    registrationHandler() {
      if (this.registration.step == 2) {
        let role = this.registration.role.toLocaleLowerCase()
        let url = `/api/${role}s/create`

        this.isLoading = true

        axios.post(url, {
          user: {
            email: this.registration.email,
            password: this.registration.password,
            first_name: this.registration.firstName,
            last_name: this.registration.lastName
          }
        }).then(result => {
          this.isLoading = false
          this.errorMessages.length = 0
          console.log(result)
          // this.results = res.data

          this.switchLogin()

          this.registration.email = ''
          this.registration.password = ''
          this.registration.firstName = ''
          this.registration.lastName = ''
        }).catch(error => {
          let errorData = error.response.data
          this.isLoading = false

          if (errorData) {
            this.errorMessages = Object.values(errorData['user']).map(e => e[0])
          } else {
            this.errorMessages = ['Something went wrong...']
          }

          this.registration.password = ''
          this.registration.step = 2
        })
      }
    },

    loginHandler() { // TODO refactoring
      this.isLoading = true

      axios.post('/api/auth', {
        email: this.login.email,
        password: this.login.password
      }).then(result => {
        this.isLoading = false
        this.errorMessages.length = 0
        console.log(result)
        // this.results = res.data // TODO

        this.login.email = ''
        this.login.password = ''
      }).catch(error => {
        let errorData = error.response.data
        this.isLoading = false

        if (errorData) {
          this.errorMessages = Object.values(errorData).map(e => e[0])
        } else {
          this.errorMessages = ['Something went wrong...']
        }

        this.login.password = ''
      })
    },

    forgotPasswordHandler() {
      this.isLoading = true

      axios.post('/api/reset-password', {

      }).then(result => {
        this.isLoading = false
        this.errorMessages.length = 0
        console.log(result)

        this.forgot.email = ''
      }).catch(error => {
        let errorData = error.response.data
        this.isLoading = false

        if (errorData) {
          this.errorMessages = [errorData.message]
        } else {
          this.errorMessages = ['Something went wrong...']
        }

        this.forgot.email = ''
      })
    },

    // TODO move to helpers
    capitalizeFirstLetter(string) {
      console.log(string)
      return string.charAt(0).toUpperCase() + string.slice(1);
    }
  }
}
</script>
