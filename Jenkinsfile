pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "serjart/world-of-games"
        DOCKER_TAG = "latest"
        COMPOSE_PROJECT_NAME = "worldofgames"  // for easier docker-compose management
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout scm
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    // Run the app and selenium containers in the background
                    sh "docker-compose up -d --build flask-app selenium"

                    // Optional: wait a bit for Flask app to boot
                    sh "sleep 5"

                    // Check container status
                    sh "docker-compose ps"
                }
            }
        }

        stage('Test') {
             steps {
                script {
                    sh 'docker-compose --verbose up --build --abort-on-container-exit --exit-code-from test test'
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    // Stop containers
                    sh "docker-compose down"

                    // Push image to Docker Hub
                    docker.withRegistry('', 'dockerhub-auth') {
                        sh "docker push ${DOCKER_IMAGE}:${DOCKER_TAG}"
                    }
                }
            }
        }
    }

    post {
        always {
            script {
                sh "docker system prune -f"
            }
        }
    }
}
