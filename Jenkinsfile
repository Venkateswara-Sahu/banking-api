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
        bat 'docker build -t banking-api .'
      }
    }

    stage('Run Docker Container') {
      steps {
        bat 'docker-compose up -d'
        // Wait for the service to be healthy
        script {
          def timeout = 120 // seconds
          def startTime = System.currentTimeMillis()
          def isHealthy = false
          
          // Add debugging information
          echo "Checking container logs..."
          bat 'docker logs banking-api || echo "No logs available"'

          while (System.currentTimeMillis() - startTime < timeout * 1000) {
            def healthStatus = bat(
              script: "docker inspect --format='{{.State.Health.Status}}' banking_api",
              returnStdout: true
            ).trim()

            echo "Current health status: ${healthStatus}"

            // Check if container is running
            def containerStatus = bat(
              script: "docker inspect --format='{{.State.Status}}' banking_api",
              returnStdout: true
            ).trim()
            echo "Container status: ${containerStatus}"

            // Show recent logs
            bat 'docker logs --tail=10 banking-api || echo "Cannot fetch logs"'

            if (healthStatus == "healthy") {
              echo "banking-api container is healthy!"
              isHealthy = true
              break
            }

            echo "Waiting for banking-api container to become healthy..."
            sleep time: 5, unit: 'SECONDS'
          }

          if (!isHealthy) {
            // Get final health status for error message
            def finalStatus = bat(
              script: "docker inspect --format='{{.State.Health.Status}}' banking_api",
              returnStdout: true
            ).trim()
            error "banking-api container did not become healthy within ${timeout} seconds. Final status: ${finalStatus}"
          }
        }
      }
    }

    stage('Run Pytest') {
      steps {
        bat 'docker-compose exec -T banking-api pytest tests/test_banking_api.py --maxfail=1 --disable-warnings --tb=short'
      }
    }
  }

  post {
    always {
      echo 'Cleaning up containers...'
      bat 'docker-compose down || echo Container not found'
    }
  }
}