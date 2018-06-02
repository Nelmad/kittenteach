<template lang="html">
  <li class="teachers-list-item">
    <a :href="teacher.url">
      <div class="teachers-list-item__content">
        <img
          :src="defaultImg"
          alt="Teacher picture"
        >
      </div>
      <div class="teachers-list-item__description">
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
  }
}
</script>