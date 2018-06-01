<template lang="html">
  <li>
    <a
      :href="teacher.url"
      class="teachers__block">
      {{ teacher.user.first_name }}
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
    }
  }
}
</script>