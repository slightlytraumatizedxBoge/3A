name: Task3
on: push
jobs:
    T1:
        runs-on: ubuntu_latest
        steps:
           - name: my-steps
             run: echo "Hello"
    
