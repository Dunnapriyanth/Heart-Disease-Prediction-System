pipeline {
  agent { label 'master' }
  stages {
    stage('Source') { // Get code
      parallel {
        stage('Project-1') {
            steps {
                echo "Checkout Project-1"
            }
        }
        stage('Project-2') {
            steps {
                echo "Checkout Project-2"
            }
        }
      }  
      
    }
    stage('Compile') { // Compile and do unit testing
      steps {
        echo "Compile the Source Code"
      }
    }
    stage('Run') {
        // run Gradle to execute compile and unit testing
      steps {
          echo "Run the Source Code"
        }
     }
   }
 }
