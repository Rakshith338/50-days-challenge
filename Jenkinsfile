pipeline {
	agent any
		
	stages{
		stage (enter the repo){
			steps{
				git branch: 'main',
					credentialsId: '63aa5507-7c81-4242-898f-459afae51c5f'
					url: 'https://github.com/Rakshith338/50-days-challenge.git'
			}
		}
		stage(list workspace files) {
			steps{
				sh 'ls -ls'
			}
		}
		stage('Run python') {
			steps{
				sh 'python3 day2.py'
			}
		}

	}
}