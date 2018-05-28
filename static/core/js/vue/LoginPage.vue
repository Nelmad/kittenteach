<template lang="html">
  <div style="margin-top: 100px">
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
                type="text"
              >
            </div>
            <div class="registration__row">
              <input
                :placeholder="gettext('Password')"
                type="password"
              >
            </div>
          </div>

          <div v-if="registration.step == 3">
            <div class="registration__row">
              <input
                :placeholder="gettext('First Name')"
                type="text">
            </div>
            <div class="registration__row">
              <input
                :placeholder="gettext('Last Name')"
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
          type="text"
          name="email">
      </div>
      <div class="login__row">
        <input
          :placeholder="gettext('Password')"
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
export default {
  name: 'LoginPage',

  data() {
    return {
      registration: {
        show: false,
        role: '',
        step: 1
      },
      login: {}
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
      this.registration.show = true
      this.registration.step = 1
    },

    switchLogin() {
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
        console.log('registration')
      }
    },

    loginHandler() {
      console.log('login')
    },

    // TODO move to helpers
    capitalizeFirstLetter(string) {
      console.log(string)
      return string.charAt(0).toUpperCase() + string.slice(1);
    }
  }
}
</script>
