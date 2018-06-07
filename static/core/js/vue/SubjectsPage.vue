<template>
  <div
    class="subjects"
    style="min-height: 568px">

    <div class="subjects__search subjects-search">
      <h2 class="subjects-search__title">What Subject are you Looking for...?</h2>
      <input
        :placeholder="gettext('Write to search here...')"
        :value="params.search"
        class="subjects-search__input"
        type="text"
        @input="$event.target.value == '' && (params.search = $event.target.value)"
        @keyup.enter="params.search = $event.target.value">
    </div>

    <ul
      v-show="subjects.length > 0 || isLoading"
      class="subjects__list subjects-list">
      <li
        is="vSubjectBlock"
        v-for="subject in subjects"
        :key="subject.url"
        :subject="subject"
        :default-img="`${staticUrl}images/temp/subjects/default.jpg`"
        class="subjects-list__item subjects-list-item">
        {{ subject.name }}
      </li>
    </ul>

    <div
      v-show="isLoading"
      class="spinner-wrapper">
      <vLoad color="v-gray"/>
    </div>

    <div
      v-show="subjects.length === 0 && !isLoading"
      class="subjects__empty-list subjects-empty-list">
      <h2 class="subjects-empty-list__title">(>_&lt;)</h2>
      <p class="subjects-empty-list__description">
        No Subjects Found...
      </p>
    </div>

    <button
      v-if="loadMoreBtnShow && !isLoading"
      class="subjects__btn subjects__btn--center"
      @click="loadMore">
      Load More
    </button>

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
      loadMoreBtnShow: true,

      subjects: [],

      params: {
        search: '',
        limit: 6,
        offset: 0
      }
    }
  },

  watch: {
    'params.search': function () {
      this.subjects.length = 0
      this.params.limit = 6
      this.params.offset = 0
      this.fetchSubjects()
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
        this.loadMoreBtnShow = !!result.data.next
      }).catch(error => {
        console.log(error)
        this.isLoading = false
      })
    },

    loadMore() {
      this.params.offset += this.params.limit
      this.fetchSubjects()
    }
  }
}
</script>