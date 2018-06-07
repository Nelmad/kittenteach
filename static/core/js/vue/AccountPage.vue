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
        v-if="!scheduleLoading"
        :time-ground="timeGround"
        :week-ground="['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']"
        :color="scheduleColors"
        :task-detail="displaySchedule"/>

      <div
        v-else
        style="margin-top: 50px;"
        class="spinner-wrapper">
        <vLoad color="v-brown"/>
      </div>

    </div>
  </div>
</template>

<script>
import axios from 'axios'
import vAccountHeader from './components/vAccountHeader.vue'
import vAccountNavigation from './components/vAccountNavigation.vue'
import vLoad from './components/vLoad.vue'

export default {
  name: 'AccountPage',
  components: {
    vAccountHeader,
    vAccountNavigation,
    vLoad
  },

  data() {
    return {
      isLoading: false, // TODO
      sections: ['schedule', 'settings'],
      schedule: [],

      email: '',
      role: '',
      profile: null,

      scheduleLoading: true,
      timeGroundObj: [10, 13],
      displaySchedule: [[], [], [], [], []],
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
    timeGround: function () {
      return this.timeGroundObj.map(item => `${item}:00`)
    },

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

    this.getSchedule().then(() => {
      this.schedule.forEach(value => {
        let group = value.group

        let time = value.time
        let timeDelIndex = time.indexOf(':')

        if (timeDelIndex === -1) {
          return true
        }
        let startHours = parseInt(time.slice(0, timeDelIndex))
        let endHours = startHours + 1

        if (startHours < this.timeGroundObj[0]) {
          this.timeGroundObj[0] = startHours
        }

        if (endHours > this.timeGroundObj[1]) {
          this.timeGroundObj[1] = endHours + 1
        }

        let dateStart = time.slice(0, time.lastIndexOf(':'))
        let dateEnd = endHours + time.slice(timeDelIndex, time.lastIndexOf(':'))

        let detail = 'Students: ' + group.students.map((item) => {
          return item.user.first_name + ' ' + item.user.last_name
        }).join(', ')

        let displayScheduleItem = {
          dateStart: dateStart,
          dateEnd: dateEnd,
          title: `${group.name} [${group.subject.name}]`,
          detail: detail
        }

        this.displaySchedule[value.weekday].push(displayScheduleItem)
      })
      this.scheduleLoading = false
    })
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