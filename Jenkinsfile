pipeline {
    agent any

    stages {
        stage('Clean Workspace') {
            steps {
                deleteDir()
            }
        }

        stage('Preparar') {
            steps {
                bat 'python -m pip install pandas'
                bat 'python -m pip install openpyxl'
            }
        }

        stage('READ DATA') {
            steps {
                bat 'python scripts/data_read.py'
            }
        }

        stage('TRANSFORM DATA') {
            steps {
                bat 'python scripts/data_transform.py'
            }
        }

        stage('EXPORT DATA') {
            steps {
                bat 'python scripts/data_export.py'
            }
        }
    }

    post {
        success {
            emailext(
                subject: "Pipeline ejecutado correctamente",
                body: "El pipeline de datos Uber Peru 2010 se ejecutó correctamente.",
                to: "luistest2431@gmail.com"
            )
        }

        failure {
            emailext(
                subject: "Error en pipeline",
                body: "El pipeline de datos Uber Peru 2010 falló. Revisar Jenkins.",
                to: "luistest2431@gmail.com"
            )
        }
    }
}