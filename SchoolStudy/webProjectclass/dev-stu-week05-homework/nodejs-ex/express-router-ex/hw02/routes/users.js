// ./routes/users.js
const express = require('express');
let router = express.Router();


router.get('./users/:id GET', (req,res,next) =>{
    res.send('사용자 정보 가져오기');
});

router.post('/users POST',(req,res,next)=> {
    res.send('회원가입')
})

router.post('/users/:id PUT' function()




사용자 API
/users/:id GET 사용자 정보 가져오기
/users POST 회원 가입
/users/:id PUT 회원 정보 수정
/users/:id DELETE 회원 탈퇴