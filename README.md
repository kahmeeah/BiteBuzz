![Lint-free](https://github.com/nyu-software-engineering/containerized-app-exercise/actions/workflows/lint.yml/badge.svg)
![Web App CI](https://github.com/software-students-spring2025/4-containers-dockstars/actions/workflows/web-app-ci.yml/badge.svg?branch=main)
![ML Client CI](https://github.com/software-students-spring2025/4-containers-dockstars/actions/workflows/machine-learning-client-ci.yml/badge.svg?branch=main)

# Voice Review Analyzer 

This project provides a more natural and accessible way for restaurant customers to give feedback using speech input. Instead of typing, customers can simply record their reviews directly through the web app.

Our Machine Learning Client transcribes the audio into text, performs sentiment analysis, detects relevant content, and generates helpful suggestions for improvement. Restaurant owners can open an admin dashboard to view these processed reviews and take meaningful action on customer feedback.

This voice-powered system enhances both the user experience and the business insight process.

# Overview:
The application consists of three independent subsystems:

### Flask Web App
- Captures voice reviews via microphone
- Performs speech-to-text conversion
- Sends raw data to the database
- Retrieves processed insights to display to restaurant owners

### ML Client
- Performs sentiment analysis (Positive, Negative, Neutral) using ```TextBlob```
-  Detects keyword-based categories (e.g., Food, Service, Cleanliness, etc.)
- Generates suggestions based on detected content and sentiment

### MongoDB (Dockerized)
- Stores all incoming raw review data
- Stores all processed sentiment, category, and suggestion metadata
- Acts as the communication layer between the web app and the ML client

# Key Features:
- Microphone-based review capture
- Sentiment and text analysis
- improvement suggestions
- Admin dashboard to display reviews and their associated suggestions





# Setup and Installation:
## Prerequisites

Install the following software on your machine:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Python 3.8+](https://www.python.org/downloads/)

### Installing Docker

1. Go to the [Docker website](https://www.docker.com/products/docker-desktop) and download Docker Desktop for your operating system.
2. Follow the installation instructions and make sure Docker Desktop is running.

## Running and Configuration Instructions

Clone the repository:
```shell
git clone https://github.com/software-students-spring2025/4-containers-dockstars.git
```

Run the following command:
```shell
docker-compose up --build
```
This starts all three services:
- Machine learning client
- Flask web app
- MongoDB database


Access the web interface at http://127.0.0.1:8080

### Development

Alternatively, if you would like to test each system locally, you can install the dependencies for each as follows:


ML Client:
```shell
cd machine-learning-client
pipenv install
```

Web App:
```shell
cd web-app
pipenv install
```





# Team
* [Ajok Thon](https://github.com/ajokt123)
* [Aria Nguyen](https://github.com/ariangn)
* [Kahmeeah Obey](https://github.com/kahmeeah)
* [Nyjur Majok](https://github.com/nyjur1)
