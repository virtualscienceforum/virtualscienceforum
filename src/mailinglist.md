<form id="mailingListForm" method="post" class="registration" action="https://vsf-worker.virtualscienceforum.workers.dev/maillinglist" style="border:1px solid #ccc" onsubmit="submitMailingListSignupForm(event);">
  <div class="container">
    <h1>Sign Up</h1>
    <p>Please fill in this form and select the mailing lists you would like to join.</p>
    <div id="errordiv" class="alert" style="display:none">
      <span class="closebtn" onclick="this.parentElement.style.display='none';"">&times;</span>
      <strong id="errormsg"></strong>
    </div>
    <hr>
    <label for="name"><b>Name</b></label>
    <input type="text" placeholder="Enter your name" name="name" id="name" required>
    <label for="address"><b>Email</b></label>
    <input type="text" placeholder="Enter your Email" name="address" id="address" required>
    <div id="mailinglists">
      <label for="mailinglist"><b>Mailing lists</b></label>
      <ul id="mailinglist" style='list-style:none'>
        <li> <input type="checkbox" name="signup-checkbox" value="signup-general" checked> General mailing list </li>
        <li> <input type="checkbox" name="signup-checkbox" value="signup-speakerscorner"> <a href="#speakers-corner">Speakers' Corner</a> mailing list </li>
      </ul>
    </div>
    <div id="recaptcha" name="recaptcha" class="g-recaptcha" data-sitekey="6Lf37MoZAAAAAF19QdljioXkLIw23w94QWpy9c5E"></div>
    <div class="clearfix">
      <button type="submit" class="signupbtn">Sign Up</button>
    </div>
  </div>
</form>

<script src='https://www.google.com/recaptcha/api.js' async defer></script>
