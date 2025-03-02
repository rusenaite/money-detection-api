# AI-Powered Banknote Detection

## Overview
Web-based solution that allows users to upload images for analysis using an AI model running in a **Dockerized FastAPI server**. The model detects and identifies banknotes.

![web_app](web_app.png)

## Technologies & Libraries Used
- **Backend:** Django, Django REST Framework, FastAPI (Dockerized)
- **AI Model:** YOLO (Ultralytics)
- **Image Processing:** OpenCV
- **Frontend:** React, JavaScript, Axios
- **Server & Storage:** Django Media Storage, Local Development Server, FastAPI in Docker

## System Workflow
1. User uploads an image via the web interface.
2. The image is sent to the Django API.
3. Django forwards the image to the **FastAPI model server running in Docker**.
4. The AI model detects banknotes and marks them on the image.
5. The processed image is returned to Django, then displayed on the frontend.

## How to Run the System
### **Backend Setup (Django)**
1. Clone the repository:
   ```bash
   git clone https://github.com/rusenaite/money-detection-api.git
   cd money-detection-api
   ```
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Apply migrations and run the server:
   ```bash
   python manage.py migrate
   python manage.py runserver 0.0.0.0:8000
   ```

### **FastAPI Model Server (Dockerized)**
1. Navigate to `model_server` directory:
   ```bash
   cd model_server
   ```
2. **Build and run the Docker container:**
   ```bash
   docker build -t model_server .
   docker run -p 8001:8001 model_server
   ```

3. **FastAPI should now be running on:** `http://localhost:8001`

### **Frontend Setup (React)**
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the React app:
   ```bash
   npm start
   ```
4. Open `http://localhost:3000` in your browser.

## Results & Visualization
- The system correctly identifies and highlights banknotes.
- The processed image is displayed alongside the original.

## What could be improved
- Optimize model performance and inference speed.