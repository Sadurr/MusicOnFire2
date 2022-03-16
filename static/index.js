var modal = document.getElementById("modal");
var btn = document.getElementById("addModalButton");
var span = document.getElementsByClassName("close")[0];

btn.onclick = function() {
  modal.style.display = "block";
}

span.onclick = function() {
  modal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

// check if modal is open 
// const modal = document.querySelector("#modal");
//         const body = document.querySelector("body");
  
//         const showModal = function (e) {
//             modal.classList.toggle("hidden");
  
//             if (!modal.classList.contains("hidden")) {
//                 // Disable scroll
//                 body.style.overflow = "hidden";
//             } else {
//                 // Enable scroll
//                 body.style.overflow = "auto";
    
//             }
//         };