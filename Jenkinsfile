pipeline{
        agent any
        environment{
            DOCKERHUB_CREDENTIALS = credentials("DOCKERHUB_CREDENTIALS")
            DATABASE_URI = credentials("DATABASE_URI")
        }

        stages{
        //     stage('Run Tests'){
        //         steps{
        //             sh  'bash scripts/unit_test.sh'
        //         }
        //     }
        
            stage('Build and Push'){
                steps{
                    sh  'bash scripts/build_push.sh'
                }
            }

            stage('Configure Ansible'){
                steps{
                    sh  'bash scripts/ansible_config.sh'
                }
            }

            stage('Deploy Application'){
                steps{
                    sh  'bash scripts/deploy.sh'
                }
            }



        }
}