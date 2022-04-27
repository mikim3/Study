
// es5
function zoo() {
    console.log('zoo');
};
zoo()
// es5 일급객체이용 함수를 변수에 담음
const yoo = function() {
    console.log('yoo');
};
yoo()
// 화살표 함수
const too = () => {
    console.log('too');
};
too()

// 화살표함수: return 키워드 생략
const yoo2 = function() {
    return 'yoo2';
};
console.log(yoo2());

// 화살표 함수 : return 키워드 생략
// () => ('return값');  이런식으로 해도 리턴값이 넘겨짐
const foo2 = () => ( 'foo2' );
const boo2 = () => { return 'boo2' };
console.log(foo2());
console.log(boo2());