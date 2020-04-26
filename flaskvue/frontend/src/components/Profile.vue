<template>
<div>
    <Nav_bar></Nav_bar>
    <div class = "container" style="margin-top:7%">
        <div class = "row" style = "height:200px;background-color:black">
            <div class = " align-self-end col d-flex flex-row justify-content-between">
                <div style = "margin-right:20px;margin-top:30px;height:300px;width:300px;border:2px solid white; border-radius:100%">
                <img  class = "align-self-end img-fluid" style = "border:1px solid none; border-radius:100%;height:100%;width:auto" src = "../assets/tajcore me.jpg">
                </div>
                <h4 class = "align-self-end" style = "font-size:30px;margin-bottom:140px;color:white;margin-right:auto;"><strong>Tahjyei Thompson</strong></h4>
                <button style= "margin-bottom:140px;height:40px;width:140px;" class = "align-self-end btn btn-light">
                    <div class = "d-flex flex-row">
                        <img class = "align-self-center img-fluid" style = "margin-right:auto;margin-bottom:25px;height:28px;width:auto" src = "../assets/create-24px.png">
                        <p class ="align-self-center" style ="margin-left:3px;margin-bottom:25px;font-size:16px;color:gray">Edit Profile</p>
                    </div>
                </button>
            </div>
        </div>
        <div class = "row " >
            <div style = "margin-left:35%; width:100%" class = "jumbotron d-flex flex-column">
                <div class = "d-flex flex-row">
                    <img class = "lead align-self-center" style ="height:40px ; width:auto" src="../assets/account_circle-24px.png">
                    <h4 class = "lead mt-2 ml-2 align-self-center"><strong>About</strong></h4>
                </div>
                <hr style = "width:100%;border:2px solid lightgray">
                 <div class = "d-flex flex-row">
                    <img class = "mr-2 align-self-center" style ="margin-bottom:2px;height:25px ; width:auto" src="../assets/mail_outline-24px.png">
                    <p class = "mt-3 ml-2 align-self-center" style = "color:gray"><strong>TahjyeiThompson@gmail.com</strong></p>
                </div>
                <div class = "d-flex flex-row">
                    <img class = "mr-2 align-self-center" style ="margin-bottom:2px;height:25px ; width:auto" src="../assets/location_on-24px.png">
                    <p class = "mt-3 ml-2 align-self-center" style = "color:gray"><strong>Portmore, Jamaica</strong></p>
                </div>
                    <div class = "d-flex flex-row">
                    <img class = "mr-2 align-self-center" style ="margin-bottom:2px;height:25px ; width:auto" src="../assets/event_note-24px.png">
                    <p class = "mt-3 ml-2 align-self-center" style = "color:gray"><strong>Joined on April 15th, 2020</strong></p>
                </div>
                <hr style = "width:100%;border:2px solid lightgray">
                <div class = "d-flex flex-row">
                    <img class = "lead align-self-center" style ="height:40px ; width:auto" src="../assets/account_circle-24px.png">
                    <h4 class = "lead mt-2 ml-2 align-self-center"><strong>Biography</strong></h4>
                </div>
                    <p style ="text-align:left; margin-left:20px; margin-top:10px">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. In est ante in nibh mauris cursus mattis molestie a. Elit duis tristique sollicitudin nibh.</p>
            </div>
        </div>
    </div>

</div>
</template>

<script>
// eslint-disable-next-line camelcase
import Nav_bar from './Nav_bar.vue'

export default{
  components: {
    'Nav_bar': Nav_bar
  }
}
</script>
