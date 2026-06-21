import http.server
import socketserver
import webbrowser
import threading

PORT = 8000


HTML = """
<!DOCTYPE html>
<html>
<head>
<title>All-in-One Hub</title>

<style>
body{
    margin:0;
    font-family:Arial;
    background:linear-gradient(135deg,#141e30,#243b55);
    color:white;
}

.container{
    width:90%;
    margin:auto;
    padding:20px;
}

h1{
    text-align:center;
    color:#00ffd5;
}

.box{
    background:rgba(255,255,255,0.1);
    padding:15px;
    margin:15px 0;
    border-radius:12px;
    backdrop-filter: blur(10px);
}

input{
    padding:8px;
    margin:5px;
    border-radius:6px;
    border:none;
}

button{
    padding:8px 12px;
    border:none;
    background:#00ffd5;
    border-radius:6px;
    cursor:pointer;
    font-weight:bold;
}

table{
    width:100%;
    border-collapse:collapse;
    margin-top:10px;
}

th,td{
    padding:10px;
    text-align:center;
}

th{
    background:#00ffd5;
    color:black;
}

tr:hover{
    background:rgba(255,255,255,0.1);
}

.pwd{
    background:black;
    padding:10px;
    margin-top:10px;
    color:#00ff88;
    word-break:break-all;
}
</style>
</head>

<body>

<div class="container">

<h1>🔥 ALL-IN-ONE HUB</h1>

<div class="box">
<h3>📒 Contact Manager (Client Side)</h3>

<input id="name" placeholder="Name">
<input id="phone" placeholder="Phone">
<input id="email" placeholder="Email">
<button onclick="add()">Add</button>

<table id="table">
<tr>
<th>Name</th>
<th>Phone</th>
<th>Email</th>
</tr>
</table>
</div>

<div class="box">
<h3>🔐 Password Generator</h3>

<input id="len" type="number" placeholder="Length" min="4">
<button onclick="gen()">Generate</button>

<div class="pwd" id="pwd"></div>
</div>

</div>

<script>

let contacts=[];

function add(){
    let n=document.getElementById("name").value;
    let p=document.getElementById("phone").value;
    let e=document.getElementById("email").value;

    if(n && p && e){
        contacts.push({n,p,e});
        render();
    }
}

function render(){
    let t=document.getElementById("table");

    t.innerHTML=`
    <tr>
    <th>Name</th><th>Phone</th><th>Email</th>
    </tr>`;

    contacts.forEach(c=>{
        t.innerHTML+=`
        <tr>
        <td>${c.n}</td>
        <td>${c.p}</td>
        <td>${c.e}</td>
        </tr>`;
    });
}

function gen(){
    let len=document.getElementById("len").value;

    let chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()";
    let pwd="";

    for(let i=0;i<len;i++){
        pwd+=chars[Math.floor(Math.random()*chars.length)];
    }

    document.getElementById("pwd").innerText=pwd;
}

</script>

</body>
</html>
"""


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(HTML.encode())
        else:
            self.send_error(404)


def start():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()


print("🚀 Server running at http://127.0.0.1:8000")

threading.Thread(target=start, daemon=True).start()

webbrowser.open(f"http://127.0.0.1:{PORT}")

input("Press ENTER to stop server...\n")