pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install dependencies and test') {
            steps {
                // Jenkins agent must have Python and pip available.
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements-dev.txt'
                bat 'python -m pytest -q'
            }
        }
        stage('Build Docker image') {
            steps {
                // Requires Docker CLI/Engine available to the Jenkins agent.
                bat 'docker build -t student-performance-mlops:latest .'
            }
        }
    }
    post {
        always {
            echo 'Pipeline finished. Review the test/build stage logs for the result.'
        }
    }
}
