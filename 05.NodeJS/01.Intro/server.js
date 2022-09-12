const express = require('express');
const app = express();

app.listen(8888, function(){
    console.log('listening on 8888')
});

app.get('/', function(request, response){
    response.sendFile(__dirname + '/index.html')
});

app.get('/hello', function(request, response){
    response.send('world')
});

app.get('/foo', function(request, response){
    response.send('bar')
});
