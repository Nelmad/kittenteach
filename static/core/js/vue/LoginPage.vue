<template lang="html">
  <div
    v-if="registration.show"
    class="registration">

    <div
      v-if="registration.step == 1">
      <button
        @click="chooseRegistrationType('teacher')">
        Teacher
      </button>
      <button
        @click="chooseRegistrationType('student')">
        Student
      </button>
    </div>

    <form
      v-else
      action="#">
      <div v-if="registration.step == 2">
        <div class="registration__row">
          <input
            type="text"
            :placeholder="gettext('Email')"
          >
        </div>
        <div class="registration__row">
          <input
            type="password"
            :placeholder="gettext('Password')"
          >
        </div>
      </div>

      <div v-if="registration.step == 3">
        <input type="text">
      </div>

      <div class="registration__row">
        <button
          type="button"
          @click="registrationHandler">
          {{ registrationButtonText }}
        </button>
      </div>
    </form>

    <div class="registration__row">
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
</template>

<script>
export default {
  name: 'LoginPage',

  data() {
    return {
      registration: {
        show: false,
        type: '',
        step: 1
      },
      login: {

      }
    }
  },

  computed: {
    registrationButtonText: function () {
      if (this.registration.step == 2) {
      	return 'Next'
      } else if (this.registration.step == 3) {
      	return 'Sign Up'
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

    chooseRegistrationType(type) {
      this.registration.type = type
      this.registration.step = 2
    },

    registrationHandler() {
      if (this.registration.step == 2) {
      	this.registration.step = 3
      } else if (this.registration.step == 3) {
      	console.log('registration')
      }
    },

    loginHandler() {
      console.log('login')
    }
  }
}
</script>
