<template>
    <div class = "container">
        <Nav_bar></Nav_bar>
        <div  class= "container">
            <h1 style="margin-top:90px" class="title_2">Search results for "{{this.user_name}}"</h1>
            <div class="container w-50 cardbox">
                <div class="column list-group ">
                <li v-for="user in users" :key="user.id" class = "list-group-item list-group-mine">
                <div class="profile-card">
                <div class="imagebox">
                    <img id="profile-picture" v-bind:src=user.profile_pic>
                </div>
                <div class="user-info">
                    <p class="user-name" style = "line-height: 23px; font-weight: bold;">{{ user.f_name }} {{ user.l_name }}</p>
                    <div>
                        <div class ="location-area">
                            <img id ="location-image" src="../assets/location_on-24px@2x.png">
                            <p style="margin-top : 0.2rem;font-size: 13px;line-height: 14px; color: lightgray">{{ user.location }}</p>
                        </div>
                    </div>
                </div>
                <div class = "button">
                    <button id = "button" type="button" class="btn btn-success" @click="toProfile(user.id)">Profile</button>
                </div>
            </li>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
// eslint-disable-next-line camelcase
import Nav_bar from './Nav_bar.vue'
import axios from 'axios'

export default{
  components: {
    'Nav_bar': Nav_bar
  },
  data () {
    return {
      users: null,
      user_name: ''
    }
  },
  created () {
    this.user_name = this.$route.params.srch
    var fd1 = new FormData()
    fd1.append('user', this.user_name)
    axios.post('http://localhost:5000/searchUser', fd1).then((res) => {
      this.users = res.data.users
    })
  },
  methods: {
    toProfile (id) {
      this.$router.push('/profile/' + id)
    }
  }
}
</script>
<style scoped>
body {
    margin-bottom: 60px;

}

main {
  padding-top: 60px;

}

footer {
  position: inherit;
  margin-left: 0 !important;
  bottom: 0;
  width: 100%;
  height: 60px;
  line-height: 60px;
  background-color: #f5f5f5;

}
.profile-card{
  width: 100%;
  height: 10em;

  display: flex;
  flex-direction: row;
  box-shadow: 1px 1px 1px 1px #dadada;
  border-radius: 3px;
  border: 2px solid rgb(231, 228, 228);
  border-top: 4px solid blue;
}

.imagebox, .user-info, .button{
  height: 100%;
  width: 30%;
  margin: auto;
  display: flex;
}

.user-info {
  display: flex;
  flex-direction: column;

  line-height: 10px;
}

.user-info > p{
  vertical-align: middle;
}

.user-name{
  margin-top: 2.5rem;
}
.gender-area,.location-area{
  display: flex;
  flex-direction: row;

}
#gender-image, #location-image{
  height: 15%;
  width: 15%;
  margin-right: 0.2rem;
}

#profile-picture{
  margin: auto;
  height: 50%;
  border: 1px solid none;
  border-radius: 200px;
}

#button{
  height: 20%;
  width: 75%;
  margin: auto;
  line-height: 1px;

}

.list-group-mine .list-group-item {
  background-color: #f1f9fb;
  border-top: 1px solid #0091b5;
  border-left-color: #fff;
  border-right-color: #fff;
}

.list-group-mine .list-group-item:hover {
  background-color: red;
}

.card-form {
  box-shadow: 1px 1px 1px 1px #dadada;
  border-radius: 3px;
  border: 2px solid rgb(231, 228, 228);
  /* height: 20rem; */
}

.detailed-profile {
  max-width: 75%;
}

.profile-desc {
  color: #8f8c8c;
  font-weight: 500;
}

.bg-primary{
  background-color: rgb(74, 144, 226) !important;
}

.view-p-btn {
  background-color: #11d03d;
  border-color: #11d03d;
}

.small-pic{
  max-width: 100%;
  max-height: 100%;
}

.profile-cmnds {
  display: flex;
  justify-content: space-around;
}

.profile-cmnds > .btn {
  width: 15rem;
}

#bio {
  margin-top: 1.2rem;
}

i {
  margin-right: 0.5rem;
}
li {
    border-top: none;
    border:none;
}

.card-form {
  border-top: 0.5rem solid rgb(74, 144, 226);
  /* height: 20rem; */
}
</style>
