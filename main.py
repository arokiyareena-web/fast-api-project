from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Website Layout</title>
        <style>
            body{
                margin:0;
                font-family:Arial, sans-serif;
            }

            header{
                background:#333;
                color:white;
                text-align:center;
                padding:20px;
            }

            nav{
                background:#555;
                display:flex;
                justify-content:center;
            }

            nav a{
                color:white;
                padding:14px 20px;
                text-decoration:none;
            }

            nav a:hover{
                background:#777;
            }

            .hero{
                background:#eaeaea;
                text-align:center;
                padding:80px 20px;
                font-size:32px;
            }

            .container{
                display:flex;
                padding:20px;
            }

            .sidebar{
                width:25%;
                background:#f4f4f4;
                padding:20px;
            }

            .content{
                width:75%;
                padding:20px;
            }

            .card{
                background:#eee;
                padding:15px;
                margin-bottom:15px;
            }

            footer{
                background:#333;
                color:white;
                text-align:center;
                padding:15px;
            }
        </style>
    </head>

    <body>

        <header>
            <h1>My Website</h1>
            <p>FastAPI HTML Layout Example</p>
        </header>

        <nav>
            <a href="#">Home</a>
            <a href="#">Services</a>
            <a href="#">Portfolio</a>
            <a href="#">Contact</a>
        </nav>

        <section class="hero">
            Welcome to My Website
        </section>

        <div class="container">

            <aside class="sidebar">
                <h3>Sidebar</h3>
                <ul>
                    <li>About</li>
                    <li>Blog</li>
                    <li>Projects</li>
                </ul>
            </aside>

            <main class="content">
                <div class="card">
                    <h2>Article Title</h2>
                    <p>This page is returned directly as HTML from FastAPI.</p>
                </div>

                <div class="card">
                    <h2>Another Section</h2>
                    <p>You can add more content here.</p>
                </div>
            </main>

        </div>

        <footer>
            <p>© 2026 My Website</p>
        </footer>

    </body>
    </html>
    """

@app.get("/test")
async test():
    return {"test":"App is working"}