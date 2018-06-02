<template lang="html">
  <li class="teachers-list-item">
    <a :href="teacher.url">
      <div class="teachers-list-item__content">
        <img
          :src="imageSrc"
          :class="`teachers-list-item__image teachers-list-item__image--${imageType}`"
          alt="Teacher picture"
        >
      </div>
      <div
        :style="{color: descriptionColor}"
        class="teachers-list-item__description">
        {{ teacher.user.first_name }} {{ teacher.user.last_name }}
      </div>
    </a>
  </li>
</template>

<script>
export default {
  name: 'VTeacherBlock',
  props: {
    teacher: {
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
      imageSrc: this.teacher.image_url || this.defaultImg,
      imageType: this.teacher.image_url ? 'custom' : 'default',
      descriptionColor: this.teacher.image_url ? '#FFFFFF' : '#797979'
    }
  }
}
</script>