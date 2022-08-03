'''
파이썬 기초

데이터 저장
 1.변수
   - 데이터를 하나 저장하는 것
 2.리스트
    -데이터를 여러 개 저장하는 것
 3.딕셔너리
    -사전형 데이터를 의미하며 key : value 를 1:1 로 대응시킨 형태

조건문

 1.if
    -만약 ~~ 라면
 2.if / else
    -만약 ~~ 라면 / 그것이 아니라면
 3.if / elif / else
    -else if 의 줄임말
    -만약 ~~ 라면 / 만약 ~~ 이 아닌데 이것이라면 / 모두 아니라면

반복문
 1.while
    -for문과의 차이점 : 종료 조건이 필요하다
 2.for
    -while문과의 차이점 : 종료 조건이 필요없다 ( 반복하는 범위를 지정하므로 )
함수
  -왜 쓰는가 ? 반복되는 코드 덩어리를 묶어놓기 위해
모듈
  -정의 : 함수와 변수를 모아둔 파이썬 파일
  -왜 쓰는가 ? 코드를 편하게 보기 위해 + 배포를 편하게 하기위해'''

#1~10까지 숫자를 하나씩 출력해라
# while문 조건이 True인 동안 반복적으로 실행 되기에 종료조건이 반드시 필요
n = 1
while n<=10:
    print(n, end='')
    n+=1

