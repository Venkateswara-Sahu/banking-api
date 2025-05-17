pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/Venkateswara-Sahu/banking-api.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t banking-api .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker stop banking-api-container || true'
                sh 'docker rm banking-api-container || true'
                sh 'docker run -d -p 5000:5000 --name banking-api-container banking-api'
            }
        }
    }
}
