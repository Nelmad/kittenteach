<template lang="html">
  <li class="schools-list-item">
    <a :href="school.url">
      <img
        :src="imageSrc"
        alt="School picture"
      >
      <!--<div class="schools-list-item__image"/>-->
      <div class="schools-list-item__text-container">
        <span class="schools-list-item__text">{{ school.name }}</span>
      </div>
    </a>
  </li>
</template>

<script>
export default {
  name: 'VSchoolBlock',
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
  }
}
</script>