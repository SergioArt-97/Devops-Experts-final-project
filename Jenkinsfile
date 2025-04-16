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
                    sh "docker-compose up -d --build"

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
                    echo "Waiting for Selenium to be ready..."
                    sh '''
                        for i in {1..10}; do
                            if curl -s http://localhost:4444/wd/hub/status | grep -q '"ready":true'; then
                                echo "Selenium is ready!"
                                break
                            fi
                            echo "Waiting for Selenium..."
                            sleep 2
                        done
                    '''

                    def result = sh(script: '''
                        . /home/jenkins/venv/bin/activate
                        python3 e2e.py
                    ''', returnStatus: true)

                    echo "Test result: ${result}"
                    if (result != 0) {
                        error "Test failed with exit code ${result}"
                    }
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
