pipeline {
    agent any

    environment {
        FLASK_APP = "app.main"
        FLASK_RUN_HOST = "0.0.0.0"
        FLASK_RUN_PORT = "5000"
    }

    stages {
        stage('Cloning') {
            steps {
                bat '''
                if exist banking-api (
                    rmdir /s /q banking-api
                )
                git clone https://github.com/Venkateswara-Sahu/banking-api.git
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('banking-api:latest')
                }
            }
        }

        stage('Start Flask API') {
            steps {
                bat '''
                docker-compose up -d
                ping -n 30 127.0.0.1 >nul
                curl -f http://localhost:5000/health || exit /b 1
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat 'docker exec banking_api pytest -v tests/'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        bat """
                        echo Logging in to Docker Hub...
                        echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin

                        echo Tagging the image...
                        docker tag banking-api:latest %DOCKER_USER%/banking-api:latest

                        echo Pushing the image to Docker Hub...
                        docker push %DOCKER_USER%/banking-api:latest
                        """
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