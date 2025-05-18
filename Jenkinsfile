pipeline {
    agent any

    environment {
        FLASK_APP = "app.main"
        FLASK_RUN_HOST = "0.0.0.0"
        FLASK_RUN_PORT = "5000"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Venkateswara-Sahu/banking-api.git' // Replace with actual repo URL
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('banking-api:latest')
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat 'docker run --rm banking-api pytest'
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://hub.docker.com/repositories/riverstead', 'docker-hub-credentials') {
                        docker.image('banking-api:latest').push()
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                bat 'docker-compose up -d'
            }
        }

        stage('Health Check') {
            steps {
                bat 'curl -f http://localhost:5000/health || exit /b 1'
            }
        }
    }

    post {
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}