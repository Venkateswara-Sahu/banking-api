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
          while (System.currentTimeMillis() - startTime < timeout * 1000) {
            def result = bat(
              script: "docker inspect --format='{{.State.Health.Status}}' banking_api",
              returnStatus: true
            ).trim()
            if (result == "healthy") {
              echo "banking-api container is healthy!"
              break
            }
            echo "Waiting for banking-api container to become healthy (current status: ${result})..."
            sleep time: 5, unit: 'SECONDS'
          }
          if (bat(script: "docker inspect --format='{{.State.Health.Status}}' banking_api", returnStatus: true).trim() != "healthy") {
            error "banking-api container did not become healthy within ${timeout} seconds"
          }
        }
      }
    }

    stage('Run Pytest') {
      steps {
        bat 'docker-compose exec -T banking_api pytest tests/test_banking_api.py --maxfail=1 --disable-warnings --tb=short'
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
