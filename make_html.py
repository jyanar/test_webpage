from datetime import datetime

# Get the current date and time
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Define the content of the index.html file
html_content = """
<!DOCTYPE html>
<html>
<head>
	<title>My Website</title>
</head>
<body>
	<h1>Welcome to my website</h1>
	<p>This is some sample text.</p>
	<p>Current date and time: {}</p>
	<img src="image.jpg" alt="Sample image">
</body>
</html>
""".format(current_datetime)

# Create index.html and write content to it
with open('index.html', 'w') as f:
        f.write(html_content)

