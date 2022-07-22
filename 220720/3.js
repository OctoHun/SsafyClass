// console.log("hi");
// console.log(document.querySelector("h1").textContent);
// document.querySelector("h1").textContent = "ㅎㅎ";
// document.querySelector(".lalala").textContent = "ㅎㅎㅎ";
// querySelector는 맨 처음 찾은 한가지만

const lalalas =  document.querySelectorAll(".lalala");
console.log(lalalas[0].textContent);
console.log(lalalas[1].textContent);
console.log(lalalas[2].textContent);

for(let i=0;i<3;i++)
{
  console.log(lalalas[i].textContent = "성훈");
}