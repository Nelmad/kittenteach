<template>
  <div
    class="schools"
    style="min-height: 568px">

    <div class="schools__search schools-search">
      <h2 class="schools-search__title">Let's find School for you!</h2>
      <input
        :placeholder="gettext('Write to search here...')"
        :value="params.search"
        class="schools-search__input"
        type="text"
        @input="$event.target.value == '' && (params.search = $event.target.value)"
        @keyup.enter="params.search = $event.target.value">
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

    <div
      v-show="iframeSrc"
      class="schools__map-modal schools-map-modal"
      @click="closeMapModal">
      <vLoad
        v-show="isIframeLoading || iframeSrc === ''"
        class="schools-map-modal__spinner"
        color="#005C5F"/>

      <iframe
        :src="iframeSrc"
        frameborder="0"
        @load="isIframeLoading = false"/>
    </div>

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

      isIframeLoading: true,
      iframeSrc: '',

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
    imagesToChoose: {
      get: function() {
        return this.defaultImages.slice()
      },
      set: function (newValue) {
        this.defaultImages = newValue;
      }
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
    this.$eventBus.$on('onUrl', (url) => {
      this.iframeSrc = url
    })
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
    },

    closeMapModal() {
      this.iframeSrc = ''
      this.isIframeLoading = true
    }
  }
}
</script>