// 웹서버 연결없이 데이터베이스 저장만
// virtual_test1.js

var mongoose = require('mongoose');

var database;
var UserSchema;
var UserModel;

function connectDB() {
   var databaseUrl = "mongodb://localhost:27017/local"

       mongoose.Promise = global.Promise;  // mongoose의 Promise 객체는 global의 Promise 객체 사용하도록 함
	mongoose.connect(databaseUrl);
	database = mongoose.connection;
		
	database.on('open', function () {
		console.log('데이터베이스에 연결되었습니다. : ' + databaseUrl);

                // user 스키마 및 모델 객체 생성
		createUserSchema();

		// test 진행
                doTest();

	});
	
	database.on('disconnected', function() {
            console.log('연결이 끊어졌습니다. 5초 후 재연결합니다.');
            setInterval(connectDB, 5000);
        }); 
	database.on('error', console.error.bind(console, 'mongoose connection error.'));
}
// user 스키마 및 모델 객체 생성

function createUserSchema() {
		UserSchema = mongoose.Schema({
		    id: {type: String, required: true, unique: true},
		//  password: {type: String, required: true},
		    name: {type: String, index: 'hashed'},
		    age: {type: Number, 'default': -1},
		    created_at: {type: Date, index: {unique: false}, 'default': Date.now},
		    updated_at: {type: Date, index: {unique: false}, 'default': Date.now}
		});
                
                console.log("UserSchema 정의함");

                UserSchema.virtual('info')
                     .set(function(info) {
                        var splitted = info.split(' ');
                        this.id = splitted[0];
                        this.name = splitted[1];
                        console.log('virtual info 속성 설정됨 : ' + this.id + ', ' +
                                                                    this.name);
                      })
                     .get(function() {return this.id + ' ' + this.name});
		
                UserModel = moongoose.model("users4", UserSchema);  
         
		console.log('UserSchema 정의함.');


		// 스키마에 static으로 findById 메소드 추가
		UserSchema.static('findById', function(id, callback) {
			return this.find({id:id}, callback);
		});
		
                // 스키마에 static으로 findAll 메소드 추가
		UserSchema.static('findAll', function(callback) {
			return this.find({}, callback);
		});
	
};

function doTest() {
    var user = new UserModel({"info: "test01 소녀시대"});

    user.save(function(err) {
       if(err) {
          console.log('에러 발생.');
          return;
       }
       console.log('데이터 추가함.');

       findAll();

       console.log('info 속성에 값 할당함.');
       console.log('id: %s, name: %s', user.id, user.name);
    });
}
		
connectDB();