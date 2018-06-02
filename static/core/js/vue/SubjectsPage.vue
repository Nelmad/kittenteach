<template>
  <div style="min-height: 568px">

    <ul class="teachers__list teachers-list">
      <li
        is="vSubjectBlock"
        v-for="subject in subjects"
        :key="subject.url"
        :subject="subject"
        :default-img="`${staticUrl}test`"
        class="teachers-list__item teachers-list-item">
        {{ subject.name }}
      </li>
    </ul>

    <div
      v-show="isLoading"
      class="spinner-wrapper">
      <vLoad color="v-gray"/>
    </div>

  </div>
</template>

<script>
import axios from 'axios'
import vSubjectBlock from './components/vSubjectBlock.vue'
import vLoad from './components/vLoad.vue'

export default {
  name: 'SubjectsPage',
  components: {
    vSubjectBlock,
    vLoad
  },

  data() {
    return {
      isLoading: true,

      subjects: [],
      params: {
        limit: 20,
        offset: 0
      }
    }
  },

  created() {
    this.fetchSubjects()
  },

  methods: {
    fetchSubjects() {
      this.isLoading = true

      axios.get('/api/subjects', {
        params: this.params
      }).then(result => {
        this.subjects = result.data.results
        this.isLoading = false
      }).catch(error => {
        console.log(error)
        this.isLoading = false
      })
    }
  }
}
</script>