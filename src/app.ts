import { Socket } from "dgram";
import express, { Request, Response } from "express";
import { createServer } from "http";
import { Server } from "socket.io";

const PORT: number = 5000;

const app = express();
app.use(express.json());
const httpServer = createServer(app);
const io = new Server(httpServer);

interface IPInfo {
  ip: String;
  port: String;
}

var ips: { [id: string]: IPInfo } = {};

app.get("/", (req: Request, res: Response) => {
  return res.send("Inavlid route. Try /ip/:id");
});

app.post("/ip/:id", (req: Request, res: Response) => {
  const { id } = req.params;

  ips[id] = { ip: req.body.ip, port: req.body.port };
  console.log(`POST /ip/${id}: ${ips[id]}`);

  return res.send("Posted");
});

app.get("/ip/:id", (req: Request, res: Response) => {
  const { id } = req.params;

  console.log(`GET /ip/${id}: ${ips[id]}`);

  var ip: String = "none";
  var port: String = "none";
  if (ips[id] != undefined) {
    ip = ips[id].ip;
    port = ips[id].port;
  }

  return res.json({
    id: id,
    ip: ip,
    port: port,
  });
});

app.get("/ips", (req: Request, res: Response) => {
  let jsonObj = [];
  for (let key in ips) {
    if (ips[key] != undefined) {
      jsonObj.push({
        id: key,
        ip: ips[key].ip,
        port: ips[key].port,
      });
    }
  }

  return res.json(jsonObj);
});

io.on("connect", (socket) => {
  console.log(`Client ${socket.id} connected.`);
  socket.emit("message", "You've connected");
});

io.on("message", (msg) => {
  console.log(`${msg}`);
});

httpServer.listen(PORT, () => {
  console.log(`Application listening at http://localhost:${PORT}`);
});
