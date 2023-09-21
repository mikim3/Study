// ./datatype-ex/datatype04.js
// entry 자바스크립트 객체를 JSON stringify() 함수 파라미터로 입력
// stringify() 결과로 JSON 문자열 생성

var entry = {
    profile: {
        name: "희정" ,
        job: "Singer"  
    }
};

// 여기에 작성
// entry를 문자열 형식으로 바꾼다.
var jsonStr = JSON.stringify(entry);
// 그것을 출력
console.log('stringify: ', jsonStr);
