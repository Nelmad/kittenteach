<template lang="html">
  <li class="teachers-list-item">
    <a :href="teacher.url">
      link
    </a>
    <div class="teachers-list-item__description">
      {{ teacher.user.first_name }} {{ teacher.user.last_name }}
    </div>
  </li>
</template>

<script>
export default {
  name: 'VTeacherBlock',
  props: {
    teacher: {
      type: Object,
      required: true
    }
  }
}
</script>