pipeline{
    environment{
        IMAGE_NAME= "python_app"
        IMAGE_TAG= "latest"
        STAGING = "vafemoh_staging_app"
        PRODUCTION = "vafemoh_production_app"
    }
    agent none
    stages{
        stage("Build image"){
            agent any
            steps{
                script {
                    sh "docker build -t soum25/${IMAGE_NAME}:${IMAGE_TAG} ."
                }
            }
        }

        stage("Run container based on build image"){
        agent any
        steps{
            script {
                sh """
                docker run -d --name $IMAGE_NAME -p 70:5555 soum25/${IMAGE_NAME}:${IMAGE_TAG} 
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

         stage("Push image on staging and Deploy"){
             when {
                 expression { GIT_BRANCH == "origin/main" }
             }

            agent any
            environment{
               HEROKU_API_KEY = credentials('heroku_api_key')
             }
            steps{
                sh """
                
                heroku container:login
                heroku create $STAGING || echo " project already exist"
                heroku container:push -a $STAGING web
                heroku container:release -a $STAGING web
                
                """
            }
        }
    }

}
