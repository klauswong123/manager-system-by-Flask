pipeline {
  agent any
  stages {
    stage('TRy') {
      steps {
        sh 'git config --global ghi.token e5b9be6f3a92af601f93006551651be2896c945b'
      }
    }

    stage('gitcon') {
      steps {
        sh 'ghi open -m "this is a new issue\\n a new issue"'
      }
    }

  }
  environment {
    Key = 'e5b9be6f3a92af601f93006551651be2896c945b'
  }
}