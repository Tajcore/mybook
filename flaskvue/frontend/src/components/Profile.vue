<template>
<div>
    <Nav_bar></Nav_bar>
    <div class = "container" style="margin-top:7%">
        <div class = "row" style = "height:200px;background-color:black">
            <div class = " align-self-end col d-flex flex-row justify-content-between">
                <div style = "margin-right:20px;margin-top:30px;height:300px;width:300px;border:2px solid white; border-radius:50%">
                <img  class = "align-self-end img-fluid" style = "border:1px solid none; border-radius:50%;height:100%;width:auto" v-bind:src=profile_details.Profile_pic>
                </div>
                <h4 class = "align-self-end" style = "font-size:30px;margin-bottom:140px;color:white;margin-right:auto;"><strong>{{profile_details.first_name}} {{profile_details.last_name}}</strong></h4>
                <button v-show="profile_id === id" v-b-modal.modal-edit-profile style = "margin-bottom:140px;height:40px;width:140px;" class = "align-self-end btn btn-light">
                    <div class = "d-flex flex-row">
                        <img class = "align-self-center img-fluid" style = "margin-right:auto;margin-bottom:25px;height:28px;width:auto" src = "../assets/create-24px.png">
                        <p class ="align-self-center" style ="margin-left:3px;margin-bottom:25px;font-size:16px;color:gray">Edit Profile</p>
                    </div>
                </button>
                <button @click="addFriend" v-show="profile_id !== id & relationship_status === null" style = "margin-bottom:140px;height:40px;width:140px;" class = "align-self-end btn btn-success">
                    <div class = "d-flex flex-row">
                        <p class ="align-self-center" style ="font-weight:bold;margin-left:18px;margin-bottom:23px;font-size:16px;color:white">Add Friend</p>
                    </div>
                </button>
                <button  v-show="profile_id !== id && relationship_status === 0" style = "margin-bottom:140px;height:40px;width:140px;" class = "align-self-end btn btn-light">
                    <div class = "d-flex flex-row">
                        <p class ="align-self-center" style ="margin-left:18px;font-weight:bold;margin-bottom:23px;font-size:16px;color:black">Pending</p>
                    </div>
                </button>
                <button  v-show="profile_id !== id && relationship_status === 1" style = "margin-bottom:140px;height:40px;width:140px;" class = "align-self-end btn btn-success">
                    <div class = "d-flex flex-row">
                        <p class ="align-self-center" style ="margin-left:28px;font-weight:bold;margin-bottom:23px;font-size:16px;color:white">Friends</p>
                    </div>
                </button>
            </div>
        </div>
        <div  v-show="HasProfile === false" class = "row " >
            <div  style = "margin-left:35%; width:100%" class = "jumbotron d-flex flex-column">
                <div  class = "d-flex flex-row">
                    <img class = "lead align-self-center" style ="height:40px ; width:auto" src="../assets/account_circle-24px.png">
                    <h4 class = "lead mt-2 ml-2 align-self-center"><strong>About</strong></h4>
                </div>
                <hr style = "width:100%;border:2px solid lightgray">
                 <div class = "d-flex flex-row">
                    <img class = "mr-2 align-self-center" style ="margin-bottom:2px;height:25px ; width:auto" src="../assets/mail_outline-24px.png">
                    <p class = "mt-3 ml-2 align-self-center" style = "color:gray"><strong>User Hasn't Added This Info</strong></p>
                </div>
                <div class = "d-flex flex-row">
                    <img class = "mr-2 align-self-center" style ="margin-bottom:2px;height:25px ; width:auto" src="../assets/location_on-24px.png">
                    <p class = "mt-3 ml-2 align-self-center" style = "color:gray"><strong>User Hasn't Added This Info</strong></p>
                </div>
                    <div class = "d-flex flex-row">
                    <img class = "mr-2 align-self-center" style ="margin-bottom:2px;height:25px ; width:auto" src="../assets/event_note-24px.png">
                    <p class = "mt-3 ml-2 align-self-center" style = "color:gray"><strong>User Hasn't Added This Info</strong></p>
                </div>
                <div class = "d-flex flex-row">
                    <img class = "mr-2 align-self-center" style ="margin-bottom:2px;height:25px ; width:auto" src="../assets/event_note-24px.png">
                    <p class = "mt-3 ml-2 align-self-center" style = "color:gray"><strong>User Hasn't Added This Info</strong></p>
                </div>
                <hr style = "width:100%;border:2px solid lightgray">
                <div class = "d-flex flex-row">
                    <img class = "lead align-self-center" style ="height:40px ; width:auto" src="../assets/account_circle-24px.png">
                    <h4 class = "lead mt-2 ml-2 align-self-center"><strong>Biography</strong></h4>
                </div>
                    <p style ="text-align:left; margin-left:20px; margin-top:10px">User Hasn't Added This Info</p>
            </div>
        </div>
        <div v-show="HasProfile === true" class = "row " >
            <div  style = "margin-left:35%; width:100%" class = "jumbotron d-flex flex-column">
                <div  class = "d-flex flex-row">
                    <img class = "lead align-self-center" style ="height:40px ; width:auto" src="../assets/account_circle-24px.png">
                    <h4 class = "lead mt-2 ml-2 align-self-center"><strong>About</strong></h4>
                </div>
                <hr style = "width:100%;border:2px solid lightgray">
                 <div class = "d-flex flex-row">
                    <img class = "mr-2 align-self-center" style ="margin-bottom:2px;height:25px ; width:auto" src="../assets/mail_outline-24px.png">
                    <p class = "mt-3 ml-2 align-self-center" style = "color:gray"><strong>{{profile_details.email}}</strong></p>
                </div>
                <div class = "d-flex flex-row">
                    <img class = "mr-2 align-self-center" style ="margin-bottom:2px;height:25px ; width:auto" src="../assets/location_on-24px.png">
                    <p class = "mt-3 ml-2 align-self-center" style = "color:gray"><strong>{{profile_details.location_}}</strong></p>
                </div>
                    <div class = "d-flex flex-row">
                    <img class = "mr-2 align-self-center" style ="margin-bottom:2px;height:25px ; width:auto" src="../assets/event_note-24px.png">
                    <p class = "mt-3 ml-2 align-self-center" style = "color:gray"><strong>Joined on {{[profile_details.date_created]}}</strong></p>
                </div>
                <div class = "d-flex flex-row">
                    <img class = "mr-2 align-self-center" style ="margin-bottom:2px;height:25px ; width:auto" src="../assets/event_note-24px.png">
                    <p class = "mt-3 ml-2 align-self-center" style = "color:gray"><strong>Born on {{profile_details.dob}}</strong></p>
                </div>
                <hr style = "width:100%;border:2px solid lightgray">
                <div class = "d-flex flex-row">
                    <img class = "lead align-self-center" style ="height:40px ; width:auto" src="../assets/account_circle-24px.png">
                    <h4 class = "lead mt-2 ml-2 align-self-center"><strong>Biography</strong></h4>
                </div>
                    <p style ="text-align:left; margin-left:20px; margin-top:10px">{{profile_details.bio}}</p>
            </div>
        </div>
        <FlashMessage></FlashMessage>
    <b-modal  busy=true id="modal-edit-profile" hide-backdrop content-class="shadow" title="Edit Profile">
    <div class = "container" style = "height:650px;">
      <div class = "row">
          <div class = "d-flex flex-column">
            <form>
              <div class = "container d-flex flex-column" >
                  <img style = "margin-left:120px;position:absolute;height:200px;width:auto;border:1px solid none;border-radius:50%" :src="image">
                  <div class="image-upload">
                    <label for="file-input">
                        <img style ="position:absolute;margin-top:150px;margin-left:205px;height:30px;width:auto" src ="../assets/photo.png"/>
                    </label>
                    <input  @change="onFileChange" style = "display: none;width:0;height:0" id="file-input" type="file" />
                </div>
              </div>
              <div class = "row">
                  <div style = "width:75%; margin-top:240px" class = "d-flex flex-row">
                      <img style = "margin-left:22px;" src = "../assets/mail_outline-24px.png">
                      <input v-model="email_input" style = "width:90%;margin-left:25px;" type = "text" class = " form-control">
                  </div>
                    <div class = "mt-4 d-flex flex-row" style = "width:75%;">
                      <img class = "ml-3" src = "../assets/location_on-24px.png">
                      <input v-model="location_input" style = "width:90%;margin-left:20px;" type = "text" class = " form-control">
                    </div>
                      <div class = "mt-3 form-group d-flex flex-row" style = "margin-left:20px;width:71%">
                        <img style = "height:40px;width:auto"  src = "../assets/account_circle-24px.png">
                        <select v-model="gender_input" class="ml-4 form-control" id="sel1">
                            <option>Male</option>
                            <option>Female</option>
                            <option>Non-Binary</option>
                        </select>
                    </div>
                    <div class = "mt-3 form-group d-flex flex-row" style = "margin-left:20px;width:71%">
                    <b-form-datepicker v-model = "dob_input" button-only id="dob-datepicker" ></b-form-datepicker>
                      <input style = "width:90%;margin-left:20px;" :value= dob_input type = "text" class = " form-control">
                    </div>
                    <textarea v-model="bio_input" style = "width:90%;margin-left:30px" rows = 4 class = "mt-3 ml-3 form-control"></textarea>
              </div>
            </form>
          </div>
      </div>
    </div>
  <template v-slot:modal-footer>
          <b-button size="sm" variant="success" @click="updateProfile()">
            Save Changes
          </b-button>

        </template>
  </b-modal>
    </div>
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
      first_name: decoded.identity.first_name,
      last_name: decoded.identity.last_name,
      id: decoded.identity.id,
      profile_id: '',
      dob_input: '',
      profile_details: [],
      HasProfile: false,
      image: decoded.identity.profile_pic,
      gender_input: '',
      email_input: '',
      location_input: '',
      bio_input: '',
      relationship_status: null
    }
  },
  created () {
    this.profile_id = this.$route.params.user_id
    var fd1 = new FormData()
    fd1.append('user1_id', this.id)
    fd1.append('user2_id', this.profile_id)
    axios.post('http://localhost:5000/users/status', fd1).then((res) => {
      this.relationship_status = res.data.status
    })
  },
  mounted () {
    axios.get('http://localhost:5000/user/profile/' + this.profile_id.toString()).then((res) => {
      this.profile_details = res.data.profile_details
      if (this.profile_details.gender !== 'none') {
        this.HasProfile = true
      }
    })
  },
  methods: {
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
    updateProfile () {
      var fd = new FormData()
      fd.append('email', this.email_input)
      fd.append('location', this.location_input)
      fd.append('dob', this.dob_input)
      fd.append('profile_pic', document.getElementById('file-input').files[0])
      fd.append('bio', this.bio_input)
      fd.append('gender', this.gender_input)
      fd.append('user_id', this.id)
      axios.post('http://localhost:5000/user/profile/' + this.id.toString(), fd).then((res) => {
        this.flashMessage.success({title: 'Profile Updated', message: 'Refresh the page to see the changes'})
      }).catch((err) => {
        // eslint-disable-next-line eqeqeq
        if (err.name != 'NavigationDuplicated') {
          this.flashMessage.error({title: err.name, message: err.message})
          throw err
        }
      })
    },
    addFriend () {
      var fd = new FormData()
      fd.append('user1_id', this.id)
      fd.append('user2_id', this.profile_id)
      axios.post('/users/add', fd)
    }
  }
}
</script>
