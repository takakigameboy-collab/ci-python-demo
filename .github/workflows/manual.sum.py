echo "# Test2" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/takakigameboy-collab/Test2.git
git push -u origin main

    # Steps represent a sequence of tasks that will be executed as part of the job
     steps:
    # Runs a single command using the runners shell
      name: Send greeting
      run: echo "Hello ${{ inputs.name }}"
    # Runs a single command using the runners shell
    - name: Send greeting
      run: echo "Hello ${{ inputs.name }}"
