<template>
  <div class="account">
    <vAccountHeader
      :name="userName"
      :image="imageUrl"
      :role="role"
      class="account__header account-header"/>
    <div class="account__body">
      <vAccountNavigation
        :sections="sections"
        class="account__navigation account-navigation"/>
      <div>
        BODY
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import vAccountHeader from './components/vAccountHeader.vue'
import vAccountNavigation from './components/vAccountNavigation.vue'

export default {
  name: 'AccountPage',
  components: {
    vAccountHeader,
    vAccountNavigation
  },

  data() {
    return {
      isLoading: false, // TODO
      sections: ['management', 'privacy', 'settings'],

      email: '',
      role: '',
      profile: null
    }
  },

  computed: {
    userName: function () {
      return this.profile ? `${this.profile.user.first_name} ${this.profile.user.last_name}` : ''
    },
    imageUrl: function () {
      return this.profile ? this.profile.image_url : ''
    }
  },

  created() {
    let token = localStorage.getItem('token');
    axios.defaults.headers.common['Authorization'] = `Token ${token}`

    this.getCurrentUserDetails()
  },

  methods: {
    getCurrentUserDetails() {
      axios.get('/api/current-user-details')
        .then(result => {
          let data = result.data
          this.email = data.email
          this.role = data.role
          this.profile = data.profile
        }).catch(error => {
          console.log(error)
        })
    }
  }
}
</script>