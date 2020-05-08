<template>

<nav  class="navbar navbar-expand-lg navbar-default fixed-top navbar-light bg-success">
  <a class="navbar-brand ml-2" href="#">
  <div class = "container" style = "background-color:white" >
    <span style = "color:#0E9F35;font-size:32px;font-weight:bold">M</span>
    </div>
  </a>
  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <form class="form-inline my-2 my-lg-0 mr-auto">
      <div class = "row lg-6 no-gutters ">
        <div class = "col d-flex" >
          <ejs-autocomplete id='employees'  v-model:='value' popupHeight:='height' :popupWidth='width'  :dataSource='users' :fields='fields' :placeholder='waterMark' :sortOrder='sortOrder' :itemTemplate='iTemplate' popupHeight="450px"></ejs-autocomplete>
        </div>
        <div style = "width:50px;height:50px">
            <img @click="toProfile_Search" style = "height:100%;width:auto%;" src = "../assets/search-24px.png">
        </div>
    </form>
    <ul style = "align-items:center;margin-right:auto" class="navbar-nav d-inline-flex">
      <li class="nav-item mr-5" >
        <div class = "d-inline-flex p-2">
            <button @click="toProfile(id)" style = "height:50px;font-weight:bold;color:white" class="btn btn-success btn-outline-white nav-link" >
              <div class = "mb-5 d-flex flex-row-reverse ">
                <span style = "margin-top:3px;" class = "ml-2">{{ first_name }}</span>
                <img v-bind:src=profile_pic style = "height:40px;width:40px;border: 1px solid none;border-radius:40px">
              </div>
            </button>
        </div>
      </li>
      <li class="nav-item mr-5">
        <router-link to="/home">
          <button style = "font-weight:bold;color:white" class="btn btn-success btn-outline-white nav-link" >Home</button>
        </router-link>
      </li>
     <b-dropdown id="dropdown-1"  variant ="success" no-caret  class="nav item mr-5 ">
       <template v-slot:button-content>
         <Strong>Create</Strong>
       </template>
    <b-dropdown-item>
      <div style = "align-items:center" class = "row d-flex-inline">
        <img class = "ml-2 mr-2" style = "height:16px; width:auto" src = "../assets/flag.png">
        <strong class = "">Page</strong>
      </div>
      <div style = "align-items:center" class = "row d-flex-inline">
        <strong style = "margin-left:28px; color:#A29B9B">Connect and share with customers or fans</strong>
      </div>
    </b-dropdown-item>
    <b-dropdown-divider></b-dropdown-divider>
    <b-dropdown-item>
      <div style = "align-items:center" class = "row d-flex-inline">
        <img class = "ml-2 mr-2" style = "height:16px; width:auto" src = "../assets/Component 4 – 1.png">
        <strong class = "">Ad</strong>
      </div>
      <div style = "align-items:center" class = "row d-flex-inline">
        <strong  style = "margin-left:33px;color:#A29B9B">Advertise your business or organization</strong>
      </div>
    </b-dropdown-item>
    <b-dropdown-divider></b-dropdown-divider>
       <b-dropdown-item v-b-modal.modal-no-backdrop>
      <div style = "align-items:center" class = "row d-flex-inline">
        <img class = "ml-2 mr-2" style = "height:16px; width:auto" src = "../assets/team.png">
        <strong class = "">Group</strong>
      </div>
      <div style = "align-items:center" class = "row d-flex-inline">
        <strong  style = "margin-left:37px;color:#A29B9B">Find people with shared interests</strong>
      </div>
    </b-dropdown-item>
    <b-dropdown-divider></b-dropdown-divider>
       <b-dropdown-item>
      <div style = "align-items:center" class = "row d-flex-inline">
        <img class = "ml-2 mr-2" style = "height:16px; width:auto" src = "../assets/event_note-24px-black.png">
        <strong class = "">Event</strong>
      </div>
      <div style = "align-items:center" class = "row d-flex-inline">
        <strong  style = "margin-left:33px;color:#A29B9B">Bring people together with events</strong>
      </div>
    </b-dropdown-item>
  </b-dropdown>
     <li class="nav-item mr-5">
        <router-link to="/groups">
          <button style = "font-weight:bold;color:white" class="btn btn-success btn-outline-white nav-link" >Groups</button>
        </router-link>
      </li>
    </ul>
  </div>
  <div>
  <b-modal cancel-disabled ok-disabled id="modal-no-backdrop" hide-backdrop content-class="shadow" title="Create New Group">
    <div class = "container">
      <div class = "row">
        <div class = "container" style = "border:1px solid lightgray">
        <div class = "row">
          <div class = "w-30">
            <img class = "img-fluid" src = "../assets/Component 3 – 1.png">
          </div>
          <div class = "col d-flex">
            <p class = "mt-3"  style = "color:gray;font-size:12px">Groups are great for getting things done and staying in touch with just the people you want. Share photos and videos, have conversations, make plans and more.</p>
          </div>
        </div>
        </div>
      </div>
      <div class = "row d-flex flex-column">
        <h5 class = "mt-3">Name your group</h5>
        <form>
          <input v-model="group_name" type = "text" class = "form-control" placeholder="Group name here">
        </form>
      </div>
    </div>
  <template v-slot:modal-footer="{cancel}">
          <b-button size="sm" variant="success" @click="create()">
            Create
          </b-button>
            <b-button size="sm" variant="danger" @click="cancel()">
              Cancel
            </b-button>
        </template>
  </b-modal>
</div>
</nav>
</template>

<script>
import EventBus from './EventBus'
import jwtDecode from 'jwt-decode'
import axios from 'axios'
import Vue from 'vue'
import { AutoCompletePlugin } from '@syncfusion/ej2-vue-dropdowns'

Vue.use(AutoCompletePlugin)

EventBus.$on('logged-in', test => {

})

var itemVue = Vue.component('itemTemplate', {
  template: `<div class = "d-flex flex-row"> 
    <img style = "height:30px; width:auto" class = "img ml-2 mb-1 mt-2 mr-1" :src='data.profile_pic'>
    <div>
      <span style = "Font-weight:bold;color:gray" class = "mr-5" >{{data.name}}</span>
    </div>
    <hr>
  </div>
  `,
  data () {
    return {
      data: {}
    }
  }
})
export default {
  data () {
    const token = localStorage.usertoken
    const decoded = jwtDecode(token)
    return {
      width: '270px',
      height: '300px',
      profile_pic: decoded.identity.profile_pic,
      first_name: decoded.identity.first_name,
      last_name: decoded.identity.last_name,
      id: decoded.identity.id,
      auth: '',
      user: '',
      users: [],
      value: null,
      waterMark: 'Find user',
      sortOrder: 'Ascending',
      fields: {value: 'name'},
      iTemplate: function (e) {
        return {
          template: itemVue
        }
      }}
  },
  methods: {
    create () {
      var fd = new FormData()
      fd.append('group_name', this.group_name)
      fd.append('user_id', this.id)
      axios.post('http://localhost:5000/users/groups', fd).then((res) => {
        this.flashMessage.success({title: 'New Group Created', message: 'Check out your group page!'})
      }).catch((err) => {
        // eslint-disable-next-line eqeqeq
        if (err.name != 'NavigationDuplicated') {
          this.flashMessage.error({title: err.name, message: err.message})
          throw err
        }
      })
    },
    logout () {
      localStorage.removeItem('usertoken')
    },
    toProfile (id) {
      this.$router.push({name: 'Profile', params: {user_id: id}})
    },
    toProfile_Search () {
      var keyword = document.getElementById('employees_hidden').value
      var id = this.getID(keyword)
      this.toProfile(id)
    },
    getID (string) {
      var arr = string.split(' ')
      return arr[2]
    }
  },
  mounted () {
    console.log(document.getElementById('employees_hidden').value)
    EventBus.$on('logged-in', status => {
      this.auth = status
    })
    axios.get('http://localhost:5000/users').then((res) => {
      this.users = res.data.users
    })
  }
}

</script>
<style>
@import "../../node_modules/@syncfusion/ej2-base/styles/material.css";
@import "../../node_modules/@syncfusion/ej2-inputs/styles/material.css";
@import "../../node_modules/@syncfusion/ej2-vue-dropdowns/styles/material.css";
</style>
