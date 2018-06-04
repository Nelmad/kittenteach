<template lang="html">
  <li class="schools-list-item">
    <a :href="school.url">
      <div class="schools-list-item__description">
        <div class="schools-list-item__title">{{ school.name }}</div>
        <div class="schools-list-item__text">Rating:
          <FontAwesomeIcon
            v-for="index in school.rating"
            :key="index"
            class="schools-list-item__rating"
            icon="star"/>
        </div>
        <div
          v-if="school.address"
          class="schools-list-item__text">
          Address:
          <a
            :href="`https://www.google.ru/maps/search/${school.address}`"
            target="_blank"
            @click.prevent="schoolAddressHandler">
            {{ school.address }}
          </a>
        </div>
      </div>
      <img
        :src="imageSrc"
        class="schools-list-item__image"
        alt="School picture"
      >
    </a>
  </li>
</template>

<script>
import fontawesome from '@fortawesome/fontawesome'
import faStar from '@fortawesome/fontawesome-free-solid/faStar'
import FontAwesomeIcon from '@fortawesome/vue-fontawesome'

fontawesome.library.add(faStar);

export default {
  name: 'VSchoolBlock',
  components: {
    FontAwesomeIcon
  },
  props: {
    school: {
      type: Object,
      required: true
    },
    defaultImg: {
      type: String,
      required: true
    }
  },

  data() {
    return {
      imageSrc: this.school.image_url || this.defaultImg,
    }
  },

  methods: {
    schoolAddressHandler() {
      this.$eventBus.$emit('onUrl', `https://maps.google.com/maps?q=${encodeURIComponent(this.school.address)}&output=embed`)
    }
  }
}
</script>