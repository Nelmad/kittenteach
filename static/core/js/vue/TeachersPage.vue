<template>
  <div
    class="teachers"
    style="min-height: 568px">

    <div class="teachers teachers--popular">
      <div class="teachers__title-block teachers-title-block teachers-title-block--primary">
        <span class="teachers-title-block__text">
          The Most Popular Teachers
        </span>
      </div>

      <ul
        v-show="popularTeachers.length > 0 || popularTeachersLoading"
        class="teachers__list teachers-list">
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

      <div
        v-if="popularTeachersLoading"
        class="spinner-wrapper">
        <vLoad color="v-gray"/>
      </div>

      <div
        v-show="popularTeachers.length === 0 && !popularTeachersLoading"
        class="teachers__empty-list teachers-empty-list">
        <h2 class="teachers-empty-list__title"> (>_&lt;) </h2>
        <p class="teachers-empty-list__description">No Popular Teachers Found...</p>
      </div>
    </div>

    <div class="teachers__search teachers-search">
      <h2 class="teachers-search__title">Find Teacher as Quick as Possible!</h2>
      <input
        v-model="params.search"
        class="teachers-search__input"
        type="text">
    </div>

    <div class="teachers">
      <div class="teachers__title-block teachers-title-block">
        <span class="teachers-title-block__text">
          Choose your Teacher and Get Started
        </span>
      </div>

      <ul
        v-show="teachers.length > 0 || teachersLoading"
        class="teachers__list teachers-list">
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

      <div
        v-show="teachers.length === 0 && !teachersLoading"
        class="teachers__empty-list teachers-empty-list">
        <h2 class="teachers-empty-list__title"> (>_&lt;) </h2>
        <p class="teachers-empty-list__description">No Teachers Found...</p>
      </div>

      <div
        v-show="teachersLoading"
        class="spinner-wrapper">
        <vLoad color="v-gray"/>
      </div>
    </div>

    <button
      v-if="loadMoreBtnShow && !teachersLoading"
      class="teachers__btn teachers__btn--center"
      @click="loadMore">
      Load More
    </button>

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
      popularTeachersLoading: true,
      teachersLoading: true,
      loadMoreBtnShow: true,

      popularTeachers: [],
      teachers: [],

      params: {
        search: '',
        limit: 6,
        offset: 0
      }
    }
  },

  watch: {
    'params.search': function () {
      this.teachers.length = 0
      this.params.limit = 6
      this.params.offset = 0
      this.fetchTeachers()
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
        this.loadMoreBtnShow = !!result.data.next
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