# Make-BST (Binary Search Tree Visualizer)

This is a small project I built to **visualize Binary Search Trees (BSTs)** using **Python, Flask, and Graphviz**.  
It lets you add, delete, and search nodes in a BST, and instantly shows the updated tree in your browser with a clean graphical view.

## Features
- Add nodes to build a BST  
- Delete nodes and watch the tree restructure itself  
- Search for a node (it will be highlighted)  
- Real-time updates using Graphviz  
- Simple and clean web interface (Flask + CSS)  

## How to Set It Up

### 1. Clone this repo
git clone https://github.com/KajalMeena04/Make-BST.git
cd Make-BST

### 2. Create a virtual environment
python -m venv venv

Activate it:  
- Windows: venv\Scripts\activate  
- Linux/Mac: source venv/bin/activate  

### 3. Install dependencies
pip install -r requirements.txt

### 4. Install Graphviz
- Windows: Download from https://graphviz.gitlab.io/_pages/Download/Download_windows.html and add the bin/ folder to PATH  
- Linux: sudo apt install graphviz  
- macOS: brew install graphviz  

Check installation:
dot -V

### 5. Run the app
python app.py

Now open your browser and visit:  
http://127.0.0.1:5000



## Project Structure
Make-BST/
│── app.py              # Flask app
│── bst.py              # BST logic
│── templates/          # HTML templates
│── static/             # CSS/JS files
│── requirements.txt    # Python dependencies
│── README.md           # Project details


## Tech Stack
- Python + Flask   
- Graphviz (tree visualization)  
- HTML/CSS (frontend)  

This project is mainly for learning and experimenting with BSTs and Flask. If you’re trying it out, feel free to clone and play around with it!
