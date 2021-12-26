pipeline {
    agent {
        docker { image 'python:3.8-slim-buster' }
    }
    stages{

        stage("Set up"){
            agent any
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



        stage("Build image"){
            agent any
            steps{
                script {
                    sh """
                    source app_venv/bin/activate
                    docker build -t ${IMAGE_REPO}/${IMAGE_NAME}:${IMAGE_TAG} .
                    """
                }
            }
        }

        stage("Run container based on build image"){
        agent any
        steps{
            script {
                sh """
                source app_venv/bin/activate
                docker run -d --name $IMAGE_NAME -p 70:5550 ${IMAGE_REPO}/${IMAGE_NAME}:${IMAGE_TAG}
                docker stop $IMAGE_NAME
                """
                    }
                }
            }


        stage("Test"){
            agent any
            steps{
               script {
                sh """
                source app_venv/bin/activate
                docker restart $IMAGE_NAME
                sleep 7
                curl -I 192.168.6.132:70
                curl -I 172.17.0.1:70

                """
                    }
                }
            }

        stage("Clean container"){
            agent any
            steps{
                sh """
                docker stop $IMAGE_NAME
                docker rm -f $IMAGE_NAME
                """
            }
        }

    }

}

