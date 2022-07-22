const btn = document.createElement("button");
// 버튼 태그를 만들기만 함. 아직 안보임

btn.setAttribute("class", "bts");

const txt = document.createTextNode("민코월드");
// 텍스트 만들기만 함.

btn.append(txt);
// 버튼에 텍스트 추가. 여전히 안보임

document.querySelector("body").append(btn);
// body 안에 추가. 이제 보임