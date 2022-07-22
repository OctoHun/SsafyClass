function showAlert(){
  alert("야호");
}

const sampleBtn = document.querySelector(".sample-btn");

sampleBtn.addEventListener("click", showAlert);
// sampleBtn.addEventListener("이벤트이름", 불러올 함수)
// 조건을 만족할때까지 기다리는 함수 => 콜백함수(파라미터로 함수 자체가 들어가는 함수)
// 함수 선언 따로 안하고 showAlert 자리에 함수를 써도 됨.