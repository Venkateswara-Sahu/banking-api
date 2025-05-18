pipeline {
    agent any

    environment {
        COMPOSE_PROJECT_NAME = 'banking_api_project'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Venkateswara-Sahu/banking-api.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker-compose up -d'
                // Wait for health check to pass
                sh 'sleep 20'
            }
        }

        stage('Run Pytest') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pip install pytest requests'
                sh 'pytest tests/test_banking_api.py --maxfail=1 --disable-warnings --tb=short'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up containers...'
            sh 'docker-compose down'
        }
    }
}
