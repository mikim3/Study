// ./05express/app01.js



// 기본 포트를 app 객체에 속성으로 설정
app.set('port', process.env.PORT || 3000);

// Express 서버 시작
http.createServer(app).listen(app.get('port'), () => {
  console.log('server on : ' + app.get('port'))
});
