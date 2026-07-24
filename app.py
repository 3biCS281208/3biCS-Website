from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return r'''
<!DOCTYPE html>
<html lang="vi">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>3biCS Website</title>

<style>

*{
margin:0;
padding:0;
box-sizing:border-box;
font-family:Arial,sans-serif;
}

html{
scroll-behavior:smooth;
}

body{

background:#16181d;

color:#ffffff;

}

.header{

background:linear-gradient(135deg,#00b894,#0984e3);

padding:40px 20px;

text-align:center;

box-shadow:0 5px 25px rgba(0,0,0,.4);

}

.logo{

font-size:42px;

font-weight:bold;

margin-bottom:10px;

}

.subtitle{

font-size:20px;

opacity:.95;

margin-bottom:20px;

}

.intro{

max-width:900px;

margin:auto;

line-height:1.8;

font-size:17px;

}

.container{

max-width:900px;

margin:auto;

padding:20px;

}

.title{

font-size:28px;

margin:30px 0 20px;

color:#00e5ff;

font-weight:bold;

}

.card{

background:#242731;

border-radius:16px;

margin-bottom:12px;

overflow:hidden;

transition:.3s;

box-shadow:0 2px 10px rgba(0,0,0,.2);

}

.card:hover{

transform:translateY(-2px);

box-shadow:0 5px 20px rgba(0,0,0,.4);

}

.card-header{

padding:18px;

display:flex;

justify-content:space-between;

align-items:center;

cursor:pointer;

font-size:18px;

font-weight:bold;

}

.arrow{

font-size:20px;

color:#00e5ff;

transition:.25s;

}

.content{

display:none;

padding:18px;

border-top:1px solid #333;

background:#1f2128;

line-height:1.8;

font-size:16px;

animation:fade .25s;

}

@keyframes fade{

from{

opacity:0;

transform:translateY(-8px);

}

to{

opacity:1;

transform:translateY(0);

}

}

.community{

background:#1d2027;

padding:18px;

border-radius:16px;

margin-top:18px;

}

.link{

display:block;

text-decoration:none;

margin:12px 0;

padding:16px;

border-radius:12px;

color:white;

font-weight:bold;

transition:.25s;

}

.telegram{

background:#229ED9;

}

.facebook{

background:#1877F2;

}

.link:hover{

transform:scale(1.02);

}

.footer{

text-align:center;

padding:40px 20px;

color:#cfcfcf;

line-height:1.8;

font-size:15px;

}

@media(max-width:700px){

.logo{

font-size:34px;

}

.subtitle{

font-size:17px;

}

.title{

font-size:24px;

}

.card-header{

font-size:17px;

}

}

</style>

</head>

<body>

<div class="header">

<div class="logo">

🎮 3biCS Website

</div>

<div class="subtitle">

Counter-Strike 1.6 Mobile

</div>

<div class="intro">

Được phát triển bởi <b>QuanMods</b>

<br><br>

Dự án cộng đồng Counter-Strike 1.6 dành cho Mobile.

<br><br>

⭐ Không chỉ chia sẻ Mod.

<br>

Tôi mong muốn gìn giữ giá trị của Counter-Strike 1.6 Mobile & PC.

<br>

Tựa game FPS hay nhất mọi thời đại.

</div>

</div>

<div class="container">

<div class="title">

📚 KHÁM PHÁ

</div><div class="card">

<div class="card-header" onclick="toggle('cs')">

<span>📖 Counter-Strike là gì?</span>

<span class="arrow" id="arrow-cs">▶</span>

</div>

<div class="content" id="cs">

<h3>Counter-Strike là gì?</h3>

<br>

<p>

Counter-Strike (CS) là dòng game bắn súng góc nhìn thứ nhất (FPS) được phát triển từ bản Mod của Half-Life và được tạo ra bởi •Lê Minh• Anh ta còn được biết đến bởi nickname trên mạng là Gooseman, là một nhà sản xuất trò chơi máy tính người Canada gốc Việt, đã sáng tạo nên bản mod Half-Life nổi tiếng Counter-Strike Huyền Thoại với Jess Cliffe vào năm 1999

Người chơi sẽ chia thành hai phe:

<br><br>

🔵 Counter-Terrorists (Chống khủng bố)

<br>

🔴 Terrorists (Khủng bố)

<br><br>

Hai đội sẽ chiến đấu để hoàn thành mục tiêu Đặt Bomb hoặc tiêu diệt toàn bộ đối phương để dành Chiến Thắng!

Counter-Strike được xem là một trong những tựa game FPS kinh điển nhất mọi thời đại và cũng là 1 tượng đài của dòng game FPS

</p>

</div>

</div>

<div class="card">

<div class="card-header" onclick="toggle('mode')">

<span>🎮 Chế Độ Chơi</span>

<span class="arrow" id="arrow-mode">▶</span>

</div>

<div class="content" id="mode">

<h3>Các chế độ phổ biến</h3>

<br>

🧟 Zombie Mode Mod

<br><br>

⚔️ Team DeathMatch

<br><br>

🎯 Solo

<br><br>

🔫 AWP Only

<br><br>

💣 Đặt Bomb⭐

<br><br>

🏃🏽 Parkout & Bunny Hop

</div>

</div>

<div class="card">

<div class="card-header" onclick="toggle('mod')">

<span>🛠️ Mod là gì?</span>

<span class="arrow" id="arrow-mod">▶</span>

</div>

<div class="content" id="mod">

<p>

Mod (Modification) là những thay đổi được cộng đồng tạo ra nhằm thay đổi giao diện, âm thanh, nhân vật, vũ khí hoặc thêm tính năng mới cho trò chơi và đặc biệt Mod không thể được nhìn thấy bởi người chơi khác!

<br><br>

CS1.6 Mobile có thể Mod:

<br><br>

🎨 Giao diện

<br>

🔫 Skin súng

<br>

👤 Skin nhân vật

<br>

🎵 Âm thanh

<br>

💥 Hiệu ứng

<br>

📦 Menu

<br>

🌄 Background

</p>

</div>

</div>

<div class="card">

<div class="card-header" onclick="toggle('sound')">

<span>🎙️ Âm Thanh</span>

<span class="arrow" id="arrow-sound">▶</span>

</div>

<div class="content" id="sound">

🎤 Ngọc Trinh Voice

<br><br>

👧 Anime Girl Voice

<br><br>

🎵 Radio Sound

<br><br>

🔊 Weapon Sound

</div>

</div>

<div class="card">

<div class="card-header" onclick="toggle('gallery')">

<span>📸 Thư Viện Hình Ảnh CS1.6</span>

<span class="arrow" id="arrow-gallery">▶</span>

</div>

<div class="content" id="gallery">


<img src="data:image/png;base64,BASE64_ANH_1" width="100%" style="border-radius:10px;">

<img src="data:image/png;base64,BASE64_ANH_2" width="100%" style="border-radius:10px;">

<img src="data:image/png;base64,BASE64_ANH_3" width="100%" style="border-radius:10px;">

</div>

</div>

</div>

<div class="title">

🌐 CỘNG ĐỒNG

</div>

<div class="community">

<a class="link telegram"

href="https://t.me/+pfADBNFr_c8yMDFl"

target="_blank">

👥 Tham Gia 3biCS Group Telegram

</a>

<a class="link facebook"

href="https://www.facebook.com/share/1A6coTFgR1/"

target="_blank">

🔵 Facebook QuanMods

</a>

</div><div class="footer">

💬 "Khám phá Counter-Strike 1.6 Mobile từ những điều cơ bản đến các bản Mod chất lượng."

<br><br>

⭐ Hàng Việt Nam Chất Lượng Cao

<br><br>

© 2026 QuanMods | 3biCS Website

</div>

<script>

function toggle(id){

const blocks=document.querySelecifrAll(".content");
const arrows=document.querySelectorAll(".arrow");

blocks.forEach(function(item){

if(item.id!=id){

item.style.display="none";

}

});

arrows.forEach(function(item){

item.innerHTML="▶";

});

let x=document.getElementById(id);
let arrow=document.getElementById("arrow-"+id);

if(x.style.display=="block"){

x.style.display="none";

arrow.innerHTML="▶";

}else{

x.style.display="block";

arrow.innerHTML="▼";

}

}

</script>

</body>

</html>

'''

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )
