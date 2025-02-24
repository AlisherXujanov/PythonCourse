*# 🚀 FastHTML

FastHTML is a powerful Python library that brings together Starlette, Uvicorn, HTMX, and fastcore's `FT` "FastTags" to create server-rendered hypermedia applications with minimal code and maximum productivity.

## ✨ Features

- 🎯 **Simple & Intuitive** - Write Python functions that directly render HTML
- ⚡ **High Performance** - Built on Starlette and Uvicorn for blazing fast responses
- 🔄 **HTMX Integration** - Modern interactivity without complex JavaScript
- 🎨 **PicoCSS Included** - Beautiful default styling out of the box
- 🛠️ **Type-Safe** - Leverages Python type hints for automatic request parsing
- 🔌 **WebSocket Support** - Real-time bidirectional communication made easy

## 📦 Installation

```bash
pip install python-fasthtml
```

## 🌟 Quick Start

Create a new file `main.py`:

```python
from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Titled("FastHTML", P("Let's build something amazing!"))

serve()
```

Run it:
```bash
python main.py
```

Visit http://127.0.0.1:5001 to see your app!

## 💡 Examples

### 1. Dynamic Routes
```python
@rt("/hello/{name}")
def get(name: str):
    return Titled(f"Hello {name}!", 
        P(f"Welcome to FastHTML, {name}!"))

# Route Parameters
# This example shows how to use route parameters in FastHTML:

# - `@rt("/hello/{name}")`  - Defines a route with a dynamic `name` parameter
# - `def get(name: str)`    - The parameter is automatically extracted and type-converted to a string
# - `return Titled(...)`    - Returns a titled page with a personalized greeting
# - `P(f"Welcome...")`      - Renders a paragraph with the dynamic name value

# The route will match URLs like `/hello/Alice` or `/hello/Bob` and display a personalized welcome message.
```



### 2. Form Handling
```python
# Define a Profile dataclass to handle form data
@dataclass
class Profile:
    email: str  # Email field as string
    age: int    # Age field as integer

# GET route to display the profile form
@rt("/profile")
def get():
    return Titled("Profile Form",
        Form(method="post")(  # Create a POST form
            Label("Email", Input(name="email")),  # Email input with label
            Label("Age", Input(name="age", type="number")),  # Age input with label and number type
            Button("Save", type="submit")  # Submit button
        ))

# POST route to handle form submission
@rt("/profile") 
def post(profile: Profile):  # FastHTML auto-converts form data to Profile instance
    return Titled("Success!",  # Show success page
        P(f"Saved profile for {profile.email}"))  # Display confirmation message
```

### 3. WebSocket Chat
```python
# Create a FastHTML app with WebSocket extension enabled
app, rt = fast_app(exts='ws')

# GET route to display the chat interface
@rt('/')
async def get():
    return Titled("Chat", 
        Div(id='messages'),  # Container for chat messages
        Form(Input(id='msg'), ws_send=True),  # Form with input that sends via WebSocket
        hx_ext='ws',  # Enable HTMX WebSocket extension
        ws_connect='/ws'  # WebSocket endpoint to connect to
    )

# WebSocket route to handle messages
@app.ws('/ws')
async def ws(msg: str, send):
    # When message received, send back a div containing the message
    await send(Div(f"Message: {msg}", id='messages'))
```

## 🎨 Custom Components

Create reusable UI components:

```python
# Add tailwind to the app
app, rt = fast_app(exts='tw')

# Define a hero component
def hero(title, statement):
    return Div(
        H1(title, cls="text-5xl font-bold mb-4 text-indigo-600"),  # Large, bold title in indigo with margin bottom
        P(statement, cls="text-xl text-gray-600 max-w-2xl"),  # Larger paragraph text in gray with max width
        cls="flex flex-col items-center justify-center min-h-[50vh] py-12 px-4"  # Center content vertically and horizontally with padding
    )

@rt("/")
def get():
    return Titled("Home",
        hero("Welcome!", "Build beautiful web apps with Python")
    )
```

## 🔒 Authentication

Add authentication with Beforeware:

```python
def auth_check(req, sess):
    auth = req.scope['auth'] = sess.get('auth')
    if not auth:
        return RedirectResponse('/login', status_code=303)

bware = Beforeware(auth_check, skip=['/login', '/static/.*'])
app, rt = fast_app(before=bware)
```

## 🌐 Best Practices

1. **Use Type Hints**
   - FastHTML leverages type annotations for automatic request parsing
   - Makes your code more maintainable and self-documenting

2. **Leverage HTMX**
   - Use HTMX attributes for dynamic updates
   - Minimize client-side JavaScript

3. **Keep Components Small**
   - Break UI into reusable functions
   - Makes testing and maintenance easier

## 📚 Resources

- [Official Documentation](https://docs.fastht.ml/)
- [HTMX Documentation](https://htmx.org/)
- [Tailwind Documentation](https://tailwindcss.com/)



*