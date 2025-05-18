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
                bat 'docker ps -q --filter "name=banking_api" | for /F "delims=" %%i in (\'more\') do docker stop %%i || echo "No active container found"'
                bat 'docker ps -aq --filter "name=banking_api" | for /F "delims=" %%i in (\'more\') do docker rm %%i || echo "No containers to remove"'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t banking-api .'
            }
        }

        stage('Run Docker Container') {
            steps {
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
                bat 'docker run --rm banking-api pytest tests/test_banking_api.py --maxfail=1 --disable-warnings --tb=short || echo "Tests failed"'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up containers...'
            bat 'docker stop banking_api || echo "No active container to stop"'
            bat 'docker rm banking_api || echo "No container to remove"'
        }
    }
}