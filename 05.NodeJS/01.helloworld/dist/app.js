"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const express = require("express");
const app = express();
const port = 8888;
app.listen(port, () => {
    console.log('listening on 8888');
});
app.get('/', (request, response) => {
    response.send("hello world!");
});
app.get('/foo', (request, response) => {
    response.send({ "foo": "bar" });
});
//# sourceMappingURL=app.js.map