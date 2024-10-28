# Conditional Logic

there are two main types of Conditional logic in Jenkins pipelines

1) Declarative Pipeline (when):
You can define conditions for whether a stage should be executed using the when block. 

2) Scripted Pipeline (if-else):
Using script {} block, you can introduce custom conditional logic like if-else to check the branch or any other environment variables.

### Declarative

The Deploy stage runs only when the branch is main, thanks to the when condition. Here’s an example:
```Yml
stage('Deploy') {
    when {
        branch 'main'  // This stage runs only if the branch is 'main'
    }
    steps {
        echo 'Deploying...'
    }
}
```

### If-else 
In scripted pipelines, you can use traditional if-else logic within script blocks to control which steps to run.

```Yml
stage('Conditional Deployment') {
    steps {
        script {
            if (env.BRANCH_NAME == 'main') {
                echo 'Deploying to production'
            } else {
                echo 'Skipping deployment'
            }
        }
    }
}
```