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

        stage('Debug') {
                steps {
                    script {
                        sh 'ls -l /home/jenkins/workspace/WorldOfGamesPipeline/Scores.txt'
                    }
                }
            }

        stage('Run') {
            steps {
                script {
                    try {
                        // Ensure any existing container is stopped and removed
                        sh """
                            docker stop ${CONTAINER_NAME} || true
                            docker rm ${CONTAINER_NAME} || true
                        """

                        // Ensure Scores.txt exists and is a file
                        sh """
                            if [ ! -f ${WORKSPACE}/Scores.txt ]; then
                                echo 'Scores.txt file not found in workspace!' && exit 1
                            fi
                        """

                        // Pull the latest image and run the new container
                        sh """
                            docker stop flask-game-app || true  # Stop container if already running
                            docker rm flask-game-app || true  # Remove existing container
                            docker pull serjart/world-of-games:latest
                            docker run -d --rm --name flask-game-app \
                            -p 8777:5000 \
                            -v ${WORKSPACE}/Scores.txt:/app/Scores.txt:ro \
                            serjart/world-of-games:latest
                        """
                    } catch (Exception e) {
                        echo "Error during docker run: ${e}"
                        currentBuild.result = 'FAILURE'
                        throw e
                    }
                }
            }
        }


        stage('Test') {
            steps {
                script {
                    sh '''
                        echo "Waiting for Flask app to be ready..."
                        for i in {1..10}; do
                            if curl -s http://localhost:8777 >/dev/null; then
                                echo "Flask app is up!"
                                break
                            fi
                            echo "Waiting..."
                            sleep 2
                        done
                    '''
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
