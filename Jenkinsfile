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
                    sh  'bash scripts/build_push.sh'
                }
            }







        }
}