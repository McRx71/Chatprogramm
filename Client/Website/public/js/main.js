function sendData(data, type) {
  var xhttp = new XMLHttpRequest();
  xhttp.open("POST", "http://" + window.location.host + "/" + type);
  xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  xhttp.send(data);
}

function listen() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
          alert("sdsd")
     }
  };
}

function register(){
  username = document.getElementById("username").value;
  password = document.getElementById("password").value;
  email = document.getElementById("email").value;
  sendData(username + ":" + password + ":" + email, "register");
  window.location.pathname = "login";
  alert("Registering...");//TODO: add callback from node js server if succeded or not and display with alert
  return false;
}

function login(){
  username = document.getElementById("username").value;
  password = document.getElementById("password").value;
  sendData(username + ":" + password, "login");
  window.location.pathname = "adminPanel";
  alert("Logging in...");//TODO: add callback from node js server if succeded or not and display with alert
  return false;
}