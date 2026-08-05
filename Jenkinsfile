pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Rakshith338/50-days-challenge.git'
            }
        }

        stage('List Workspace Files') {
            steps {
                sh 'ls -la'
            }
        }

        stage('Run Python') {
            steps {
                sh 'python3 day2.py'
            }
        }
    }
}