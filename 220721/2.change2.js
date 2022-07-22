<<<<<<< HEAD
const select = document.querySelector("select");
const div = document.querySelector("div");

// value 값을 읽어옴
select.addEventListener("change", function(e){
    console.log(e.target.value);
    div.textContent = e.target.value;
=======
const select = document.querySelector("select");
const div = document.querySelector("div");

// value 값을 읽어옴
select.addEventListener("change", function(e){
    console.log(e.target.value);
    div.textContent = e.target.value;
>>>>>>> bd9deaa0376a03549404e8548c7d9025bd239699
})