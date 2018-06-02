<template>
  <div style="min-height: 568px">

    <div class="teachers teachers--popular">
      <div class="teachers__title-block teachers-title-block teachers-title-block--primary">
        <span class="teachers-title-block__text">
          The Most Popular Teachers
        </span>
      </div>

      <ul class="teachers__list teachers-list">
        <li
          is="vTeacherBlock"
          v-for="teacher in popularTeachers"
          :key="teacher.url"
          :teacher="teacher"
          :default-img="`${staticUrl}core/img/portrait/teacher-portrait.svg`"
          class="teachers-list__item teachers-list-item">
          {{ teacher.user.first_name }} {{ teacher.user.last_name }}
        </li>
      </ul>

      <div class="spinner-wrapper">
        <vLoad
          v-if="popularTeachersLoading"
          color="v-gray"/>
      </div>
    </div>

    <div class="teachers">
      <div class="teachers__title-block teachers-title-block">
        <span class="teachers-title-block__text">
          Choose your Teacher and Get Started
        </span>
      </div>

      <ul class="teachers__list teachers-list">
        <li
          is="vTeacherBlock"
          v-for="teacher in teachers"
          :key="teacher.url"
          :teacher="teacher"
          :default-img="`${staticUrl}core/img/portrait/teacher-portrait.svg`"
          class="teachers-list__item">
          {{ teacher.user.first_name }} {{ teacher.user.last_name }}
        </li>
      </ul>

      <div class="spinner-wrapper">
        <vLoad
          v-show="teachersLoading"
          color="v-gray"/>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'
import vTeacherBlock from './components/vTeacherBlock.vue'
import vLoad from './components/vLoad.vue'

export default {
  name: 'TeachersPage',
  components: {
    vTeacherBlock,
    vLoad
  },

  data() {
    return {
      staticUrl: window.static,
      popularTeachersLoading: true,
      teachersLoading: true,

      popularTeachers: [],
      teachers: [],

      params: {
        limit: 20,
        offset: 0
      }
    }
  },

  created() {
    this.fetchPopularTeachers()
    this.fetchTeachers()
  },

  methods: {
    fetchPopularTeachers() {
      // TODO fetch popular teachers
      this.popularTeachersLoading = true
      let params = {
        limit: 3,
        offset: 5
      }

      axios.get('/api/teachers', {
        params: params
      }).then(result => {
        this.popularTeachers = result.data.results
        this.popularTeachersLoading = false
      }).catch(error => {
        console.log(error)
        this.popularTeachersLoading = false
      })
    },

    fetchTeachers() {
      this.teachersLoading = true

      axios.get('/api/teachers', {
        params: this.params
      }).then(result => {
        this.teachers = this.teachers.concat(result.data.results)
        this.teachersLoading = false
      }).catch(error => {
        console.log(error)
        this.teachersLoading = false
      })
    },

    loadMore() {
      this.params.offset += this.params.limit
      this.fetchTeachers()
    }
  }
}
</script>