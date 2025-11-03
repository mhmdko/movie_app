pipeline {
  agent any

  triggers {
    // Check GitHub every 2 minutes for changes
    pollSCM('H/2 * * * *')
  }

  stages {

    stage('Checkout') {
      steps {
        git branch: 'main', url: 'https://github.com/mhmdko/movie_app.git'
      }
    }

    stage('Build Docker Image') {
      steps {
        bat '''
        echo Building Django image...
        docker build -t mydjangoapp:latest .
        echo Loading image into Minikube...
        minikube image load mydjangoapp:latest
        '''
      }
    }

    stage('Deploy to Minikube') {
      steps {
        bat '''
        echo Applying Kubernetes manifests...
        kubectl apply -f deployment.yaml
        kubectl apply -f service.yaml
        kubectl rollout status deployment/django-deployment
        '''
      }
    }

    stage('Verify Deployment') {
      steps {
        bat '''
        echo Checking running pods...
        kubectl get pods
        '''
      }
    }
  }
}
