require("dotenv").config();
const express = require("express");
const mongoose = require("mongoose");
const bodyParser = require("body-parser");
const nodemailer = require("nodemailer");

var d = new Date();
var date = d.getDate();

const app = express();

app.set("view engine", "ejs");
app.use(express.static("public"));
app.use(bodyParser.urlencoded({ extended: true }));

mongoose.connect(
  process.env.MONGO_STRING
);

app.get("/home", function (req, res) {
  // res.render("home");
  res.sendFile(__dirname + "/index.html");
});


const scrapSchema = new mongoose.Schema({
  Link: { type: String, required: true },
  Price: { type: Number, required: true },
  Email: { type: String, required: true },
  time: { type: String, default: new Date().toLocaleDateString() },
  noofdays: { type: Number },
});

const stockSchema=new mongoose.Schema({
     
  Symbol:String,
  minPrice:Number,
  maxPrice:Number,
  Email:String,
  time: { type: String, default: new Date().toLocaleDateString() },
  noofdays: { type: Number }
  
});



const ScrapModel = mongoose.model("Prod", scrapSchema);

const stockModel=mongoose.model("Stock",stockSchema);



app.get("/:products", function (req, res) {
  // res.render("home");
  res.sendFile(__dirname + "/public/products.html");
});






app.post("/", function (req, res) {
  const email = req.body.prodEmail;
  const productlink=req.body.prodLink;
  const price=req.body.prodPrice;
  const posting = new ScrapModel({
    Link: req.body.prodLink,
    Price: req.body.prodPrice,
    Email: req.body.prodEmail,
    noofdays: req.body.duration,
  });

  posting.save();

  res.redirect("/products");

  const transporter = nodemailer.createTransport({
    service: "Gmail",
    auth: {
      user: "scraptivists@gmail.com",
      pass: process.env.EMAIL_PASS,
    },
  });
  //testing
  const mailOptions = {
    from: "it.160320737020@gmail.com",
    to: email,
    subject: "Confirmation of Details",
    text: `Dear Customer,

  This is an email to confirm the details you provided for monitoring the price. We appreciate your interest and look forward to your participation.

  1.product:${productlink}
  2.Target price:${price}

  Please take a moment to review the above details and kindly notify us if there are any changes or corrections that need to be made. Your satisfaction is our priority. 
  If you have any questions or require further assistance, feel free to contact us at scraptivists@gmail.com. We are here to help and will be more than happy to assist you.
  Thank you for providing the necessary information.
    
  Best regards,
  Team Price Notifier 
     `
  };

  transporter.sendMail(mailOptions, (error, info) => {
    if (error) {
      console.log("Error sending email:", error);
      res.status(500).send("Error sending OTP");
    } else {
      console.log("OTP sent:", info.response);
      // res.sendFile(__dirname + "/ver.html");
    }
  });
});







app.get("/:stockcrypto", function (req, res) {
  // res.render("home");
  res.sendFile(__dirname + "/public/stockscrypto.html");
});
app.post("/dbs", function (req, res) {

  const email=req.body.scEmail;
  const symbol=req.body.scSymbol;
  const minprice=req.body.scMinPrice;
  const maxprice=req.body.scMaxPrice;
  const days=req.body.duration;
 
  const posting = new stockModel({
    Symbol: req.body.scSymbol,
    Email: req.body.scEmail,
    minPrice:req.body.scMinPrice,
    maxPrice:req.body.scMaxPrice,
    noofdays: req.body.duration,
  });

  posting.save();

  // res.redirect("/stockcrypto");
  res.sendFile(__dirname + "/public/stockscrypto.html");

  const transporter = nodemailer.createTransport({
    service: "Gmail",
    auth: {
      user: "scraptivists@gmail.com",
      pass: process.env.EMAIL_PASS,
    },
  });
  //testing
  const mailOptions = {
    from: "it.160320737020@gmail.com",
    to: email,
    subject: "Confirmation of Details",
    text: `Dear Customer,

  This is an email to confirm the details you provided for monitoring the price. We appreciate your interest and look forward to your participation.

  Stock/Crypto:${symbol}
  Min Price:${minprice}
  Max Price:${maxprice}

  Please take a moment to review the above details and kindly notify us if there are any changes or corrections that need to be made. Your satisfaction is our priority. 
  If you have any questions or require further assistance, feel free to contact us at scraptivists@gmail.com. We are here to help and will be more than happy to assist you.
  Thank you for providing the necessary information.
    
  Best regards,
  Team Price Notifier 
     `
  };

  transporter.sendMail(mailOptions, (error, info) => {
    if (error) {
      console.log("Error sending email:", error);
      res.status(500).send("Error sending OTP");
    } else {
      console.log("OTP sent:", info.response);
      // res.sendFile(__dirname + "/ver.html");
    }
  });
});

app.listen(3000, function (req, res) {
  console.log("Listening");
});
