<template>
<div class = "container-fluid">
<nav class="navbar navbar-expand-lg  navbar-fixed-top navbar-light bg-success">
  <a class="navbar-brand ml-2" href="#">
  <div class = "container" style = "background-color:white" >
    <span style = "color:#0E9F35;font-size:32px;font-weight:bold">M</span>
    </div>
  </a>
  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <form class="form-inline my-2 my-lg-0 mr-auto">
      <div class = "row lg-6 no-gutters ">
        <div class = "col d-flex" >
          <input class="form-control lg-6" style = "box-shadow:0px 1px 1px 1px #e5e5e5;border-bottom:0;border-right:thin solid #e5e5e5;border-top:thin solid #e5e5e5;float:left;border-bottom-right-radius: 0px;border-top-right-radius: 0px; align-self:center" type="text" aria-label="Search">
        </div>
          <button style = "box-shadow:1px 1px 1px 1px #e5e5e5;border-top:thin solid #e5e5e5;float:left;height:38px;background-color:#EEEEEE;padding:0" class="btn" type="submit">
            <img  style = "height:100%;width:80%;" src = "../assets/search-24px.png">
          </button>
        <div/>
    </div>
    </form>
    <ul style = "align-items:center" class="navbar-nav mr-5 d-inline-flex">
      <li class="nav-item mr-5" >
        <div class = "d-inline-flex p-2">
          <img src = "../assets/tajcore me.jpg" style = "align-self:center;height:40px;width:40px;border: 1px solid none;border-radius:40px">
          <button style = "font-weight:bold;color:white" class="btn btn-success btn-outline-white nav-link" href="#">Tahjyei</button>
        </div>
      </li>
      <li class="nav-item mr-5">
        <button style = "font-weight:bold;color:white" class="btn btn-success btn-outline-white nav-link" href="#">Home</button>
      </li>
     <b-dropdown id="dropdown-1" right variant ="success" no-caret  class="nav item mr-5 ">
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
       <b-dropdown-item>
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
        <img class = "ml-2 mr-2" style = "height:16px; width:auto" src = "../assets/event_note-24px.png">
        <strong class = "">Event</strong>
      </div>
      <div style = "align-items:center" class = "row d-flex-inline">
        <strong  style = "margin-left:33px;color:#A29B9B">Bring people together with events</strong>
      </div>
    </b-dropdown-item>
  </b-dropdown>
      <li class="nav-item">
        <a class="nav-link disabled" href="#"><img style = "height:40px;width:auto" src = "../assets/supervisor_account-24px.png"></a>
      </li>
    </ul>
  </div>
</nav>
</div>
</template>
