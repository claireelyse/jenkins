# Approval Gates

### Pausing the Pipeline for Approval:

1) When the pipeline reaches the input step, it pauses and waits for manual approval.
The pipeline cannot proceed until someone (a user with the required permissions) approves or rejects the request.

2) Parameters in the input Step:

- message: This is the prompt displayed to the user in the Jenkins UI, asking for approval. For example, "Do you approve deployment?"
- ok: This is the label for the confirmation button that will be shown in the UI. When clicked, the pipeline will proceed. For example, the button text could be "Deploy".
- submitter: This specifies which Jenkins users or groups are allowed to approve this step. You can list a username (e.g., admin) or leave it empty, allowing any user with appropriate access to approve.

3) How It Works:

The pipeline runs the earlier stages (e.g., building code).
When it reaches the Approval Gate stage, the pipeline stops, and Jenkins displays the approval request in the UI.
The specified submitter (or any allowed user) must manually approve the step for the pipeline to continue.
Once approved, the pipeline moves to the next stage (e.g., deployment).

4) Add a timeout. 

If an approver does not approve the pipeline then it will wait indefinitely unless specified otherwise. If the approval is not given within the specified time, the pipeline will proceed to the next action (which can be an error, a failure, or skipping deployment). In our example we want the Pipeline to abort if not approved in 10 mins.

### Add an approval step to the Pipeline
This will stop the Pipeline for manual approval from the "admin" user. In the Jenkins GUI there will be a button that has the label "Deploy". 
```Yml
        stage('Approval Gate') {
            steps {
                // Timeout block for the input step
                timeout(time: 10, unit: 'MINUTES') {  // Waits for 10 minutes for approval
                    // Manual approval step
                    input message: 'Do you approve deployment?', ok: 'Deploy', submitter: 'admin'
            }
        }

        # insert Pipeline steps if approved

        post {
            // Fail the job if the input timeout is reached
            aborted {
                echo 'Approval was not granted in time. Failing the job.'
                error('Job failed due to lack of approval.')
            }
        }
```