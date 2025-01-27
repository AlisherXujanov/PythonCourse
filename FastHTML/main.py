###
# Example of a FastHTML app using Tailwind CSS
###

# This fasthtml app includes functionality from fastcore, starlette, fastlite, and fasthtml itself.
# Run with: `python adv_app.py`
# Importing from `fasthtml.common` brings the key parts of all of these together.
# For simplicity, you can just `from fasthtml.common import *`:
from fasthtml.common import *
# ...or you can import everything into a namespace:
# from fasthtml import common as fh
# ...or you can import each symbol explicitly (which we're commenting out here but including for completeness):
"""
from fasthtml.common import (
    # These are the HTML components we use in this app
    A, AX, Button, Card, CheckboxX, Container, Div, Form, Grid, Group, H1, H2, Hidden, Input, Li, Main, Script, Style, Textarea, Title, Titled, Ul,
    # These are FastHTML symbols we'll use
    Beforeware, FastHTML, fast_app, SortableJS, fill_form, picolink, serve,
    # These are from Starlette, Fastlite, fastcore, and the Python stdlib
    FileResponse, NotFoundError, RedirectResponse, database, patch, dataclass
)
"""

from hmac import compare_digest

# You can use any database you want; it'll be easier if you pick a lib that supports the MiniDataAPI spec.
# Here we are using SQLite, with the FastLite library, which supports the MiniDataAPI spec.
db = database('data/utodos.db')
# The `t` attribute is the table collection. The `todos` and `users` tables are not created if they don't exist.
# Instead, you can use the `create` method to create them if needed.
todos, users = db.t.todos, db.t.users
if todos not in db.t:
    # You can pass a dict, or kwargs, to most MiniDataAPI methods.
    users.create(dict(name=str, pwd=str), pk='name')
    todos.create(id=int, title=str, done=bool, name=str,
                 details=str, priority=int, pk='id')
# Although you can just use dicts, it can be helpful to have types for your DB objects.
# The `dataclass` method creates that type, and stores it in the object, so it will use it for any returned items.
Todo, User = todos.dataclass(), users.dataclass()

# Any Starlette response class can be returned by a FastHTML route handler.
# In that case, FastHTML won't change it at all.
# Status code 303 is a redirect that can change POST to GET, so it's appropriate for a login page.
login_redir = RedirectResponse('/login', status_code=303)

# The `before` function is a *Beforeware* function. These are functions that run before a route handler is called.


def before(req, sess):
    """Authentication middleware"""
    # This sets the `auth` attribute in the request scope, and gets it from the session.
    # The session is a Starlette session, which is a dict-like object which is cryptographically signed,
    # so it can't be tampered with.
    # The `auth` key in the scope is automatically provided to any handler which requests it, and can not
    # be injected by the user using query params, cookies, etc, so it should be secure to use.
    auth = req.scope['auth'] = sess.get('auth', None)
    # If the session key is not there, it redirects to the login page.
    if not auth:
        return login_redir
    # `xtra` is part of the MiniDataAPI spec. It adds a filter to queries and DDL statements,
    # to ensure that the user can only see/edit their own todos.
    todos.xtra(name=auth)


markdown_js = """
import { marked } from "https://cdn.jsdelivr.net/npm/marked/lib/marked.esm.js";
proc_htmx('.markdown', e => e.innerHTML = marked.parse(e.textContent));
"""

# We will use this in our `exception_handlers` dict


def _not_found(req, exc): 
    return Titled('404 Not Found', 
                 Div('Page not found', cls='text-red-600 p-4 rounded-lg bg-red-100'))


# To create a Beforeware object, we pass the function itself, and optionally a list of regexes to skip.
bware = Beforeware(
    before, skip=[r'/favicon\.ico', r'/static/.*', r'.*\.css', '/login'])
# The `FastHTML` class is a subclass of `Starlette`, so you can use any parameters that `Starlette` accepts.
# In addition, you can add your Beforeware here, and any headers you want included in HTML responses.
# FastHTML includes the "HTMX" and "Surreal" libraries in headers, unless you pass `default_hdrs=False`.
app = FastHTML(before=bware,
               # These are the same as Starlette exception_handlers, except they also support `FT` results
               exception_handlers={404: _not_found},
               # Tailwind CSS via CDN - in production you should use a proper build process
               hdrs=(
                   Script(src='https://cdn.tailwindcss.com'),
                   # Custom styles - minimal since we're using Tailwind utility classes
                   Style("""
                       .todo-list { max-width: 800px; margin: 2rem auto; }
                   """),
                   # Additional libraries
                   SortableJS('.sortable'),
                   Script(markdown_js, type='module')
               ))
# We add `rt` as a shortcut for `app.route`, which is what we'll use to decorate our route handlers.
# When using `app.route` (or this shortcut), the only required argument is the path.
# The name of the decorated function (eg `get`, `post`, etc) is used as the HTTP verb for the handler.
rt = app.route

# For instance, this function handles GET requests to the `/login` path.


@rt("/login")
def get():
    """Login page with Tailwind styling"""
    frm = Form(
        Div(cls='mb-6')(
            Label('Username', cls='block text-gray-700 text-sm font-bold mb-2', for_='name'),
            Input(id='name', placeholder='Enter username', 
                 cls='shadow-lg appearance-none border-2 border-gray-200 rounded-lg w-full py-3 px-4 text-gray-700 leading-tight focus:outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-200 transition duration-200')
        ),
        Div(cls='mb-6')(
            Label('Password', cls='block text-gray-700 text-sm font-bold mb-2', for_='pwd'),
            Input(id='pwd', type='password', placeholder='Enter password',
                 cls='shadow-lg appearance-none border-2 border-gray-200 rounded-lg w-full py-3 px-4 text-gray-700 leading-tight focus:outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-200 transition duration-200')
        ),
        Button('Login', cls='w-full bg-gradient-to-r from-blue-500 to-blue-600 hover:from-blue-600 hover:to-blue-700 text-white font-bold py-3 px-6 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400 focus:ring-offset-2 transform hover:scale-[1.02] transition-all duration-200'),
        action='/login', method='post', 
        cls='bg-white backdrop-blur-lg bg-opacity-90 shadow-2xl rounded-xl px-8 py-8 border border-gray-100')
    return Titled("Login", Div(frm, cls='container mx-auto max-w-md mt-20'))

# Handlers are passed whatever information they "request" in the URL, as keyword arguments.
# Dataclasses, dicts, namedtuples, TypedDicts, and custom classes are automatically instantiated
# from form data.
# In this case, the `Login` class is a dataclass, so the handler will be passed `name` and `pwd`.


@dataclass
class Login:
    name: str
    pwd: str

# This handler is called when a POST request is made to the `/login` path.
# The `login` argument is an instance of the `Login` class, which has been auto-instantiated from the form data.
# There are a number of special parameter names, which will be passed useful information about the request:
# `session`: the Starlette session; `request`: the Starlette request; `auth`: the value of `scope['auth']`,
# `htmx`: the HTMX headers, if any; `app`: the FastHTML app object.
# You can also pass any string prefix of `request` or `session`.


@rt("/login")
def post(login: Login, sess):
    """Handle login form submission"""
    if not login.name or not login.pwd:
        return login_redir
    # Indexing into a MiniDataAPI table queries by primary key, which is `name` here.
    # It returns a dataclass object, if `dataclass()` has been called at some point, or a dict otherwise.
    try:
        u = users[login.name]
    # If the primary key does not exist, the method raises a `NotFoundError`.
    # Here we use this to just generate a user -- in practice you'd probably to redirect to a signup page.
    except NotFoundError:
        u = users.insert(login)
    # This compares the passwords using a constant time string comparison
    # https://sqreen.github.io/DevelopersSecurityBestPractices/timing-attack/python
    if not compare_digest(u.pwd.encode("utf-8"), login.pwd.encode("utf-8")):
        return login_redir
    # Because the session is signed, we can securely add information to it. It's stored in the browser cookies.
    # If you don't pass a secret signing key to `FastHTML`, it will auto-generate one and store it in a file `./sesskey`.
    sess['auth'] = u.name
    return RedirectResponse('/', status_code=303)

# Instead of using `app.route` (or the `rt` shortcut), you can also use `app.get`, `app.post`, etc.
# In this case, the function name is not used to determine the HTTP verb.


@app.get("/logout")
def logout(sess):
    """Handle logout"""
    del sess['auth']
    return login_redir

# FastHTML uses Starlette's path syntax, and adds a `static` type which matches standard static file extensions.
# You can define your own regex path specifiers -- for instance this is how `static` is defined in FastHTML
# `reg_re_param("static", "ico|gif|jpg|jpeg|webm|css|js|woff|png|svg|mp4|webp|ttf|otf|eot|woff2|txt|xml|html")`
# In this app, we only actually have one static file, which is `favicon.ico`. But it would also be needed if
# we were referencing images, CSS/JS files, etc.
# Note, this function is unnecessary, as the `fast_app()` call already includes this functionality.
# However, it's included here to show how you can define your own static file handler.


@rt("/{fname:path}.{ext:static}")
def get(fname: str, ext: str): 
    return FileResponse(f'{fname}.{ext}')

# The `patch` decorator, which is defined in `fastcore`, adds a method to an existing class.
# Here we are adding a method to the `Todo` class, which is returned by the `todos` table.
# The `__ft__` method is a special method that FastHTML uses to convert the object into an `FT` object,
# so that it can be composed into an FT tree, and later rendered into HTML.


@patch
def __ft__(self: Todo):
    """Todo item component with Tailwind styling"""
    show = AX(self.title, f'/todos/{self.id}', 'current-todo')
    edit = AX('Edit', f'/edit/{self.id}', 'current-todo', 
              cls='ml-3 px-4 py-2 text-sm text-blue-600 hover:text-blue-700 border-2 border-blue-500 rounded-lg hover:bg-blue-50 font-semibold transition duration-200')
    dt = '✅ ' if self.done else ''
    cts = (dt, show, edit,
           Hidden(id="id", value=self.id),
           Hidden(id="priority", value="0"))
    return Li(*cts, id=f'todo-{self.id}', 
             cls='flex justify-between items-center p-4 hover:bg-gray-50 transition duration-200')

# This is the handler for the main todo list application.
# By including the `auth` parameter, it gets passed the current username, for displaying in the title.


@rt("/")
def get(auth):
    """Main todo list page with Tailwind styling"""
    title = f"{auth}'s Todo List"
    
    # Header with logout button
    top = Div(
        H1(title, cls='text-3xl font-bold bg-gradient-to-r from-blue-600 to-blue-400 bg-clip-text text-transparent'),
        A('Logout', href='/logout', 
          cls='px-4 py-2 border-2 border-red-500 text-red-500 rounded-lg hover:bg-red-50 transition duration-200 font-semibold'),
        cls='flex justify-between items-center mb-8'
    )
    
    # New todo form
    new_inp = Input(id="new-title", name="title", 
                   placeholder="Add a new task...",
                   cls='w-full p-3 border-2 border-gray-200 rounded-l-lg focus:outline-none focus:ring-2 focus:ring-blue-300 focus:border-blue-500 transition duration-200')
    add = Form(
        Div(cls='flex shadow-lg')(
            new_inp,
            Button("Add Task", cls='bg-gradient-to-r from-blue-500 to-blue-600 text-white px-6 py-3 rounded-r-lg hover:from-blue-600 hover:to-blue-700 font-semibold transition duration-200')
        ),
        hx_post="/", target_id='todo-list', hx_swap="afterbegin",
        cls='mb-8'
    )
    
    # Todo list
    frm = Form(
        *todos(order_by='priority'),
        id='todo-list', 
        cls='divide-y divide-gray-200 sortable', 
        hx_post="/reorder", 
        hx_trigger="end"
    )
    
    # Main container
    content = Div(
        top,
        add,
        Div(Ul(frm), cls='bg-white shadow-xl rounded-xl overflow-hidden mb-8 border border-gray-100'),
        Div(id='current-todo'),
        cls='todo-list'
    )
    
    return Title(title), Div(content, cls='container mx-auto px-6 py-12 max-w-4xl')

# This is the handler for the reordering of todos.
# It's a POST request, which is used by the 'sortable' js library.
# Because the todo list form created earlier included hidden inputs with the todo IDs,
# they are passed as form data. By using a parameter called (e.g) "id", FastHTML will try to find
# something suitable in the request with this name. In order, it searches as follows:
# path; query; cookies; headers; session keys; form data.
# Although all these are provided in the request as strings, FastHTML will use your parameter's type
# annotation to try to cast the value to the requested type.
# In the case of form data, there can be multiple values with the same key. So in this case,
# the parameter is a list of ints.


@rt("/reorder")
def post(id: list[int]):
    for i, id_ in enumerate(id):
        todos.update({'priority': i}, id_)
    # HTMX by default replaces the inner HTML of the calling element, which in this case is the todo list form.
    # Therefore, we return the list of todos, now in the correct order, which will be auto-converted to FT for us.
    # In this case, it's not strictly necessary, because sortable.js has already reorder the DOM elements.
    # However, by returning the updated data, we can be assured that there aren't sync issues between the DOM
    # and the server.
    return tuple(todos(order_by='priority'))

# Refactoring components in FastHTML is as simple as creating Python functions.
# The `clr_details` function creates a Div with specific HTMX attributes.
# `hx_swap_oob='innerHTML'` tells HTMX to swap the inner HTML of the target element out-of-band,
# meaning it will update this element regardless of where the HTMX request originated from.


def clr_details(): 
    return Div(hx_swap_oob='innerHTML', id='current-todo')

# This route handler uses a path parameter `{id}` which is automatically parsed and passed as an int.


@rt("/todos/{id}")
def delete(id: int):
    # The `delete` method is part of the MiniDataAPI spec, removing the item with the given primary key.
    todos.delete(id)
    # Returning `clr_details()` ensures the details view is cleared after deletion,
    # leveraging HTMX's out-of-band swap feature.
    # Note that we are not returning *any* FT component that doesn't have an "OOB" swap, so the target element
    # inner HTML is simply deleted. That's why the deleted todo is removed from the list.
    return clr_details()


@rt("/edit/{id}")
def get(id: int):
    """Edit form with Tailwind styling"""
    todo = todos[id]
    
    # Add delete completed button if todo is done
    delete_completed = (
        Div(
            Button("Delete Completed Task", 
                   hx_delete=f'/todos/{id}',
                   target_id=f'todo-{id}',
                   hx_swap="outerHTML",
                   cls='w-full bg-gradient-to-r from-red-500 to-red-600 hover:from-red-600 hover:to-red-700 text-white font-bold py-3 px-6 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-400 transform hover:scale-[1.02] transition-all duration-200 mb-6'),
            cls='animate-fade-in'
        ) if todo.done else Div()
    )

    res = Form(
        # Add warning banner for completed tasks
        (Div(
            Div(
                Div(cls="flex-shrink-0")(
                    Div(cls="h-12 w-12 flex items-center justify-center rounded-full bg-yellow-100")(
                        "⚠️"
                    )
                ),
                Div(cls="ml-3")(
                    H3("Task Completed", cls="text-lg font-medium text-yellow-800"),
                    Div(cls="mt-2 text-sm text-yellow-700")(
                        P("This task is marked as complete. You can either continue editing or delete it using the button below.")
                    )
                )
            ),
            cls="rounded-md bg-yellow-50 p-4 mb-8"
        ) if todo.done else Div()),

        delete_completed,

        Div(cls='mb-6')(
            Label('Title', cls='block text-gray-700 font-bold mb-2'),
            Input(id="title", cls='w-full p-3 border-2 border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-300 focus:border-blue-500 transition duration-200')
        ),
        Div(cls='mb-6 flex items-center space-x-2')(
            CheckboxX(id="done", 
                     cls='h-5 w-5 rounded border-gray-300 text-blue-600 focus:ring-blue-500 transition duration-200'),
            Label('Mark as Complete', cls='text-gray-700 font-medium select-none')
        ),
        Div(cls='mb-6')(
            Label('Details', cls='block text-gray-700 font-bold mb-2'),
            Textarea(id="details", name="details", rows=10, 
                    cls='w-full p-3 border-2 border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-300 focus:border-blue-500 transition duration-200')
        ),
        Hidden(id="id"),
        Button("Save Changes", 
               cls='w-full bg-gradient-to-r from-blue-500 to-blue-600 hover:from-blue-600 hover:to-blue-700 text-white font-bold py-3 px-6 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400 transform hover:scale-[1.02] transition-all duration-200'),
        hx_put="/", target_id=f'todo-{id}', id="edit",
        cls='bg-white shadow-2xl rounded-xl p-8 border border-gray-100'
    )
    return fill_form(res, todo)


@rt("/")
def put(todo: Todo):
    # `update` is part of the MiniDataAPI spec.
    # Note that the updated todo is returned. By returning the updated todo, we can update the list directly.
    # Because we return a tuple with `clr_details()`, the details view is also cleared.
    return todos.update(todo), clr_details()


@rt("/")
def post(todo: Todo):
    # `hx_swap_oob='true'` tells HTMX to perform an out-of-band swap, updating this element wherever it appears.
    # This is used to clear the input field after adding the new todo.
    new_inp = Input(id="new-title", name="title",
                   placeholder="New Todo", cls='form-control',
                   hx_swap_oob='true')
    # `insert` returns the inserted todo, which is appended to the start of the list, because we used
    # `hx_swap='afterbegin'` when creating the todo list form.
    return todos.insert(todo), new_inp


@rt("/todos/{id}")
def get(id: int):
    """Todo details with Tailwind styling"""
    todo = todos[id]
    btn = Button('Delete Task', 
               hx_delete=f'/todos/{todo.id}',
               target_id=f'todo-{todo.id}',
               hx_swap="outerHTML",
               cls='bg-gradient-to-r from-red-500 to-red-600 hover:from-red-600 hover:to-red-700 text-white px-6 py-3 rounded-lg font-semibold transform hover:scale-[1.02] transition-all duration-200')
    return Div(
        H2(todo.title, cls='text-2xl font-bold mb-6 bg-gradient-to-r from-blue-600 to-blue-400 bg-clip-text text-transparent'),
        Div(todo.details, cls="markdown prose max-w-none bg-gray-50 p-6 rounded-xl mb-6"),
        btn,
        cls='bg-white shadow-2xl rounded-xl p-8 border border-gray-100'
    )


serve()
