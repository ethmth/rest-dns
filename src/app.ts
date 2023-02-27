import express, { Request, Response } from "express";

const PORT: number = 5000;

const app = express();
app.use(express.json());

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
    ip: ip,
    port: port,
  });
});

app.get("/ips", (req: Request, res: Response) => {
  //  console.log(ips.map);
  let jsonObj = [];
  for (let key in ips) {
    console.log(`${key} and ${ips[key]}`);
    console.log(ips[key]);

    if (ips[key] != undefined) {
      jsonObj.push({
        ip: ips[key].ip,
        port: ips[key].port,
      });
    }
  }

  return res.json(jsonObj);
  // const new = ips.map((ip) => `NEW${ip}`);
});

app.listen(PORT, () => {
  console.log(`Application listening at http://localhost:${PORT}`);
});
