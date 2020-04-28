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
                <form>
                  <textarea class = "form-control form-control-lg" placeholder="Start a post..." rows = 3></textarea>
                   <div class = "row">
                     <div class = "col d-flex d-flex-row-reverse " style = "vertical-align:center">
                      <button class = "btn btn-outline-success mr-3" style = "margin-top:12px">Post</button>
                      <svg style = "" class="bi bi-image mt-3" width="2em" height="2em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd" d="M14.002 2h-12a1 1 0 00-1 1v10a1 1 0 001 1h12a1 1 0 001-1V3a1 1 0 00-1-1zm-12-1a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V3a2 2 0 00-2-2h-12z" clip-rule="evenodd"/>
                        <path d="M10.648 7.646a.5.5 0 01.577-.093L15.002 9.5V14h-14v-2l2.646-2.354a.5.5 0 01.63-.062l2.66 1.773 3.71-3.71z"/>
                        <path fill-rule="evenodd" d="M4.502 7a1.5 1.5 0 100-3 1.5 1.5 0 000 3z" clip-rule="evenodd"/>
                      </svg>
                     </div>
                   </div>
                </form>
            </div>
          </div>
          <div class = "card mt-4" style="width:70%">
            <div class = "card-body">
              <div class = "row">
                <div class = "col" style ="width:20%">
                  <img class = "img-fluid" style ="height:60px;width:auto;border:1px solid none; border-radius:100%" src = "../assets/tajcore me.jpg">
                </div>
                <div class = "d-flex flex-column" style ="width:86%">
                  <h4 class = "Card Title" style = "font-weight:bold; text-align:left">Tahjyei Thompson</h4>
                  <p style = "margin-left:5px;font-size:12px;color:gray;text-align:left">4hr ago</p>
                </div>
              </div>
              <div class = "row ml-2">
                <p class = "mr-2" style = "text-align:left">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
                <img class = "img-fluid" src = '../assets/tajcore me.jpg'>
              </div>
              <hr>
              <div class = "row mr-2">
                <div class = "col" style ="width:20%">
                  <img class = "img-fluid" style ="height:60px;width:auto;border:1px solid none; border-radius:100%" src = "../assets/tajcore me.jpg">
                </div>
                <div class = "d-flex flex-column" style ="width:86%">
                  <div class = "d-flex flex-row justify-content-between">
                  <h4 class = "Card Title" style = "font-weight:bold; text-align:left">Tahjyei Thompson</h4>
                   <p style = "margin-left:5px;font-size:15px;color:gray;margin-right:25px">11:00</p>
                  </div>
                  <p style = "margin-left:5px;font-size:16px;text-align:left">Damn I look good</p>
                </div>
              </div>
              <hr>
                <div class = "row mr-2">
                <div class = "col" style ="width:20%">
                  <img class = "img-fluid" style ="height:60px;width:auto;border:1px solid none; border-radius:100%" src = "../assets/tajcore me.jpg">
                </div>
                <div class = "d-flex flex-column" style ="width:86%">
                  <form>
                    <textarea  class = "form-control mt-3" placeholder="Leave a comment" rows = 1></textarea>
                  </form>
                </div>
                </div>
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
      id: decoded.identity.id
    }
  }
}

</script>
