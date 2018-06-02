<template lang="html">
  <li class="teachers-list-item">
    <a :href="subject.url">
      SUBJECT
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
  }
}
</script>