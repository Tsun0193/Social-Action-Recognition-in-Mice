#!/usr/bin/env bash
echo "🔧 Creating virtual environment..."
uv init
uv venv --python=3.12

# 3. Activate the virtual environment
echo "🔗 Activating virtual environment..."
. .venv/bin/activate

# 4. Install dependencies
echo "📦 Installing dependencies..."
uv pip install -r requirements.txt
uv add --dev ipykernel

# 5. Export the current directory is the main 
echo "📂 Setting current directory as the main directory for the virtual environment..."
export PYTHON_PATH="$(pwd):$PYTHON_PATH"

# 5. Success message
echo "🎉 Setup complete! Virtual environment is ready to use."
echo "To activate the virtual environment, run: source .venv/bin/activate"