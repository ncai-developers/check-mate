const jsonServer = require('json-server');
const jwt = require('express-jwt');
const express = require('express');

//const server = jsonServer.create()
const router = jsonServer.router('db.json');
const middlewares = jsonServer.defaults();

var server = express();
// ...

// You may want to mount JSON Server on a specific end-point, for example /api
// Optiona,l except if you want to have JSON Server defaults
// server.use('/api', jsonServer.defaults());
//server.use('/api', router);

// server.use(middlewares)
server.use(router);
//
server.use('/api', jwt({
  secret: new Buffer('secretpassword', 'base64'),
  //credentialsRequired: false,
  getToken: function(req) {
    console.log(arguments);
    if (req.headers.authorization && req.headers.authorization.split(' ')[0] === 'Bearer') {
        return req.headers.authorization.split(' ')[1];
    } else if (req.query && req.query.token) {
      return req.query.token;
    }
    return null;
  }
}), ()=>{
    console.log(arguments);
});
server.listen(3000, () => {
  console.log('JSON Server is running')
})
