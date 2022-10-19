// console.log('hello, js')

// function add(num1, num2) {
//   return num1 + num2
// }
// const sub = function (num1, num2) {
//   return num1+num2
// }
// console.log(add(2, 7))
// console.log(sub(2, 7))

// 함수 선언식은 호이스팅 발생
// 따라서 표현식 권장

const greeting = function (name = 'Anonymous') {
  return `Hi ${name}`
}
console.log(greeting())

// 화살표 함수: 표현식에서만 사용 가능
// 1단계 function 키워드 삭제
// 2단계 인자가 1개일 경우 () 생량 가능(명확성과 일관성을 위해 그냥 쓰는걸 권장)
// 2-1 인자 없다면 ()나 _로 표시 가능
// 3단계 함수 바디가 return을 포함한 표현식 1개일 경우에 {}와 return 삭제 가능
// 3-1 object return시 return 명시적으로 붙여줌
// 3-2 return 안적으려면 소괄호로 감싸줌

// 즉시 실행 함수
// function(num) {return num ** 3 })(2) 
// ((num) => num ** 3)(2)

/*
배열
array.length로 길이 접근 가능
  메서드 기초
  reverse: 원본 배열의 요소들의 순서를 반대로 정렬
  push & pop: 배열의 가장 뒤에 요소를 추가 제거
  unshift & shift: 배열의 가장 앞에 요소를 추가 제거
  includes: 배열에 특정 값이 존재하는지 판별(참/거짓)
  indexOf: 배열에 특정 값이 존재하는지 판별 후 첫 번째 값의 인덱스 반환(없으면 -1)
  join: 배열의 모든 요소를 구분자를 이용하여 연결(array.join([separator] 생략시 쉼표)
  
  메서드 심화
  배열을 순회하며 특정 로직 수행, 메서드 호출 시 인자로 callback함수를 받음
  forEach: 배열의 각 요소에 대해 콜백함수 한 번씩 실행(반환값 없음)
  map: 콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환
  filter: 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열 반환
  reduce: 콜백 함수의 반환 값들을 하나의 값(acc)에 누적 후 반환
  find: 콜백 함수의 반환값이 참이면 해당 요소를 반환
  some: 배열의 요소중 하나라도 판별 함수 통과시 참 반환
  every: 배열의 모든 요소가 판별 함수를 통과시 참 반환
*/

/*
객체
  key는 문자열 타입만 가능
  객체 요소 접근은 (.)점 또는 ([])대괄호로 가능
  ES6 이후로 객체 생성 및 조작에 유용하게 사용 가능한 문법들 생김
    1. 속성명 축약: 객체를 정의할때 key와 할당하는 변수 이름 같을시 하나만 씀
    2. 메서드명 축약: 메서드 선언시 function 키워드 생략 가능
    3. 계산된 속성명 사용하기: 객체를 정의할 때 key의 이름을 표현식을 사용하여 동적으로 생성 가능(key를 대괄호로 감싸줘야함)
    4. 구조 분해 할당: 배열 또는 객체를 분해하여 속성을 변수에 쉽게 할당할 수 있는 문법(변수명을 중괄호에 넣어줌)
    5. 객체 전개 구문(Spread Operator): 배열과 마찬가지로 전개 구문(...)을 사용해 객체 내부에서 전개 가능(얕은 복사에 활용 가능)
*/

/*
객체 관련 문법
  JavaScript Object Notation(JSON)
  json은 형식이 있는 문자열이고 Object는 그 자체로 타입이다.
  따라서 json을 Object로 바꿔야 함.
  [참고] 배열은 객체다
    배열은 키와 속성들을 담고있는 참조 타입의 객체
    배열은 인덱스를 키로 가지며 length도 키로 가지고 있음. 그래서 arr.length 사용 가능
    
*/