// ./01built_in_module/stream.js
var fs = require('fs');

var os = fs.createWriteStream('./output.txt');

os.on('finish', function() {
	console.log('finish!');
});

// 여기에 작성
 
// 컨트롤 c할때까지 계속 입력받음
var is = process.stdin;
//
is.pipe(os);
