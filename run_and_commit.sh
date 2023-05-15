#!/bin/bash

# Generate HTML page and plots
python make_html.py

# Add everything to git and push
git add .
git commit -m "Automatic commit message"
git push origin main

