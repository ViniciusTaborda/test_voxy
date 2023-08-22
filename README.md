
# Word Count Challenge

This repository contains a simple web application that counts the number of words in a given block of text. The backend is implemented using FastAPI, and the frontend is a basic HTML page served by an Express.js server.

## Prerequisites

Before running the project, make sure you have the following installed:

-   Python 3.8 or higher
-   Node.js 12 or higher
-   FastAPI
-   Uvicorn
-   Express.js
-   Makefile

## Installation

1.  **Clone the Repository**:
    
    bashCopy code
    
    `git clone https://github.com/ViniciusTaborda/test_voxy.git
    cd test_voxy` 
    
2.  **Install Backend Dependencies**: Navigate to the `backend` directory and install the required Python packages.
    
    bashCopy code
    
    `cd backend &&
    pip install -r requirements.txt` 
    
3.  **Install Frontend Dependencies**: Navigate to the `frontend` directory and install the required Node.js packages.
    
    bashCopy code
    
    `cd ../frontend &&
    npm install` 
    

## Running the Project

The project can be run using the provided Makefile. From the root directory of the project, run the following command:

bashCopy code

`make run` 

This will start both the FastAPI backend and the Node.js frontend server. The backend will be accessible at `http://localhost:8000`, and the frontend will be accessible at `http://localhost:3000`.

## Usage

Open your web browser and navigate to `http://localhost:3000`. You will see a text area where you can input the text you want to count the words of. Click the "Count Words" button to see the word count.
