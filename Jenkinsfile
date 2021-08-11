pipeline{
        agent any
        environment{
            DOCKERHUB_CREDENTIALS = credentials("DOCKERHUB_CREDENTIALS")
        }

        stages{
            stage('Run Tests'){
                steps{
                    sh  'bash scripts/unit_test.sh'
                }
            }
        
            stage('Build and Push'){
                steps{
                    sh "docker login -u ${DOCKERHUB_CREDENTIALS_USR} -p ${DOCKERHUB_CREDENTIALS_PSW}"
                    sh  'bash scripts/build_push.sh'
                }
            }







        }
}