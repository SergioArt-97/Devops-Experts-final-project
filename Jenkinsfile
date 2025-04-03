pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "serjart/world-of-games:latest"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                script {
                    sh '''
                        echo "Building Docker image..."
                        docker build -t ${DOCKER_IMAGE} .
                    '''
                }
            }
        }

        stage('Run App') {
            steps {
                script {
                    echo "Running Flask app in a container..."
                    sh '''
                        docker run -d -p 8777:8777 --name flask-game-app ${DOCKER_IMAGE}
                    '''
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    echo "Waiting for Flask app to be ready..."
                    // Wait for Flask app to be ready
                    for (i in 1..10) {
                        if (sh(script: 'curl -s http://localhost:8777', returnStatus: true) == 0) {
                            echo "Flask app is up!"
                            break
                        }
                        echo "Waiting..."
                        sleep 2
                    }

                    // Run the e2e tests
                    echo "Running end-to-end tests..."
                    sh "docker exec flask-game-app python /app/e2e.py"
                }
            }
        }

        stage('Clean up') {
            steps {
                script {
                    echo "Stopping and removing Docker container..."
                    sh '''
                        docker stop flask-game-app
                        docker rm flask-game-app
                    '''
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
