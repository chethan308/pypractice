from flask import request, render_template_string

# /hello?username={{config}} will display the entire flask configuration and potential secrets
@app.route('/hello')
def hello():
    username = request.args.get('username')
    template = f"<p>Hello {username}</p>" # User input is used directly in the string to be rendered
    return render_template_string(template) # Noncompliant
  
def example():
    operation = request.args.get("operation")
    eval(f"product_{operation}()") # Noncompliant
    return "OK"

my_list = [3, 4, 5, 6]
my_list[15]
