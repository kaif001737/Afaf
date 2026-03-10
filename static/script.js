document.querySelectorAll(".option").forEach(option => {

option.addEventListener("click", function(){

let card = option.closest(".quiz-card")

card.querySelectorAll(".option").forEach(o=>{
o.classList.remove("selected")
})

option.classList.add("selected")

let radio = option.querySelector("input")
radio.checked = true

})

})