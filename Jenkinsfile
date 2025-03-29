pipeline {
    agent any

    environment {
        IMAGE_NAME = "serjart/world_of_games"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/SergioArt-97/Devops-Experts-final-project.git'  // Update with your actual repository
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Run') {
            steps {
                sh '''
  docker run -d -p 8777:5000 --name word_of_games -v $WORKSPACE/Scores.txt:/Scores.txt $IMAGE_NAME
  while ! docker ps | grep -q word_of_games; do
    sleep 1
  done
'''

            }
        }

        stage('Test') {
            steps {
                script {
                    def testResult = sh(script: 'python3 e2e.py', returnStatus: true, returnStdout: true).trim()
                    if (testResult != 0) {
                        echo "Test Output: $testResult"
                        error("Test failed during the 'Test' stage. Stopping pipeline.")
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
                sh 'docker stop word_of_games'
                sh 'docker rm word_of_games'
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([string(credentialsId: 'dockerhub-token', variable: 'DOCKERHUB_TOKEN')]) {
                    sh 'docker tag $IMAGE_NAME $IMAGE_NAME:latest'
                    sh 'docker push $IMAGE_NAME:latest'
                }
            }
        }
    }
}
