/* eslint-disable vue/require-v-for-key */
<template>
<div class = "container-fluid">
  <Nav_bar id = "navbar">
  </Nav_bar>
  <section>
    <div class = "container">
      <div class = "row py-1">
        <div class = "w-80 py-3">
          <h3 class = "card-title mt-5" style = "text-align:left">What's on your mind?</h3>
          <div class = "card mt-4 " style="width:70%">
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
          <div class = "card mt-4" v-for="post in posts" style="width:600px" :key="post.id">
            <div class = "card-body">
              <div class = "row">
                <div class = "col" style ="width:20%">
                  <img class = "img-fluid" v-bind:src=post.prof_pic  style ="height:50px;width:50px;border:1px solid none; border-radius:50%">
                </div>
                <div class = "d-flex flex-column" style ="width:86%">
                  <h4 class = "Card Title" style = "font-size:16; font-weight:bold; text-align:left">{{post.first_name}} {{post.last_name}}</h4>
                  <p style = "margin-left:5px;font-size:12px;color:gray;text-align:left">{{post.date_posted}}</p>
                </div>
              </div>
              <div class = "row ml-2">
                <p class = "mr-2 mt-3" style = "text-align:left">{{post.msg}}</p>
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
                  <form v-on:submit.prevent="commentSubmit(post.id)">
                    <div class = "d-flex flex-row">
                      <textarea :id = post.id style = "width:370px" class = "form-control mt-3" placeholder="Leave a comment" rows = 1></textarea>
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
        <div class="col">
          <div class = "row">
            <div class = "col">
          <b-container class = "mt-5">
            <h3>Friend Request</h3>
            <b-row>
              <b-col style="margin-left:150px" cols="12" v-show="friend_request.length !== 0" sm="4" class="mb-4 absolutemy-1" :key="user.id" v-for="user in paginatedItems">
                    <div class = " card-body  d-flex flex-row justify-content-center align-items-center ">
                      <img @click="toProfile(user.user_id)" style = "border:1px solid none; border-radius:50%; width:auto; height:70px" :src="user.profile_pic">
                      <p class="ml-4 card-text">{{user.first_name}}  {{ user.last_name }}</p>
                      <div class = "ml-4" style = "height:70%;width:auto">
                      <b-button @click="acceptFriend(user.user_id)"  variant="outline-success">Accept</b-button>
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
          </div>
          <div class = "row">
            <div class = "col">
          <b-container class = "mt-5">
            <h3>Friends</h3>
            <b-row>
              <b-col style="margin-left:150px" cols="12" v-show="friend_request.length !== 0" sm="4" class="mb-4 absolutemy-1" :key="user.id" v-for="user in paginatedItems_friends">
                    <div class = " card-body  d-flex flex-row justify-content-center align-items-center ">
                      <img @click="toProfile(user.user_id)" style = "border:1px solid none; border-radius:50%;width:auto; height:70px" :src="user.profile_pic">
                      <p class="ml-4 card-text">{{user.first_name}}  {{ user.last_name }}</p>
                      <div class = "ml-4" style = "height:70%;width:auto">
                      </div>
                    </div>
              </b-col>
            </b-row>
            <b-row>
              <b-col style="margin-left:150px" md="6" class=" my-1">
                <b-pagination
                  @change="onPageChanged_friends"
                  :total-rows="totalRows_friends"
                  :per-page="perPage_friend"
                  v-model="currentPage_friends"
                  class="my-0"
                />
              </b-col>
            </b-row>
          </b-container>
            </div>
          </div>

        </div>
      </div>
    </div>
  </section>

</div>
</template>

<script>

// eslint-disable-next-line camelcase
import Nav_bar from './Nav_bar.vue'
import jwtDecode from 'jwt-decode'
import axios from 'axios'

export default{
  components: {
    'Nav_bar': Nav_bar
  },
  data () {
    const token = localStorage.usertoken
    const decoded = jwtDecode(token)
    return {
      paginatedItems_friends: [],
      friends: [],
      friend_request: [],
      profile_pic: decoded.identity.profile_pic,
      first_name: decoded.identity.first_name,
      last_name: decoded.identity.last_name,
      id: decoded.identity.id,
      posts: [],
      post_msg: this.posting_msg,
      image: '',
      selected_file: null,
      paginatedItems: [],
      currentPage: 1,
      perPage: 5,
      totalRows: null,
      currentPage_friends: 1,
      perPage_friend: 3,
      totalRows_friends: null }
  },
  mounted () {
    axios.get('http://localhost:5000/user/posts/' + this.id.toString()).then((res) => {
      this.posts = res.data.posts
    })
    axios.get('http://localhost:5000/users/friends/' + this.id.toString()).then((res) => {
      this.friends = res.data.friends
      this.paginatedItems_friends = this.friends
      this.totalRows_friends = this.friends.length
      this.paginate_friends(this.perPage_friend, 0)
    })
    axios.get('http://localhost:5000/users/request/' + this.id.toString()).then((res) => {
      this.friend_request = res.data.requests
      this.paginatedItems = this.friend_request
      this.totalRows = this.friend_request.length
      this.paginate(this.perPage, 0)
    })
  },
  watch: {
    posts: function (oldPosts, newPosts) {
      this.getPosts()
    },
    friends: function (oldFriends, newFriends) {
      this.getFriends()
    },
    friend_request: function (oldFriendRequests, newFriendRequest) {
      this.getFriendRequest()
    }
  },
  methods: {
    getFriends () {
      axios.get('http://localhost:5000/users/friends/' + this.id.toString()).then((res) => {
        this.friends = res.data.friends
        this.paginatedItems_friends = this.friends
        this.totalRows_friends = this.friends.length
      })
    },
    getFriendRequest () {
      axios.get('http://localhost:5000/users/request/' + this.id.toString()).then((res) => {
        this.friend_request = res.data.requests
        this.paginatedItems = this.friend_request
        this.totalRows = this.friend_request.length
      })
    },
    // eslint-disable-next-line camelcase
    paginate (page_size, page_number) {
      let itemsToParse = this.friend_request
      this.paginatedItems = itemsToParse.slice(
        // eslint-disable-next-line camelcase
        page_number * page_size,
        // eslint-disable-next-line camelcase
        (page_number + 1) * page_size
      )
    },
    getPosts () {
      axios.get('http://localhost:5000/user/posts/' + this.id.toString()).then((res) => {
        this.posts = res.data.posts
      })
    },
    // eslint-disable-next-line camelcase
    paginate_friends (page_size, page_number) {
      let itemsToParse = this.friends
      this.paginatedItems_friends = itemsToParse.slice(
        // eslint-disable-next-line camelcase
        page_number * page_size,
        // eslint-disable-next-line camelcase
        (page_number + 1) * page_size
      )
    },
    onPageChanged (page) {
      this.paginate(this.perPage, page - 1)
    },
    onPageChanged_friends (page) {
      this.paginate_friends(this.perPage_friend, page - 1)
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
    toProfile (id) {
      this.$router.push('/profile/' + id)
    },
    postSubmit () {
      const fd = new FormData()
      fd.append('user', this.id)
      fd.append('msg', this.posting_msg)
      fd.append('file', document.getElementById('file-input').files[0])
      axios.post('http://localhost:5000/user/post', fd).then((res) => {
        this.posting_msg = ''
        this.image = ''
        console.log(res)
        this.$forceUpdate()
      })
    },
    commentSubmit (postID) {
      const fd = new FormData()
      var commentmsg = document.getElementById(postID).value
      fd.append('user', this.id)
      fd.append('posted_to', postID)
      fd.append('comment_txt', commentmsg)
      axios.post('http://localhost:5000/user/comment', fd).then((res) => {
        document.getElementById(postID).value = ''
        this.$forceUpdate()
      })
    },
    // eslint-disable-next-line camelcase
    acceptFriend (user_id) {
      var fd = new FormData()
      fd.append('user1_id', user_id)
      fd.append('user2_id', this.id)
      axios.post('http://localhost:5000/users/accept', fd).then((res) => {
        console.log(res)
      }
      )
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
