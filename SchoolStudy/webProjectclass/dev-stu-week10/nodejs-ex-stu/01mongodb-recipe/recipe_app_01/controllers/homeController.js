"use strict";

exports.logRequestPaths = (req, res, next) => {
  console.log(`request made to: ${req.url}`);
  next();
};

exports.sendReqParam = (req, res) => {
  let veg = req.params.vegetable;
  res.send(`This is the page for ${veg}`);
};

exports.respondWithName = (req, res) => {
  res.render("index");
};

////////////////////////


//2) mongod 만들기
// mongod --dbpath C:\Users\minsuda\Documents\GitHub\Study\SchoolStudy\webProjectclass\dev-stu-week10\nodejs-ex-stu\01mongodb-recipe\recipe_app_01\database

// cd 
// mongo

// 3) node 만들기  
// cd C:\Users\minsuda\Documents\GitHub\Study\SchoolStudy\webProjectclass\dev-stu-week10\nodejs-ex-stu\01mongodb-recipe\recipe_app_01


