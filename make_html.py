
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
    <img src="image.jpg">
</body>
</html>
"""

# Create index.html and write content to it
with open('index.html', 'w') as f:
        f.write(html_content)

