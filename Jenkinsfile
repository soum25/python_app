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
                        source app_venv/bin/activate  
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


        stage("static code analysis with sonar"){
            steps{
               script {
                withSonarQubeEnv('sonarqube_server'){
                        sh """ ${scannerhome}/bin/sonar-scanner \
                        -Dsonar.projectKey=python_test_2 \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=http://192.168.6.132:9000 \
                        -Dsonar.login=3b478d7bc0ed48006b608f83128bb606ff5e679f
                        """
                        }
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


