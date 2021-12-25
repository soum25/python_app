pipeline{
    environment{
        IMAGE_NAME="python_app"
        IMAGE_TAG="latest"
        IMAGE_REPO="soum25"
        STAGING="vafemoh1-staging"
        PRODUCTION="vafemoh1-production"
    }
    agent none
    stages{
        stage("Build image"){
            agent any
            steps{
                script {
                    sh "docker build -t ${IMAGE_REPO}/${IMAGE_NAME}:${IMAGE_TAG} ."
                }
            }
        }

        stage("Run container based on build image"){
        agent any
        steps{
            script {
                sh """
                docker run -d --name $IMAGE_NAME -p 70:5555 ${IMAGE_REPO}/${IMAGE_NAME}:${IMAGE_TAG} 
                docker ps -a
                sleep 7
                """
                    }
                }
            }

        stage("Test"){
        agent any
        steps{
            script {
                sh """
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
<<<<<<< HEAD

=======
>>>>>>> 527ab00488a7c072aa3ef12b19a24e0443ec37f9
