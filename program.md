# Program

<script>
  var loc = Intl.DateTimeFormat().resolvedOptions().timeZone;
  document.getElementById("location").innerHTML = loc;

  var conferencedate = new Date('2020-03-06T17:00Z');
  var localtime = conferencedate.getHours();
  document.getElementById("conferencestart").innerHTML = localtime;
</script>

The preliminary program and confirmed invited speakers are listed here.

## Invited speakers
* Jane Doe (UnivA)
* John Deer (UnivB)


## Detailed program
It seems that you might be browsing from <span id="location">here</span>.
That means the conference will start at your location at <span id="conferencestart">here</span>.

| PST   	        | EST     	      | CET   	        | Speaker    	|
|---------------	|---------------	|---------------	|-----------	|
| 9:00 - 9:55   	| 12:00 - 12:55   | 18:00 - 18:55  	| Speaker 1 	|
| 10:00 - 10:25 	| 13:00 - 13:25 	| 19:00 - 19:25 	| Speaker 2 	|
| 10:30 - 10:55 	| 13:30 - 13:55 	| 19:30 - 19:55 	| Speaker 3 	|
