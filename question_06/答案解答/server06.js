const express = require('express');
const app = express();
const encparams = require('./0606.js');
var bodyParser = require('body-parser');

app.use(bodyParser());

app.post('/encrypt',function(req,res){
    var request = req.body;
    console.log('收到客户端消息',request);
    result = encparams.get_m(request['timestamp'],request['count']);
    console.log(result);
    res.send(result);
});

app.listen(3000,()=>{
    console.log('开启服务，端口3000');
})
