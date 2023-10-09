pipeline {
    agent {
        docker {
            // Use an official Python image
            image 'python:3.8' // Specify the desired Python version
        }
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout your code from Git
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install Selenium and WebDriver dependencies
                sh 'pip install selenium==3.141.0' // Specify the desired Selenium version
                sh 'pip install webdriver_manager'
            }
        }

        stage('Run Selenium Script') {
            steps {
                // Run your Selenium script
                sh 'python3 jenkins.py'
            }
        }
    }
}
