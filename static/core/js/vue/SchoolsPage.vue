<template>
  <div
    class="schools"
    style="min-height: 568px">

    <div class="schools__search schools-search">
      <h2 class="schools-search__title">Let's find School for you!</h2>
      <input
        :placeholder="gettext('Write to search here...')"
        v-model="params.search"
        class="schools-search__input"
        type="text">
    </div>

    <ul
      v-show="schools.length > 0 || isLoading"
      class="schools__list schools-list">
      <li
        is="vSchoolBlock"
        v-for="school in schools"
        :key="school.url"
        :school="school"
        :default-img="getRandomImage()"
        class="schools-list__item schools-list-item">
        {{ school.name }}
      </li>
    </ul>

    <div
      v-show="isLoading"
      class="spinner-wrapper">
      <vLoad color="v-gray"/>
    </div>

    <div
      v-show="schools.length === 0 && !isLoading"
      class="schools__empty-list schools-empty-list">
      <h2 class="schools-empty-list__title">\(^Д^)/</h2>
      <p class="schools-empty-list__description">
        No Schools Found...
      </p>
    </div>

    <button
      v-if="loadMoreBtnShow && !isLoading"
      class="schools__btn schools__btn--center"
      @click="loadMore">
      Load More
    </button>

  </div>
</template>

<script>
import axios from 'axios'
import { getRandomInt } from './utils.js'
import vSchoolBlock from './components/vSchoolBlock.vue'
import vLoad from './components/vLoad.vue'

export default {
  name: 'SchoolsPage',
  components: {
    vSchoolBlock,
    vLoad
  },

  data() {
    return {
      isLoading: true,
      loadMoreBtnShow: true,

      schools: [],
      defaultImages: [
        'images/temp/schools/school-1.svg',
        'images/temp/schools/school-2.svg',
        'images/temp/schools/school-3.svg',
        'images/temp/schools/school-4.svg',
        'images/temp/schools/school-5.svg',
      ],

      params: {
        search: '',
        limit: 6,
        offset: 0
      }
    }
  },

  computed: {
    imagesToChoose: function () {
      return this.defaultImages.slice()
    }
  },

  watch: {
    'params.search': function () {
      this.schools.length = 0
      this.params.limit = 6
      this.params.offset = 0
      this.fetchSchools()
    }
  },

  created() {
    // this.imagesToChoose = this.defaultImages.slice();
    this.fetchSchools()
  },

  methods: {
    fetchSchools() {
      this.isLoading = true

      axios.get('/api/schools', {
        params: this.params
      }).then(result => {
        this.schools = result.data.results
        this.isLoading = false
        this.loadMoreBtnShow = !!result.data.next
      }).catch(error => {
        console.log(error)
        this.isLoading = false
      })
    },

    loadMore() {
      this.params.offset += this.params.limit
      this.fetchSchools()
    },

    getRandomImage() {
      if (this.imagesToChoose.length === 0) { // reset
        this.imagesToChoose = this.defaultImages.slice();
      }

      let index = getRandomInt(0, this.imagesToChoose.length)
      let imagePath = this.imagesToChoose.splice(index, 1)[0];

      return this.staticUrl + imagePath
    }
  }
}
</script>