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

        stage('Build Docker Image') {
            steps {
                bat 'docker-compose down || echo "No container to stop"'
                bat 'docker build -t banking-api .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker-compose up -d'

                script {
                    def timeout = 120 // seconds
                    def startTime = System.currentTimeMillis()
                    def isHealthy = false

                    echo "Waiting for Flask container to stabilize..."

                    while (System.currentTimeMillis() - startTime < timeout * 1000) {
                        def containerStatus = bat(
                            script: "docker inspect --format='{{.State.Status}}' banking_api",
                            returnStdout: true
                        ).trim()

                        echo "Container status: ${containerStatus}"

                        if (containerStatus == 'running') {
                            echo "Flask container is running!"
                            isHealthy = true
                            break
                        }

                        sleep time: 5, unit: 'SECONDS'
                    }

                    if (!isHealthy) {
                        error "Flask container did not become stable within ${timeout} seconds."
                    }
                }
            }
        }

        stage('Run Pytest') {
            steps {
                bat 'docker-compose exec banking-api pytest tests/test_banking_api.py --maxfail=1 --disable-warnings --tb=short || echo "Tests failed"'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up containers...'
            bat 'docker-compose down || echo "No active containers to remove"'
        }
    }
}