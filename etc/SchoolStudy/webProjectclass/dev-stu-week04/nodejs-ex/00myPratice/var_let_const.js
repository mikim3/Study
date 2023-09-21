//var let 
// var : 함수 유효범위
// let, const: 블록 유효범위(블록 밖에서 변수 접근불가)
console.log("Hello World");

var foo = 100;
console.log("foo:",foo); //100

var foo = 200; 
console.log("foo_change:",foo); //200

// let은 같은 변수명으로 두번선언 금지
let boo=2;
// let boo=3; //error
console.log("boo: ",boo); // 2
boo=3;
console.log("boo_change: ",boo); //3

//const 걍 상수 내용 값을 바꾸면 오류 출력
const a = 0;
// a = 1; //error
console.log(a); //0

/////////////////////////////////////
/// scope 알아보기
// var: 영역(scope) 벗어나도 변경된 값 유지
// let과 범위(scope)가 다르다.

var foo = 'foo1';
console.log(foo); // foo1
if(1) {
    var foo = 'foo2'
    console.log(foo); // foo2
}
console.log(foo); // foo1

//let: if문 안에 bar와 if 문 밖에 bar는 다른 변수이다.
// 블록 유효범위
let bar = 'bar1';
console.log(bar);  //bar1
if(1){
    let bar = 'bar2'  // 새로 선언안하고 bar = 'bar2'를 하면 밖에 있는 것도 바뀐다.
    console.log(bar);  //bar2
}
console.log(bar);   //bar1











