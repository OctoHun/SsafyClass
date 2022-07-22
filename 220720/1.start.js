const family = ["아빠", "엄마", "실비"];

const info = {
  userName: "이자룡",
  job: "싸피강사",
  ismarriged: true,
  family: family,
  myStack: {
    frontend: "vue.js",
    backend: "node.js",
  },
  add: function (a, b) {
    return a + b;
  },
};

console.log(info.userName);
console.log(info.family[1]);
console.log(info.myStack.frontend);
console.log(info.add(1,3));