<template>
  <div class="account-navigation">
    <ul class="account-navigation__list account-navigation-list">
      <li
        v-for="(section, index) in sections"
        :key="index"
        class="account-navigation-list__item">
        <button
          :class="{'account-navigation__btn--active': index === currentSection}"
          class="account-navigation__btn"
          @click="navChangeHandler(index)">
          {{ section }}
        </button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'VAccountNavigation',
  props: {
    sections: {
      type: Array,
      required: true,
      validator: value => value.length > 0
    },
    activeSection: {
      type: Number,
      required: false,
      default: 0
    }
  },

  data() {
    return {
      currentSection: this.activeSection
    }
  },

  methods: {
    navChangeHandler(sectionIndex) {
      this.currentSection = sectionIndex
      this.$emit('onAccountNavChange', this.currentSection)
    }
  }
}
</script>
