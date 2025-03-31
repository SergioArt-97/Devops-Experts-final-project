pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "your-dockerhub-username/word-of-games"
        DOCKER_TAG = "latest"
        CONTAINER_NAME = "flask-game-app"
        SCORE_FILE_PATH = "/app/Scores.txt"
    }

    stages {
        // Checkout the repository
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        // Build the Docker image
        stage('Build') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
                }
            }
        }

        // Run the Docker container
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

        // Run tests using e2e.py
        stage('Test') {
            steps {
                script {
                    // Wait a few seconds to ensure the Flask app is running
                    sleep(5)

                    // Run Selenium end-to-end tests
                    sh "python e2e.py"

                    // If the test fails, mark the pipeline as failed
                }
            }
        }

        // Finalize: Stop container and push to DockerHub
        stage('Finalize') {
            steps {
                script {
                    // Stop the running container
                    sh "docker stop ${CONTAINER_NAME}"

                    // Push the image to DockerHub
                    docker.withRegistry('', 'dockerhub-credentials') {
                        sh "docker push ${DOCKER_IMAGE}:${DOCKER_TAG}"
                    }
                }
            }
        }
    }

    post {
        always {
            script {
                // Clean up unused Docker resources
                sh "docker system prune -f"
            }
        }
    }
}
