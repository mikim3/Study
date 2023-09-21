// ./01built_in_module/path.js
// 내장보듈도 무조건 require() 을 해야한다.
var pathUtil = require('path');

//
// 경로 분석
//
var path = '/foo/bar/baz/asdf/quux.html';

// /foo/bar/baz/asdf
console.log('dirname : ', pathUtil.dirname(path));
// quux.html
console.log('basename : ', pathUtil.basename(path));
// .html
console.log('extname : ', pathUtil.extname(path));


var parsed = pathUtil.parse('/usr/tmp/local/image.png');
console.log('parsed : ',parsed); // 그냥 parsed 하면 다나옴
console.log('base : ', parsed.base);  // path.parse().parsed.원하는매개변수명 하면 원하는 값나옴  
console.log('ext : ',parsed.ext);

//
// 경로 만들기
//
var newPath = pathUtil.join('/foo', 'bar', 'baz/asdf', 'quux', '..')    // path.join('','','''); 로 경로 합침
// returns
console.log('path.join : ', newPath); // /foo/bar/baz/asdf


var newPath2 = pathUtil.format({
    root : "/",
    dir : "/home/user/dir",
    base : "file.txt",
    ext : ".txt",
    name : "file"
});

console.log('path.format : ', newPath2);