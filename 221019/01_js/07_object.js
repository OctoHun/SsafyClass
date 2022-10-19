// const myInto = {
//   name: 'jack',
//   phoneNumber: '123456',
//   'samsung products': {
//     buds: 'Galaxy Buds pro',
//     galaxy: 'Galaxy s99',
//   },
// }
// console.log(myInto.name)
// console.log(myInto['phoneNumber'])
// console.log(myInto['samsung products'])
// console.log(myInto['samsung products'].buds)
// console.log(myInto['samsung products']['buds'])


// // 메서드명 축약
// const obj = {
//   greeting() {
//     console.log('Hi')
//   }
// }
// obj.greeting()


// // 구조 분해 할당
// const userInformation = {
//   username: 'ssafy kim',
//   userId: 'ssafyStudent1234'
// }
// const { username, userId } = userInformation
// console.log(username, userId)


// 객체 관련 문법
const jsonData = {
  coffee: 'Americano',
  iceCream: 'Mint Choco',
}

// Object -> json
const objToJson = JSON.stringify(jsonData)
console.log(objToJson)
console.log(typeof objToJson)

// json -> Object
const jsonToObj = JSON.parse(objToJson)
console.log(jsonToObj)
console.log(typeof jsonToObj)
console.log(jsonToObj.coffee)