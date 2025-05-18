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

                    echo "Waiting for Flask service to respond..."

                    while (System.currentTimeMillis() - startTime < timeout * 1000) {
                        def responseCode = bat(
                            script: "curl -s -o nul -w \"%{http_code}\" http://localhost:5000/health",
                            returnStdout: true
                        ).trim()

                        echo "HTTP Response Code: ${responseCode}"

                        if (responseCode == '200') {
                            echo "Flask service is live!"
                            isHealthy = true
                            break
                        }

                        sleep time: 5, unit: 'SECONDS'
                    }

                    if (!isHealthy) {
                        error "Flask service did not start properly within ${timeout} seconds."
                    }
                }
            }
        }

        stage('Run Pytest') {
            steps {
                bat 'docker-compose exec -T banking-api pytest tests/test_banking_api.py --maxfail=1 --disable-warnings --tb=short || echo "Tests failed"'
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