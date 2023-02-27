import express, { Request, Response } from "express";

const PORT: number = 5000;

const app = express();

interface IPInfo {
  ip: String;
  port: String;
}

app.use(express.json());
//app.use(express.urlencoded({ extended: true }));

var ips: { [id: string]: IPInfo } = {};

app.get("/", (req: Request, res: Response) => {
  return res.send("Inavlid route. Try...");

  //  return res.redirect("https://ethanmt.com/");
  return res.json({
    success: true,
    name: "TomDoesTech",
  });
});

app.post("/ip/:id", (req: Request, res: Response) => {
  const { id } = req.params;

  // var myip: String = req.body.json("ip");
  //console.log(req.body);
  //console.log(req.body.ip);

  ips[id] = { ip: req.body.ip, port: req.body.port };

  return res.send(200);
});

app.get("/ip/:id", (req: Request, res: Response) => {
  const { id } = req.params;

  console.log(ips[id]);

  var ip: String = "none";
  var port: String = "none";
  if (ips[id] != undefined) {
    //console.log(ips[id].ip);
    ip = ips[id].ip;
    port = ips[id].port;
  }

  // return res.status(200);
  //if (ips[id] !== null) {
  return res.json({
    ip: ip,
    port: port,
  });
  //}
});

app.listen(PORT, () => {
  console.log(`Application listening at http://localhost:${PORT}`);
});
