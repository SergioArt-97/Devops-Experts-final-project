pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "serjart/world-of-games"
        DOCKER_TAG = "latest"
        CONTAINER_NAME = "flask-game-app"
        SCORE_FILE_PATH = "/app/Scores.txt"
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Make sure SCM repository is checked out
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
                    sh """
                        docker pull serjart/world-of-games:latest  # Always pull the latest image
                        docker run -d --rm --name flask-game-app \
                        -p 8777:5000 \
                        -v ${WORKSPACE}/Scores.txt:/app/Scores.txt \
                        serjart/world-of-games:latest
                    """
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sleep(5)  // Wait a few seconds to ensure Flask app is up
                    sh "python e2e.py"
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    sh "docker stop ${CONTAINER_NAME}"
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
