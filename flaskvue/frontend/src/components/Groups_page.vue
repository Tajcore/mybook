<template>
<div class="container">
    <nav_bar></nav_bar>
    <div class = "container">
        <div class = "row">
            <div class = "col mt-5">
                <h3 style = "margin-right:20px">Groups on MyBook</h3>
                <div style = "margin-left:350px" class="row">
                        <div v-for="group in groups" :key="group.group_id" class="col-md-4 mb-5">
                            <div class="card-body">
                                <h5 class="card-title">{{group.group_name}}</h5>
                                <p class="card-text">Group By {{ group.creator_name }}</p>
                                <p class="card-text">Members: <span style = "color:green;">{{ group.members_count}}</span></p>
                                <a @click="toGroup(group.group_id)" class="btn btn-primary">Check out this group</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
// eslint-disable-next-line camelcase
import Nav_bar from './Nav_bar.vue'
// eslint-disable-next-line no-unused-vars
import axios from 'axios'

export default {
  components: {
    'Nav_bar': Nav_bar
  },
  data () {
    return {
      groups: []
    }
  },
  mounted () {
    axios.get('http://localhost:5000/users/groups').then((res) => {
      this.groups = res.data.groups
    })
  },

  methods: {
    toGroup (id) {
      this.$router.push({name: 'Group', params: {group_id: id}})
    }
  }
}

</script>
