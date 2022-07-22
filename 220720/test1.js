const btns = []
for(let i=0;i<5;i++){
btns.push(document.createElement("button"));
btns[i].setAttribute("class", "all-btn");
const txt = document.createTextNode("버튼" + (i+1));
btns[i].append(txt);
document.querySelector("body").append(btns[i]);
}

const sampleBtn = document.querySelector(".all-btn");
sampleBtn.addEventListener("click", function() { 
alert("안녕");
});