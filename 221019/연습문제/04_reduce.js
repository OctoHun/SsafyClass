// 1. 배열에 담긴 중복된 이름을 {'이름': 수} 형태의 object로 반환하세요.

const names = ['harry', 'aiden', 'julie', 'julie', 'edward']

// answer
const counted = names.reduce((result, theirName) => {
    if (theirName in result) {
        result[theirName] += 1
    } else {
        result[theirName] = 1
    }
    return result
}, {})
console.log(counted)