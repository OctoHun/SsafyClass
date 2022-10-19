const numbers = [1, 2, 3]

// 1단계
// const doubleFunc = function (number) {
//   return number * 2
// }
// const doubleNumbers = numbers.map(doubleFunc)
// console.log(doubleNumbers)

// 2단계
// const doubleNumbers = numbers.map(function (number) {
//   return number * 2
// })
// console.log(doubleNumbers)

// 3단계
// const doubleNumbers = numbers.map((number) => {
//   return number * 2
// })

// 4단계
const doubleNumbers = numbers.map((number) => number * 2)
console.log(doubleNumbers)