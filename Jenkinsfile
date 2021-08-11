pipeline{
        agent any
        environment{
            docker = credentials("docker")
        }

        stages{
            stage('Run Tests'){
                steps{
                    sh  'bash scripts/unit_test.sh'
                }
            }
        
            stage('Build and Push'){
                steps{
                    sh "docker login -u ${docker_USR} -p ${docker_PSW}"
                    sh  'bash scripts/build_push.sh'
                }
            }







        }
}