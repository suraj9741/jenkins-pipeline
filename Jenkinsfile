pipeline{
    agent any
    stages{
        stage('pull code'){
            steps{
                git branch: 'main', url: 'https://github.com/suraj9741/jenkins-pipeline.git'
            }
        }
        stage('build and push'){
            steps{
                ansiblePlaybook become: true, credentialsId: 'private-key', disableHostKeyChecking: true, installation: 'ansible', inventory: 'ansible/server_setup/hosts', playbook: 'ansible/server_setup/server_setup.yml'
            }
        }
    }
}