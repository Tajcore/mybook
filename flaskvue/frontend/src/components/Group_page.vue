<template>
<div class = "container">
    <nav_bar></nav_bar>
    <div class = "container" style="margin-top:7%">
        <div class = "row" style = "border:5px solid 28a745;height:200px;background-color:black">
            <div class = " align-self-end col d-flex flex-row align-items-center justify-content-center">
                <h1 style="color:white;margin-bottom:85px">{{group.group_name}}</h1>
                <button  v-show="member_status === 1" style = "align-self:flex-end;height:40px;width:140px;" class = "align-self-end btn btn-success">
                   <span style ="color:white">Member</span>
                </button>
                <button  @click="joinGroup" v-show="member_status === null" style = "align-self:flex-end;height:40px;width:140px;" class = "align-self-end btn btn-danger">
                   <span style ="color:white">Join Group</span>
                </button>
            </div>
        </div>
        <div class = "col d-flex flex-column">
        <div class = "row">
        <div class = "col">
          <div v-show="group.created_by === user_id" class = "card mt-4 " style="width:70%">
            <div class = "card-body">
                <form v-on:submit.prevent="postSubmit" enctype="multipart/form-data">
                  <textarea v-model = "posting_msg" name = "posting_msg" class = "form-control form-control-lg" placeholder="Start a post..." rows = 3></textarea>
                   <div class = "row">
                     <div class = "col d-flex d-flex-row-reverse " style = "vertical-align:center">
                       <div class = "mt-3 mr-3" style = "width:58.02px;height:56px">
                      <button  class = "btn btn-outline-success btn-block" type="submit" style = "margin-top:12px">Post</button>
                       </div>
                      <div class = "file-input mt-3">
                      <label for="file-input">
                      <svg class="bi bi-image mt-3" width="2em" height="2em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd" d="M14.002 2h-12a1 1 0 00-1 1v10a1 1 0 001 1h12a1 1 0 001-1V3a1 1 0 00-1-1zm-12-1a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V3a2 2 0 00-2-2h-12z" clip-rule="evenodd"/>
                        <path d="M10.648 7.646a.5.5 0 01.577-.093L15.002 9.5V14h-14v-2l2.646-2.354a.5.5 0 01.63-.062l2.66 1.773 3.71-3.71z"/>
                        <path fill-rule="evenodd" d="M4.502 7a1.5 1.5 0 100-3 1.5 1.5 0 000 3z" clip-rule="evenodd"/>
                      </svg>
                      </label>
                      <input  @change="onFileChange" style = "display: none;width:0;height:0" id="file-input" type="file" />
                      </div>
                      <div class = "img-fluid" v-if="!image">
                      </div>
                      <div v-else>
                        <img style = "height:80px; width:90px ; border:1px solid none;border-radius:5px" class = "ml-3 mt-2 img-fluid" :src="image" />
                      </div>
                     </div>
                   </div>
                </form>
            </div>
          </div>
          <div class = "card mt-4" v-for="post in group.group_posts" style="width:600px" :key="post.post_id">
            <div class = "card-body">
              <div class = "row">
                <div class = "col" style ="width:20%">
                  <img class = "img-fluid" v-bind:src=post.prof_pic  style ="height:50px;width:50px;border:1px solid none; border-radius:50%">
                </div>
                <div class = "d-flex flex-column" style ="width:86%">
                  <h4 class = "Card Title" style = "font-size:16; font-weight:bold; text-align:left">{{group.group_name}}</h4>
                  <p style = "margin-left:5px;font-size:12px;color:gray;text-align:left">{{post.date_posted}}</p>
                </div>
              </div>
              <div class = "row ml-2">
                <p class = "mr-2 mt-3" style = "text-align:left">{{post.post_msg}}</p>
                <img v-if='post.img_url!=="/static/uploads/"' class = "img-fluid" :src='post.img_url'>
              </div>
              <hr>
              <div v-for="comment in post.Comments" :key="comment.id" class = "row mr-2">
                <div class = "col" style ="width:20%">
                  <img class = "img-fluid" style ="height:40px;width:40px;border:1px solid none; border-radius:50%" v-bind:src=comment.prof_pic>
                </div>
                <div class = "d-flex flex-column" style ="width:86%">
                  <div class = "d-flex flex-row justify-content-between">
                  <h4 class = "Card Title" style = "font-size:18px;font-weight:bold; text-align:left">{{comment.first_name}} {{comment.last_name}}</h4>
                   <p  style = "margin-left:5px;font-size:15px;color:gray;margin-right:25px">{{dateToTime(comment.date_commented)}}</p>
                  </div>
                  <p style = "margin-left:5px;font-size:16px;text-align:left">{{comment.comment_text}}</p>
                </div>
              </div>
              <hr>
                <div class = "row mr-2">
                <div class = "col" style ="width:20%">
                  <img class = "img-fluid" style ="border:1px solid none;height:70px;70px:auto;border:1px solid none; border-radius:50%" >
                </div>
                <div class = "d-flex flex-column" style ="width:86%">
                  <form v-on:submit.prevent="commentSubmit(post.post_id)">
                    <div class = "d-flex flex-row">
                      <textarea :id = post.post_id style = "width:370px" class = "form-control mt-3" placeholder="Leave a comment" rows = 1></textarea>
                      <div class = "ml-3 mt-3" style="height:38px;width:70px">
                      <button  type = "submit" class = "btn btn-outline-success btn-block" >Send</button>
                      </div>
                    </div>
                  </form>
                </div>
                </div>
            </div>
          </div>
          </div>
        </div>
      </div>
        <div class = "col">
          <b-container class = "mt-5">
            <h3>Group Members</h3>
            <b-row>
              <b-col style="margin-left:150px" cols="12" v-show="group.members.length !== 0" sm="4" class="mb-4 absolutemy-1" :key="user.member_id" v-for="user in paginatedItems">
                    <div class = " card-body  d-flex flex-row justify-content-center align-items-center ">
                      <img @click="toProfile(user.member_id)" style = "border:1px solid none; border-radius:50%; width:auto; height:70px" :src="user.prof_pic">
                      <p class="ml-4 card-text">{{user.member_fname}}  {{ user.member_lname }}</p>
                      <div class = "ml-4" style = "height:70%;width:auto">
                      <b-button @click="toProfile(user.member_id)"  variant="outline-success">View Profile</b-button>
                      </div>
                    </div>
              </b-col>
            </b-row>

            <b-row>
              <b-col style="margin-left:150px" md="6" class=" my-1">
                <b-pagination
                  @change="onPageChanged"
                  :total-rows="totalRows"
                  :per-page="perPage"
                  v-model="currentPage"
                  class="my-0"
                />
              </b-col>
            </b-row>
          </b-container>
            </div>
</template>

<script>
// eslint-disable-next-line camelcase
import Nav_bar from './Nav_bar.vue'
// eslint-disable-next-line no-unused-vars
import axios from 'axios'
import jwtDecode from 'jwt-decode'

export default {
  components: {
    'Nav_bar': Nav_bar
  },
  data () {
    const token = localStorage.usertoken
    const decoded = jwtDecode(token)
    return {
      profile_pic: decoded.identity.profile_pic,
      first_name: decoded.identity.first_name,
      last_name: decoded.identity.last_name,
      user_id: decoded.identity.id,
      group: [],
      group_id: '',
      post_msg: this.posting_msg,
      image: '',
      selected_file: null,
      paginatedItems: [],
      currentPage: 1,
      perPage: 3,
      totalRows: null,
      member_status: null
    }
  },

  created () {
    this.group_id = parseInt(this.$route.params.id)
    axios.get('http://localhost:5000/users/group/' + this.group_id).then((res) => {
      this.group = res.data.group
      var member
      for (member of this.group.members) {
        if (member.member_id === this.user_id) {
          this.member_status = 1
        }
        this.paginatedItems = this.group.members
        this.totalRows = this.group.members.length
        this.paginate(this.perPage, 0)
      }
    })
  },
  mounted () {

  },
  watch: {
    group: function (oldPosts, newPosts) {
      this.updateGroup()
    },
    member_status: function () {
      this.checkStatus()
    }},
  methods: {
    // eslint-disable-next-line camelcase
    paginate (page_size, page_number) {
      let itemsToParse = this.group.members
      this.paginatedItems = itemsToParse.slice(
        // eslint-disable-next-line camelcase
        page_number * page_size,
        // eslint-disable-next-line camelcase
        (page_number + 1) * page_size
      )
    },
    onPageChanged (page) {
      this.paginate(this.perPage, page - 1)
    },
    updateGroup () {
      axios.get('http://localhost:5000/users/group/' + this.group_id).then((res) => {
        this.group = res.data.group
      })
    },
    onFileChange (e) {
      var files = e.target.files || e.dataTransfer.files
      this.selected_file = files[0]
      if (!files.length) { return }
      this.createImage(files[0])
    },
    createImage (file) {
      // eslint-disable-next-line no-unused-vars
      var image = new Image()
      var reader = new FileReader()
      var vm = this

      reader.onload = (e) => {
        vm.image = e.target.result
      }
      reader.readAsDataURL(file)
    },
    checkStatus () {
      var member
      for (member of this.group.members) {
        if (member.member_id === this.user_id) {
          this.member_status = 1
        }
      }
    },
    joinGroup () {
      var fd = new FormData()
      fd.append('user_id', this.user_id)
      axios.post('http://localhost:5000/users/group/' + this.group_id, fd)
    },
    toProfile (id) {
      this.$router.push('/profile/' + id)
    },
    postSubmit () {
      const fd = new FormData()
      fd.append('group_id', this.group.group_id)
      fd.append('user', this.user_id)
      fd.append('msg', this.posting_msg)
      fd.append('file', document.getElementById('file-input').files[0])
      axios.post('http://localhost:5000/user/group/post', fd).then((res) => {
        this.posting_msg = ''
        this.image = ''
        this.$forceUpdate()
      })
    },
    commentSubmit (postID) {
      const fd = new FormData()
      var commentmsg = document.getElementById(postID).value
      fd.append('user', this.user_id)
      fd.append('posted_to', postID)
      fd.append('comment_txt', commentmsg)
      axios.post('http://localhost:5000/user/comment', fd).then((res) => {
        document.getElementById(postID).value = ''
        this.$forceUpdate()
      })
    },
    dateToTime (str) {
      var date = new Date(str)
      var minutes = date.getMinutes()
      if (parseInt(date.getMinutes()) < 10) {
        minutes = '0'.concat(date.getMinutes())
      }
      return [date.getHours(), minutes].join(':')
    }
  }

}

</script>
