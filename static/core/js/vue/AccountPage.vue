<template>
  <div class="account">
    <vAccountHeader
      :name="userName"
      :image="imageUrl"
      :role="role"
      class="account__header account-header"/>
    <vAccountNavigation
      :sections="sections"
      class="account__navigation account-navigation"/>
    <div class="account__body">
      <Schedule
        :time-ground="['09:00', '18:00']"
        :week-ground="['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']"
        :color="scheduleColors"
        :task-detail="taskDetail"/>
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
      sections: ['schedule', 'settings'],
      schedule: [],

      email: '',
      role: '',
      profile: null,

      taskDetail: [
        [
          {
            dateStart: '09:30',
            dateEnd: '10:30',
            title: 'Metting',
            detail: 'Metting (German: Mettingen) is a commune in the Moselle department in Grand Est in north-eastern France.'
          },
          {
            dateStart: '11:30',
            dateEnd: '13:50',
            title: 'Metting',
            detail: 'Metting (German: Mettingen) is a commune in the Moselle department in Grand Est in north-eastern France.'
          }

        ],
        [
          {
            dateStart: '10:30',
            dateEnd: '12:00',
            title: 'Metting',
          },
          {
            dateStart: '12:30',
            dateEnd: '14:50',
            title: 'Metting',
          }

        ],
        [
          {
            dateStart: '12:30',
            dateEnd: '13:30',
            title: 'Metting',
          },
          {
            dateStart: '15:30',
            dateEnd: '16:50',
            title: 'Metting',
          }

        ],
        [
          {
            dateStart: '09:50',
            dateEnd: '10:50',
            title: 'Metting',
          },
          {
            dateStart: '11:30',
            dateEnd: '13:50',
            title: 'Metting',
          }

        ],
        [
          {
            dateStart: '12:30',
            dateEnd: '13:30',
            title: 'Metting',
          },
          {
            dateStart: '14:30',
            dateEnd: '15:50',
            title: 'Metting',
          }
        ]],
      scheduleColors: [
        '#d7a53b',
        '#765d46',
        '#6eb2c1',
        '#69986d',
        '#c1505a',
        '#4ca296',
        '#8281b7',
      ]
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

    this.getCurrentUserDetails().then(() => {
      let item = this.role === 'teacher' ? 'my students': 'my teachers'
      let index = 1
      this.sections.splice(index, 0, item)
    })

    this.getSchedule()
  },

  methods: {
    async getCurrentUserDetails() {
      await axios.get('/api/current-user-details')
        .then(result => {
          let data = result.data
          this.email = data.email
          this.role = data.role
          this.profile = data.profile
        }).catch(error => {
          console.log(error)
        })
    },

    async getSchedule() {
      await axios.get('/api/teachers/lessons-templates')
        .then(result => {
          // TODO schedule load logic
          let data = result.data
          this.schedule = data.results

        }).catch(error => {
          console.log(error)
        })
    }
  }
}
</script>