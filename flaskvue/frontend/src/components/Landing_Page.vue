<template>
<div class = "container-fluid">
<nav class="navbar navbar-expand-lg   fixed-top navbar-light bg-success">
  <a class="navbar-brand ml-2" href="#">
  <span style = "color:white;font-size:32px;font-weight:bold">MyBook</span>
  </a>
  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <form class="form-inline my-2 my-lg-0 ml-auto">
      <input class="form-control sm-1 mr-sm-2" type="text" placeholder="E-mail" aria-label="Search">
      <input class="form-control sm-1 mr-sm-2" type="text" placeholder="Password" aria-label="Search">
      <router-link to="/home"><button class="btn btn-success btn-outline-white my-2 my-sm-0" type="submit">Login</button></router-link>
    </form>
  </div>
</nav>

<div class = "container-fluid" style = "margin-top:10%">
  <div class = "row mt-5">
    <div class = "col mb-5">
      <div class = "container-fluid">
        <div class = "row">
         <div class = "col">
            <p style = "font-size:32px;font-weight:bold;text-align:left">Connect with friends and the world around you on MyBook</p>
          </div>
        </div>
        <div class = "row">
          <div class = "col">
            <div class = "row">
              <div class = "d-flex p-0 col">
              <img src = "../assets/assignment-24px.png" class = "img-fluid mr-3" style = "align-self:left">
              <h4 style = "font-size:20px;font-weight:bold;align-self:center">See photos and updates<span style = "font-weight:normal;"> from friends in News Feed.</span></h4>
              </div>
            </div>
            <div class = "row">
              <div class = "d-flex p-0 col">
              <img src = "../assets/tv-24px.png" class = "img-fluid mr-4" style = "align-self:left">
              <h4 style = "font-size:20px;font-weight:bold;align-self:center">Share what's new<span style = "font-weight:normal;"> in your life on your Timeline.</span></h4>
              </div>
            </div>
            <div class = "row">
              <div class = "d-flex p-0 col">
              <img src = "../assets/share-24px.png" class = "img-fluid mr-4" style = "align-self:center">
              <h4 style = "font-size:20px;font-weight:bold;align-self:center">Find more<span style = "font-weight:normal;"> of what you're looking for with MyBook Search.</span></h4>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class = "col">
      <div class = "container container-sm-1">
        <div class = "row">
         <div class = "col">
            <p style = "font-size:32px;font-weight:bold;text-align:left">Sign Up</p>
            <p style = "font-size:26px;font-weight:normal;text-align:left">It's quick and easy</p>
            <form>
                <div class = "row mb-3 ">
                  <div class = "col-sm-4">
                    <input class="form-control sm-1" type="text" placeholder="First Name" aria-label="first name">
                  </div>
                  <div class = "col-sm-4">
                    <input class="form-control sm-1" type="text" placeholder="Last Name" aria-label="last name">
                  </div>
                </div>
                <div class = "row mb-3">
                  <div class = "col-lg-8">
                      <input class="form-control sm- mr-sm-2" type="email" placeholder="E-mail" aria-label="email">
                  </div>
                </div>
                <div class = "row mb-3">
                  <div class = "col-lg-8">
                      <input class="form-control sm- mr-sm-2" type="password" placeholder="Password" aria-label="password">
                  </div>
                  </div>
                <div class = "row no-gutters justify-content-start mb-3">
                    <button style="background-color:#24416D;color:white;font-weight:bold;letter-spacing:2px;" class="btn btn-outline-white my-2 my-sm-0" type="submit">Sign Up</button>
                </div>
            </form>
           </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <nav class="navbar navbar-expand-lg p-4 fixed-bottom navbar-light bg-success">
    <h4 class = "ml-auto nav-brand" style = "color:white">Copyright 2020 COMP3161</h4>
  </nav>
</div>
</template>
