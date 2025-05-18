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
        bat 'timeout /t 10' // Wait a bit for the container to be ready
      }
    }

    stage('Run Pytest') {
      steps {
        bat 'pip install -r requirements.txt'
        bat 'pip install pytest'
        bat 'pytest tests/test_banking_api.py --maxfail=1 --disable-warnings --tb=short'
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
