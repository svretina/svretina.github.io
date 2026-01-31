#!/bin/bash

# Navigate to the script's directory
cd "$(dirname "$0")"

# Navigate to project root
cd ..

echo "Updating CV..."

# Read Token
if [ ! -f ".overleaf_token" ]; then
    echo "Error: .overleaf_token file not found."
    echo "Please create it and paste your Overleaf Git Token inside."
    exit 1
fi

TOKEN=$(cat .overleaf_token | grep -v "^#" | tr -d '[:space:]')
if [ -z "$TOKEN" ]; then
    echo "Error: .overleaf_token is empty."
    exit 1
fi

# Navigate to repo
cd cv-source

# 1. Get current remote URL (e.g., https://git@git.overleaf.com/ID)
REMOTE_URL=$(git remote get-url origin)

# 2. Extract the base domain path (remove user info and protocol)
# Removes "https://"
URL_NO_PROTO=${REMOTE_URL#*://}
# Removes "git@" or "anything@" from the start
URL_CLEAN=${URL_NO_PROTO#*@}

# 3. Construct Auth URL
AUTH_URL="https://git:${TOKEN}@${URL_CLEAN}"

echo "Pulling latest changes from Overleaf..."
git pull "$AUTH_URL"

# Compile LaTeX
pdflatex -interaction=nonstopmode main.tex

# Check if PDF generated
if [ -f "main.pdf" ]; then
    echo "Compilation successful. Copying to public/cv.pdf..."
    cp main.pdf ../public/cv.pdf
    echo "Done! CV updated on website."
else
    echo "Error: PDF compilation failed."
    exit 1
fi
