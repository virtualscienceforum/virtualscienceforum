<script src='https://www.google.com/recaptcha/api.js?render=explicit' async defer></script>

<style>
body {font-family: Arial, Helvetica, sans-serif;}
* {box-sizing: border-box}

/* Full-width input fields */
input[type=text] {
  width: 100%;
  padding: 15px;
  margin: 5px 0 22px 0;
  display: inline-block;
  border: none;
  background: #f1f1f1;
}

input[type=text]:focus {
  background-color: #ddd;
  outline: none;
}

hr {
  border: 1px solid #f1f1f1;
  margin-bottom: 25px;
}

/* Set a style for all buttons */
button {
  background-color: #4CAF50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 100%;
  opacity: 0.9;
}

button:hover {
  opacity:1;
}

/* Float signup button and add an equal width */
.signupbtn {
  float: left;
  margin-top: 50px;
  width: 50%;
}

/* Add padding to container elements */
.container {
  padding: 16px;
}

/* Clear floats */
.clearfix::after {
  content: "";
  clear: both;
  display: table;
}


/* Change styles for cancel button and signup button on extra small screens */
@media screen and (max-width: 300px) {
  .signupbtn {
     width: 100%;
  }
}
</style>

<form action="https://vsf-worker.virtualscienceforum.workers.dev" method="post" onsubmit="function submit(event){}", style="border:1px solid #ccc">
  <div class="container">
    <h1>Sign Up</h1>
    <p>Please fill in this form and select the mailing lists you would like to join.</p>
    <hr>
    <label for="name"><b>Name</b></label>
    <input type="text" placeholder="Enter your name" name="name" id="name" required>
    <label for="address"><b>Email</b></label>
    <input type="text" placeholder="Enter your Email" name="address" id="address" required>
    <div id="mailinglists">
      <label for="mailinglist"><b>Mailing lists</b></label>
      <ul id="mailinglist" style='list-style:none'>
        <li> <input type="checkbox" name="signup-general" > General mailing list </li>
        <li> <input type="checkbox" name="signup-speakerscorner"> <a href="#">Speaker's Corner</a> mailing list </li>
      </ul>
    </div>
    <div id="recaptcha" class="g-recaptcha" data-sitekey="6Lf37MoZAAAAAF19QdljioXkLIw23w94QWpy9c5E"></div>
    <div class="clearfix">
      <button type="submit" class="signupbtn">Sign Up</button>
    </div>
  </div>
</form>
