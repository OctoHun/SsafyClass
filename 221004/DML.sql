CREATE TABLE users (
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTEGER NOT NULL
);

SELECT first_name, age FROM users;

SELECT * FROM users;
-- 전체 출력 해도 rowid 안나옴

SELECT rowid, first_name FROM users;
-- 명시를 해주면 숨겨져있던 rowid 출력 가능

SELECT first_name, age FROM users ORDER BY age;

SELECT first_name, age FROM users ORDER BY age DESC;

SELECT first_name, age, balance FROM users ORDER BY age, balance DESC;

SELECT DISTINCT country FROM users;
-- 중복 제거

SELECT DISTINCT first_name, country FROM users;
-- 둘 모두 중복이어야 중복 체크

SELECT first_name, age, balance FROM users WHERE age >= 30 AND balance > 500000;

SELECT first_name, last_name FROM users WHERE first_name LIKE '%준';