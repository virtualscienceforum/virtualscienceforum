function submitMailingListSignupForm(event) {
    event.preventDefault();

    // Get a handle on the errordiv element..
    var errordiv = document.getElementById("errordiv")
    // ..and hide it by default
    errordiv.style.display = "none";

    // Get a handle on the errormessage element
    var errormsg = document.getElementById("errormsg")
    // ..and empty it by default
    errormsg.textContent = ""

    // The user needs to select at least one list to sign up for
    if( document.querySelectorAll('input[name=signup-checkbox]:checked').length <= 0 )
    {
      // Changing content and color of content
      errormsg.textContent = "Please select at least one mailing list";
      errormsg.style.color = "white";
      errordiv.style.backgroundColor = "#F44336";
      errordiv.style.display = "block";
      return false;
    }

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "https://vsf-worker.virtualscienceforum.workers.dev/mailinglist");

    xhr.onload = function(event){
        if(event.target.status == 200 ) {
          errordiv.style.backgroundColor = "#4CAF50";
        }
        errordiv.style.display = "block";
        errormsg.textContent = event.target.response;
    };

    // Convert the form into a FormData object that we will send to
    // the cloudflare worker
    formData = new FormData(document.forms["mailingListForm"]);
    xhr.send(formData);

    // Clear the form after submission
    document.forms["mailingListForm"].reset();

    // Don't reload or process anything further
    return false;
});

function submitZoomRegistration(event, meetingID) {
    event.preventDefault();

    // Get a handle on the errordiv element..
    var errordiv = document.getElementById("errordiv-" + meetingID)
    // ..and hide it by default
    errordiv.style.display = "none";

    // Get a handle on the errormessage element
    var errormsg = document.getElementById("errormsg-" + meetingID)
    // ..and empty it by default
    errormsg.textContent = ""

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "https://vsf-worker.virtualscienceforum.workers.dev/register");

    xhr.onload = function(event){
        if(event.target.status == 200 ) {
          errordiv.style.backgroundColor = "#4CAF50";
        }
        errordiv.style.display = "block";
        errormsg.textContent = event.target.response;
        console.log(event);
    };

    // Convert the form into a FormData object that we will send to
    // the cloudflare worker
    formData = new FormData(document.forms["registrationForm-"+meetingID]);
    xhr.send(formData);

    // Clear the form after submission
    document.forms["registrationForm-"+meetingID].reset();

    // Don't reload or process anything further
    return false;
  });
