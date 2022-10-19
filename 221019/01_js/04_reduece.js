const numbers = [90, 90, 80, 77, 100]
// 1단계
// const sum = numbers.reduce(function (result, number) {
//   return result + number
// }, 0)

// 3단계
// const sum = numbers.reduce((result, number) => {
//   return result + number
// }, 0)

// 4단계
const sum = numbers.reduce((result, number) => 
result + number, 0) / numbers.length
