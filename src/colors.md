# Selecting theme colors

_Click on a tile to change the primary color_:

<div class="mdx-switch">
  <button data-md-color-primary="red"><code>red</code></button>
  <button data-md-color-primary="pink"><code>pink</code></button>
  <button data-md-color-primary="purple"><code>purple</code></button>
  <button data-md-color-primary="deep-purple"><code>deep purple</code></button>
  <button data-md-color-primary="indigo"><code>indigo</code></button>
  <button data-md-color-primary="blue"><code>blue</code></button>
  <button data-md-color-primary="light-blue"><code>light blue</code></button>
  <button data-md-color-primary="cyan"><code>cyan</code></button>
  <button data-md-color-primary="teal"><code>teal</code></button>
  <button data-md-color-primary="green"><code>green</code></button>
  <button data-md-color-primary="light-green"><code>light green</code></button>
  <button data-md-color-primary="lime"><code>lime</code></button>
  <button data-md-color-primary="yellow"><code>yellow</code></button>
  <button data-md-color-primary="amber"><code>amber</code></button>
  <button data-md-color-primary="orange"><code>orange</code></button>
  <button data-md-color-primary="deep-orange"><code>deep orange</code></button>
  <button data-md-color-primary="brown"><code>brown</code></button>
  <button data-md-color-primary="grey"><code>grey</code></button>
  <button data-md-color-primary="blue-grey"><code>blue grey</code></button>
  <button data-md-color-primary="black"><code>black</code></button>
  <button data-md-color-primary="white"><code>white</code></button>
</div>

<script>
  var buttons = document.querySelectorAll("button[data-md-color-primary]")
  buttons.forEach(function(button) {
    button.addEventListener("click", function() {
      var attr = this.getAttribute("data-md-color-primary")
      document.body.setAttribute("data-md-color-primary", attr)
      var name = document.querySelector("#__code_2 code span:nth-child(7)")
      name.textContent = attr.replace("-", " ")
    })
  })
</script>


_Click on a tile to change the accent color_:

<style>
  .md-typeset button[data-md-color-accent] > code {
    background-color: var(--md-code-bg-color);
    color: var(--md-accent-fg-color);
  }
</style>

<div class="mdx-switch">
  <button data-md-color-accent="red"><code>red</code></button>
  <button data-md-color-accent="pink"><code>pink</code></button>
  <button data-md-color-accent="purple"><code>purple</code></button>
  <button data-md-color-accent="deep-purple"><code>deep purple</code></button>
  <button data-md-color-accent="indigo"><code>indigo</code></button>
  <button data-md-color-accent="blue"><code>blue</code></button>
  <button data-md-color-accent="light-blue"><code>light blue</code></button>
  <button data-md-color-accent="cyan"><code>cyan</code></button>
  <button data-md-color-accent="teal"><code>teal</code></button>
  <button data-md-color-accent="green"><code>green</code></button>
  <button data-md-color-accent="light-green"><code>light green</code></button>
  <button data-md-color-accent="lime"><code>lime</code></button>
  <button data-md-color-accent="yellow"><code>yellow</code></button>
  <button data-md-color-accent="amber"><code>amber</code></button>
  <button data-md-color-accent="orange"><code>orange</code></button>
  <button data-md-color-accent="deep-orange"><code>deep orange</code></button>
</div>

<script>
  var buttons = document.querySelectorAll("button[data-md-color-accent]")
  buttons.forEach(function(button) {
    button.addEventListener("click", function() {
      var attr = this.getAttribute("data-md-color-accent")
      document.body.setAttribute("data-md-color-accent", attr)
      var name = document.querySelector("#__code_3 code span:nth-child(7)")
      name.textContent = attr.replace("-", " ")
    })
  })
</script>

Join directly:

[Long Range Colloquium](long_range_colloquium.md){ .md-button }
[Speakers' Corner](speakers-corner.md){ .md-button }

## Welcome

Virtual Science Forum is a [volunteer-run](whoweare.md) open platform aiming to accommodate organization of online conferences.
We organize, host, and support virtual academic events.
Additionally we develop best practices and provide recommendations for all community members.

## What we do

We offer beginning-to-end support for organizing an academic event of your own, check out the [organizer guide](organizerguide.md) to see what it takes. It could be a seminar series, a workshop or a tutorial. We prioritize upholding a safe, accessible, inclusive and equitable online environment for all across the spectrum of identities and lived experiences. We encourage participation, either as speakers, organizers or audience, of all members of the scientific community.

### Current Events
* [Long Range Colloquium](long_range_colloquium.md) series **every other Wednesday** at 1:30 pm EDT / 7:30pm CEST
* [Speakers' Corner](speakers-corner.md), a **self-invited** seminar series

### Previous Events
* Workshop: [Quantum Oscillations in insulators](quantum-oscillations-insulators.md)
* Mini-tutorial on [computational quantum transport](quantum-transport-workshop.md)
* [Observing Anyons 2020](Observing_Anyons_2020.md) mini-conference
* Workshop on [Scanning Probe Microscopy](SPM_workshop.md)
* Virtual March Meeting sessions on [quantum information and machine learning](inauguralsession.md)
* 2020 run of the [Long Range Colloquium](long_range_colloquium.md) series

### Follow us

Sign up for the event announcements [mailing list](mailinglist.md)

<style>
iframe.twitter-follow-button {
    border: none;
}
</style>
<a href="https://twitter.com/virtualsciforum?ref_src=twsrc%5Etfw" class="twitter-follow-button" data-size="large" data-dnt="true" data-show-count="true">Follow @virtualsciforum</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

### Join us

We are always happy to welcome new members on the organizational side of VSF. 
Please take a look [here](contact.md) to see how to keep up with our activities or join our organising team.

<a class="github-button" href="https://github.com/virtualscienceforum/virtualscienceforum" data-size="large" data-show-count="true" aria-label="Star virtualscienceforum/virtualscienceforum on GitHub">Star</a>
