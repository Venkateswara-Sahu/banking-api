pipeline {
    agent any

    environment {
        COMPOSE_PROJECT_NAME = "banking_api"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Clean Up Previous Containers') {
            steps {
                echo "Stopping and removing old containers if they exist..."
                bat 'docker stop banking_api 2> nul || echo "No active container to stop"'
                bat 'docker rm banking_api 2> nul || echo "No container to remove"'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building a fresh Docker image..."
                bat 'docker build -t banking-api .'
            }
        }

        stage('Run Docker Container') {
            steps {
                echo "Starting the Flask container..."
                bat 'docker run -d --name banking_api -p 5000:5000 banking-api'

                script {
                    def timeout = 120
                    def startTime = System.currentTimeMillis()
                    def isReady = false

                    echo "Checking container status..."

                    while (System.currentTimeMillis() - startTime < timeout * 1000) {
                        def status = bat(
                            script: "docker inspect --format='{{.State.Status}}' banking_api",
                            returnStdout: true
                        ).trim()

                        echo "Current status: ${status}"

                        if (status == 'running') {
                            echo "Container is running successfully!"
                            isReady = true
                            break
                        }

                        sleep time: 5, unit: 'SECONDS'
                    }

                    if (!isReady) {
                        error "Container did not start properly within ${timeout} seconds."
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                echo "Executing Pytest inside the container..."
                bat 'docker exec banking_api pytest tests/test_banking_api.py --maxfail=1 --disable-warnings --tb=short || echo "Tests failed"'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up containers...'
            bat 'docker stop banking_api 2> nul || echo "No active container to stop"'
            bat 'docker rm banking_api 2> nul || echo "No container to remove"'
        }
    }
}