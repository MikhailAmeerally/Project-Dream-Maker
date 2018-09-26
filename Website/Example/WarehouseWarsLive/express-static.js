/* What about serving up static content, kind of like apache? */

var express = require('express');
var app = express();

const sqlite3 = require('sqlite3').verbose();

var bodyParser = require('body-parser');
app.use(bodyParser.json()); // support json encoded bodies
app.use(bodyParser.urlencoded({ extended: true })); // support encoded bodies


var db = new sqlite3.Database('db/database.db', (err) => {
  if (err) {
          console.error(err.message);
  }
  console.log('Connected to the database.');
});

// static_files has all of statically returned content
// https://expressjs.com/en/starter/static-files.html
app.use('/',express.static('static_files')); // this directory has files to be returned

app.listen(10080,function () {
  console.log('Example app listening on port 10080!');
});

app.post('/login/', function (req, res) {
        

  var username = req.body.username;
  var password = req.body.password;


  var sql = 'SELECT * FROM users WHERE id=? AND password=?';
  db.get(sql, [username,password], (err, row) => {
          var result = {};
          if (err) {
                  // Should set res.status!!
                  res.status(409);
                  result["error"] = err.message;
          } else {
                  if(row){
                          console.log(row);
                          res.status(200);
                          result['email'] = row['email'];
                          result['name'] = row['name'];
                          result['gender'] = row['gender'];
                          result['highestScore'] = row['highestScore'];
                  }
                  else{
                    console.log("NO ROW!");
                    res.status(409);
                  }

          }
          res.json(result);
  });
});

app.post('/profile/', function (req, res) {
        
        var username = req.body.username;
        console.log(username);
        var sql = 'SELECT * FROM users WHERE id=?';
        db.get(sql, [username], (err, row) => {
                var result = {};
                if (err) {
                        res.status(409);
                        // Should set res.status!!
                        result["error"] = err.message;
                } else {
                        if(row){
                                res.status(200);
                                result["user"] = row["id"];
                                result["password"] = row["password"];
                                result["name"] = row["name"];
                                result["email"] = row["email"];
                                result["gender"] = row["gender"];
                                result['highestScore'] = row['highestScore'];
                        }
                        else{
                                res.status(409);
                        }

                        
                }
                res.json(result);
        });
});

app.post('/register/', function (req, res) {
        var username = req.body.username;

//      console.log(username, password, name);

        var result = {};
        var sql = 'SELECT * FROM users WHERE id=?';
        db.get(sql, [username], (err, row) => {
                if (err) {
                        // Should set res.status!!
                        res.status(409);
                        result["error"] = err.message;
                } else {
                        if(row){
                                result["error"] = "Already Exists";
                                console.log("username already exists");
                        }
                        else{
                                res.status(200);
                                console.log("available to use username");
                        }

                }
        });
        res.json(result);
});

app.put('/registerput/', function (req, res) {
        var username = req.body.username;
        var password = req.body.password;
        var email = req.body.email;
        var gender = req.body.gender;
        var name = req.body.name;
        result = {};
        //Does not exist.
        var sql = "INSERT INTO users(id,password,name,email,gender,highestScore) VALUES(?,?,?,?,?,0);";
        db.run(sql, [username,password,name,email,gender], function(err){
                if(err){result['error'] = err.message; res.status(409);}
                else{result['registered'] = true; res.status(201); console.log("successfully registered");}
                });

        res.json(result);
});

app.put('/updatePassword/', function (req,res) {
        var username = req.body.username;
        var password = req.body.password;
        result = {};
        var sql = "UPDATE users SET password=? WHERE id = ?";
        db.run(sql, [password,username], function(err){
                if(err){result['error'] = err.message; res.status(409);}
                else{result['update'] = true; res.status(201); console.log("successfully updated password.");}
        });
        res.json(result);
});

app.delete('/delete/', function (req,res) {
        var username = req.body.username;
        var sql = "DELETE FROM users WHERE id= ?";
        db.run(sql,[username], (err,row) => {
                var result = {};
                if(err)
                {
                        res.status(409);
                        result['error'] = err.message;
                } else {
                        res.status(200);
                        result['deleted'] = true;
                }
                res.json(result);
        });

});






