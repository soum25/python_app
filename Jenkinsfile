pipeline {
    
    environment{
        IMAGE_NAME="python_app"
        IMAGE_TAG="latest"
        IMAGE_REPO="soum25"
        STAGING="vafemoh1-staging"
        PRODUCTION="vafemoh1-production"
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
                        source app_venv/bin/activate  
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


        stage("Test"){
            steps{
               script {
                sh " pytest -v"
                    }
                }
            }

        stage("Clean container"){
            steps{
                sh """
                docker stop $IMAGE_NAME
                docker rm -f $IMAGE_NAME
                """
            }
        }

    }

}


