{% macro registration_form(talk) %}
<form id='registrationForm-{{talk.zoom_meeting_id}}' method='post' class="registration" action='https://vsf-worker.virtualscienceforum.workers.dev/register' style='border:1px solid #ccc' onsubmit="submitZoomRegistration(event, {{talk.zoom_meeting_id}})">
  <div class='container'>
    <h1>Sign Up</h1>
    <p>Please fill in this form to register for the talk by.</p>
    <hr>
    <label for='firstname'><b>First Name</b></label>
    <input type='text' placeholder='Enter your first name' name='firstname' id='firstname-{{talk.zoom_meeting_id}}' required>
    <label for='lastname'><b>Last Name</b></label>
    <input type='text' placeholder='Enter your last name' name='lastname' id='lastname-{{talk.zoom_meeting_id}}' required>
    <label for='address'><b>Email</b></label>
    <input type='email' placeholder='Enter your email' name='address' id='address-{{talk.zoom_meeting_id}}' required>
    <label for='org'><b>Affiliation</b></label>
    <input type='text' placeholder='Enter your affiliation' name='affiliation' id='affiliation-{{talk.zoom_meeting_id}}' required>
    <label for="howdidyouhear"><b>How did you hear about us?</b></label>
    <select id="howdidyouhear-{{talk.zoom_meeting_id}}" name="howdidyouhear" required>
      <option value="Email list">Email list</option>
      <option value="A colleague (not an organizer)">A colleague (not an organizer)</option>
      <option value="One of the organizers">One of the organizers</option>
      <option value="Other" selected>Other</option>
    </select>
    <div id='checkboxes'>
        <ul id='checkboxes' style='list-style:none'>
          <li> <input type='checkbox' name='instructions-checkbox' value='confirm-instructions' required> Please confirm you have read the <a href='http://virtualscienceforum.org/#/attendeeguide'>participant instructions*</a> </li>
          <li> <input type='checkbox' name='contact-checkbox' value='confirm-contact' checked> Please check this box if we may contact you about future VSF events </li>
        </ul>
    </div>
    <input type='hidden' name='eventType' id='eventType-{{talk.zoom_meeting_id}}' value='{{talk.event_type}}' required>
    <input type='hidden' name='meetingID' id='meetingID-{{talk.zoom_meeting_id}}' value='{{talk.zoom_meeting_id}}' required>
    <div id='recaptcha' name='recaptcha' class='g-recaptcha' data-sitekey='6Lf37MoZAAAAAF19QdljioXkLIw23w94QWpy9c5E'></div>
    <div class='clearfix container'>
      <button type='submit' class='registerbtn'>Register</button>
    </div>
    <div id="errordiv-{{talk.zoom_meeting_id}}" class="alert" style="display:none">
      <span class="closebtn" onclick="this.parentElement.style.display='none';"">&times;</span>
      <strong id="errormsg-{{talk.zoom_meeting_id}}"></strong>
    </div>
  </div>
</form>
{% endmacro %}