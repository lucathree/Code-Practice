import * as express from "express";

const app: express.Express = express();
const port: number = 8888;

app.listen(port, () => {
    console.log('listening on 8888')
});

app.get('/', (request: express.Request, response: express.Response) => {
    response.send("hello world!")
});

app.get('/foo', (request: express.Request, response: express.Response) => {
    response.send({"foo": "bar"})
});
