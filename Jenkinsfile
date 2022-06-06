pipeline {

    environment{
        IMAGE_NAME="python_app"
        IMAGE_TAG="latest"
        IMAGE_REPO="soum25"
    }
    
    agent {
        docker { image 'python:3.8-slim-buster' }
    }
    stages{

        stage("Set up"){
            steps{
                script {
                    sh """
                        pip install -r requirements.txt
                        virtualenv app_venv
                        source app_venv/bin/activate  
                        """
                    }
                }
            }

        stage("Test"){
            steps{
               script {
                sh """
                    cd /tests
                    coverage run -m pytest -rap  --junitxml coverage.xml
                    """
                    }
                }
            }

        stage("Build image"){
            steps{
                script {
                    sh """
                    docker build -t ${IMAGE_REPO}/${IMAGE_NAME}:${IMAGE_TAG} .
                    """
                }
            }
        }

        stage("Run container based on build image"){
        steps{
            script {
                sh """
                docker run -d --name $IMAGE_NAME -p 70:5550 ${IMAGE_REPO}/${IMAGE_NAME}:${IMAGE_TAG}
                docker stop $IMAGE_NAME
                """
                    }
                }
            }

        stage("Clean container"){
            steps{
                sh """
                docker rm -f $IMAGE_NAME
                """
            }
        }

    }

}


