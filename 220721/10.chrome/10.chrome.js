<<<<<<< HEAD
//토글버튼 클릭시에 이벤트 발생
const toggleButton = document.querySelector(".toggle-button");
const body = document.querySelector("body");
const headerNav = document.querySelector(".header-nav");
const texts = document.querySelectorAll(".text");

toggleButton.addEventListener("click", function(){

    toggleButton.textContent = "다크모드";

    //버튼 클릭시마다 classList의 toggle로 class 추가
    toggleButton.classList.toggle("toggle-button-darkmode");
    body.classList.toggle("body-background-darkmode");
    headerNav.classList.toggle("text-darkmode");
    // bookmarkWrapper.classList.toggle("text-darkmode");

    for (let i=0; i<texts.length;i++){
        texts[i].classList.toggle("text-darkmode");
    }


    //classList의 contains
    if(toggleButton.classList.contains("toggle-button-darkmode")){
        toggleButton.textContent = "일반모드";
    }
})


// 구글 이동
const searchInput = document.querySelector(".search-input");
searchInput.addEventListener("keyup", function(e){
    console.log(e);

    // e.code === "Enter"일때 특정 위치로 이동시킨다.
    if(e.code === "Enter"){


        // 유효성 검사, 빈값인 경우 검색어 입력 안했다고 경고
        if (!e.target.value){
            alert("검색어를 입력하지 않았습니다!");
            return;
        }

        // https://www.google.com/search?q=내용
        const target = "https://www.google.com/search?q="

        // 이동하는 두 가지 방법
        // 첫번째: 그냥 이동 -> location.href
        // location.href = "https://www.google.com/search?q=" + e.target.value;
        // 두번째: 새 탭 이동 -> window.open
        window.open(target + e.target.value);
    }
=======
//토글버튼 클릭시에 이벤트 발생
const toggleButton = document.querySelector(".toggle-button");
const body = document.querySelector("body");
const headerNav = document.querySelector(".header-nav");
const texts = document.querySelectorAll(".text");

toggleButton.addEventListener("click", function(){

    toggleButton.textContent = "다크모드";

    //버튼 클릭시마다 classList의 toggle로 class 추가
    toggleButton.classList.toggle("toggle-button-darkmode");
    body.classList.toggle("body-background-darkmode");
    headerNav.classList.toggle("text-darkmode");
    // bookmarkWrapper.classList.toggle("text-darkmode");

    for (let i=0; i<texts.length;i++){
        texts[i].classList.toggle("text-darkmode");
    }


    //classList의 contains
    if(toggleButton.classList.contains("toggle-button-darkmode")){
        toggleButton.textContent = "일반모드";
    }
})


// 구글 이동
const searchInput = document.querySelector(".search-input");
searchInput.addEventListener("keyup", function(e){
    console.log(e);

    // e.code === "Enter"일때 특정 위치로 이동시킨다.
    if(e.code === "Enter"){


        // 유효성 검사, 빈값인 경우 검색어 입력 안했다고 경고
        if (!e.target.value){
            alert("검색어를 입력하지 않았습니다!");
            return;
        }

        // https://www.google.com/search?q=내용
        const target = "https://www.google.com/search?q="

        // 이동하는 두 가지 방법
        // 첫번째: 그냥 이동 -> location.href
        // location.href = "https://www.google.com/search?q=" + e.target.value;
        // 두번째: 새 탭 이동 -> window.open
        window.open(target + e.target.value);
    }
>>>>>>> bd9deaa0376a03549404e8548c7d9025bd239699
})