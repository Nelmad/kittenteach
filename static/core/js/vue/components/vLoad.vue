<template lang="html">
  <div class="spinner">
    <div
      v-for="item in items"
      :key="item"
      :style="{backgroundColor}"
      class="spinner__item"/>
  </div>
</template>

<script>
export default {
  name: 'VLoad',
  props: {
    color: {
      type: String,
      default: '#FFFFFF',
      required: false
    }
  },

  data() {
    return {
      itemsAmount: 12,
      colors: {
        'v-dark-green': '#005C5F',
        'v-green': '#00979D',
        'v-gray': '#737373'
      }
    }
  },

  computed: {
    items: function () {
      return [...Array(this.itemsAmount).keys()]
    },

    backgroundColor: function () {
      return this.colors[this.color] || this.color
    }
  },
}
</script>