<template>
  <div class="account-header">
    <h1 class="account-header__title">My Account</h1>
    <div class="account-header__image-container">
      <img
        :src="imageSrc"
        class="account-header__image"
        alt="Profile picture">
    </div>
    <p class="account-header__description">
      {{ name }}
    </p>
  </div>
</template>

<script>
export default {
  name: 'VAccountHeader',
  props: {
    name: {
      type: String,
      required: true
    },
    role: {
      type: String,
      required: true
    },
    image: {
      type: String,
      required: false,
      default: ''
    }
  },

  computed: {
    defaultImage: function () {
      return `${this.staticUrl}core/img/portrait/${this.role}-portrait.svg`
    },
    imageSrc: function () {
      return this.image || this.defaultImage
    }
  }
}
</script>
