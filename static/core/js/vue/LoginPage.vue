<template lang="html">
  <div style="margin-top: 100px">
    <p style="text-align: center">{{ results }}</p>
    <h2 class="login-title">{{ pageTitle }}</h2>

    <div
      v-if="registration.show"
      class="registration">

      <div
        v-if="registration.step == 1">
        <button
          @click="chooseRegistrationRole('teacher')">
          Teacher
        </button>
        <button
          @click="chooseRegistrationRole('student')">
          Student
        </button>
      </div>

      <div
        v-else
        class="registration__form-wrapper">

        <form
          class="registration__form"
          action="#">
          <div v-if="registration.step == 2">
            <div class="registration__row">
              <input
                :placeholder="gettext('Email')"
                v-model="registration.email"
                type="text"
              >
            </div>
            <div class="registration__row">
              <input
                :placeholder="gettext('Password')"
                v-model="registration.password"
                type="password"
              >
            </div>
          </div>

          <div v-if="registration.step == 3">
            <div class="registration__row">
              <input
                :placeholder="gettext('First Name')"
                v-model="registration.firstName"
                type="text">
            </div>
            <div class="registration__row">
              <input
                :placeholder="gettext('Last Name')"
                v-model="registration.lastName"
                type="text">
            </div>
          </div>

          <div class="registration__row">
            <button
              type="button"
              @click="registrationHandler">
              {{ registrationButtonText }}
            </button>
          </div>
        </form>

      </div>

      <div class="registration__row registration__row--center">
        <p>I wanna
          <a
            href="javascript:"
            @click="switchLogin"
          >use an existing account</a>.
        </p>
      </div>

    </div>

    <div
      v-else
      class="login">

      <div class="login__row">
        <input
          :placeholder="gettext('Email')"
          v-model="login.email"
          type="text"
          name="email">
      </div>
      <div class="login__row">
        <input
          :placeholder="gettext('Password')"
          v-model="login.password"
          type="password"
          name="password">
      </div>

      <div class="login__row">
        <button
          type="button"
          @click="loginHandler">
          Log In
        </button>
      </div>

      <div class="login__row">
        <p>I forgot
          <a
            href="javascript:"
            @click="forgotPasswordHandler"
          >my password</a>.
        </p>
      </div>
      <div class="login__row">
        <p>I don't have a
          <a
            href="javascript:"
            @click="switchRegistration"
          >KittenTeach account</a>.
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
      registration: {
        show: false,
        role: '',
        step: 1,
        email: '',
        password: '',
        firstName: '',
        lastName: ''
      },
      login: {
        email: '',
        password: ''
      },
      isLoading: false,
      results: '' // TODO for test
    }
  },

  computed: {
    registrationButtonText: function () {
      if (this.registration.step == 2) {
        return 'Next'
      } else if (this.registration.step == 3) {
        return 'Sign Up'
      }
    },

    pageTitle: function () {
      if (this.isLoading) { // TODO spinner
        return 'Loading...'
      }

      if (this.registration.show) {
        if (this.registration.step == 1) {
          return 'Choose your role'
        } else if (this.registration.step == 2) {
          return `Create a Kitten-${this.capitalizeFirstLetter(this.registration.role)}`
        } else if (this.registration.step == 3) {
          return 'One more minute...'
        }
      } else {
        return 'Log in to KittenTeach'
      }
    }
  },

  methods: {
    forgotPasswordHandler() {
      console.log('forgot password')
    },

    switchRegistration() {
      this.results = ''
      this.registration.show = true
      this.registration.step = 1
    },

    switchLogin() {
      this.results = ''
      this.registration.show = false
    },

    chooseRegistrationRole(role) {
      this.registration.role = role
      this.registration.step = 2
    },

    registrationHandler() {
      if (this.registration.step == 2) {
        this.registration.step = 3
        // TODO check if email valid and unique
      } else if (this.registration.step == 3) {
        let url = `/api/${this.registration.role}s/create`
        this.isLoading = true

        axios.post(url, {
          user: {
            email: this.registration.email,
            password: this.registration.password,
            first_name: this.registration.firstName,
            last_name: this.registration.lastName
          }
        }).then(res => {
          this.results = res.data

          this.switchLogin()

          this.isLoading = false
          this.registration.email = ''
          this.registration.firstName = ''
          this.registration.lastName = ''
        }).catch((error) => {
          this.isLoading = false
          if (error.response) {
            this.results = error.response.data
          }
        })

        this.registration.password = ''
      }
    },

    loginHandler() { // TODO refactoring
      this.isLoading = true

      axios.post('/api/auth', {
        email: this.login.email,
        password: this.login.password
      }).then(res => {
        this.isLoading = false
        this.results = res.data
      }).catch((error) => {
        this.isLoading = false
        if (error.response) {
          this.results = error.response.data
        }
      })

      this.login.password = ''
    },

    // TODO move to helpers
    capitalizeFirstLetter(string) {
      console.log(string)
      return string.charAt(0).toUpperCase() + string.slice(1);
    }
  }
}
</script>
