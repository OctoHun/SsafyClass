<<<<<<< HEAD
// 가져오기
const input = document.querySelector("input");
const div = document.querySelector("div");


// 이벤트리스너 발생시 이벤트 핸들러를 실행할 것
// change는 input 등에서 변화가 일어나면 사용(이전값과 달라짐)
input.addEventListener("change", function(e){
    console.log(e);
    // 이벤트가 발생한 위치
    console.log(e.target);
    // input의 데이터를 가져오는 경우 (input.value)
    console.log(e.target.value);
    div.textContent = e.target.value;
})
=======
// 가져오기
const input = document.querySelector("input");
const div = document.querySelector("div");


// 이벤트리스너 발생시 이벤트 핸들러를 실행할 것
// change는 input 등에서 변화가 일어나면 사용(이전값과 달라짐)
input.addEventListener("change", function(e){
    console.log(e);
    // 이벤트가 발생한 위치
    console.log(e.target);
    // input의 데이터를 가져오는 경우 (input.value)
    console.log(e.target.value);
    div.textContent = e.target.value;
})
>>>>>>> bd9deaa0376a03549404e8548c7d9025bd239699
