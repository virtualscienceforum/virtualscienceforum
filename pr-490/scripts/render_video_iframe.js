const videoIframeHTML = '<iframe width="100%" height="315" src="https://www.youtube-nocookie.com/embed/{0}"\
 frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'

component$.subscribe(
  function (event){
    var ref = event.ref;
    if (ref.className !== "tabbed-set tabbed-alternate"){
      return;
    }
    var tabNumber = Array.prototype.indexOf.call(ref.children, ref.querySelector("input:checked"))
    var tab = ref.querySelectorAll(".tabbed-block")[tabNumber]
    var youtubeDiv = tab.querySelector("div[data-youtubeId]")
    if (youtubeDiv && !youtubeDiv.innerHTML){
      youtubeDiv.innerHTML = videoIframeHTML.replace("{0}", youtubeDiv.getAttribute("data-youtubeId"))
    }
  }
)