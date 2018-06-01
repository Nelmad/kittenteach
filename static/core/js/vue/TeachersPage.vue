<template>
  <div>
    Teachers
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'TeachersPage',

  data() {
    return {
      params: {
        isLoading: false,
        limit: 20,
        offset: 0
      }
    }
  },

  created() {

  },

  methods: {
    fetchTeachers() {
      axios.get('/api/teachers', {
        params: this.params
      }).then(result => {
        console.log(result)
      }).catch(error => {
        console.log(error)
      })
    }
  }
}
</script>