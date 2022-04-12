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
console.log('parsed : ',parsed);
console.log('base : ', parsed.base);
console.log('ext : ',parsed.ext);

//
// 경로 만들기
//
var newPath = pathUtil.join('/foo', 'bar', 'baz/asdf', 'quux', '..')
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