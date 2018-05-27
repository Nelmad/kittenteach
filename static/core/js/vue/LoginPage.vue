<template lang="html">
  <div
    v-if="registration.show"
    class="registration">
    <form
      action="#">
      <div v-if="registration.step == 1">
        <div class="registration__row">
          <input type="text">
        </div>
        <div class="registration__row">
          <input type="text">
        </div>
      </div>

      <div v-if="registration.step == 2">
        <input type="text">
      </div>
    </form>
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
      <p>I forgot
        <a
          href="javascript:"
          @click="forgotPassword"
        >my password</a>.
      </p>
    </div>
    <div class="login__row">
      <button type="button">Log In</button>
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
        step: 1
      }
    }
  },
  methods: {
    forgotPassword() {
      console.log('forgot password')
    }
  }
}
</script>
