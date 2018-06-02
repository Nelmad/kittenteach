<template lang="html">
  <li class="subjects-list-item">
    <a :href="subject.url">
      <div
        :style="`background-image: url(${imageSrc})`"
        class="subjects-list-item__text">
        {{ subject.name }}
      </div>
    </a>
  </li>
</template>

<script>
export default {
  name: 'VSubjectBlock',
  props: {
    subject: {
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
      imageSrc: this.subject.image_url || this.defaultImg,
    }
  }
}
</script>