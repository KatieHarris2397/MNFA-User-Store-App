# MNFA-User-Store-App
A simple user storing app to demonstrate a MongoDB-Neo4j-FastAPI-Angular Stack

## Getting Started

NOTICE: This repository includes mutiple Github actions workflows that builds and pushes the project's Docker images to the Github Container Registry (GHCR). 

1. **Fork this repository**
2. **Navigate to the 'Actions' tab at the top of the repository**
3. **Select the 'Build and Push MNFA Docker Images to GHCR (initialization purposes only)' action on the left**
4. **Click 'Run workflow' on the right and click the button that says 'Run workflow'**
  This will start the Github actions workflow to build, tag and push the Docker images for this repostory to your Github Container Registry
5. **Clone the repository**:
   ```bash
   git clone <Github-repository-URL>
   cd MNFA-User-Store-App
   ```
6. **Navigate to Nexlayer folder and open nexlayer-template.yaml in your favorite editor**:
   ```bash
   cd Nexlayer
   vi nexlayer-template.yaml
   ```
7. **Update registryLogin information to be your own**
8. **Update database pod tag to reference Mongo Docker image created by Github actions workflow**
9. **Update fastAPI pod tag to reference FastAPI Docker image created by Github actions workflow**
10. **Update nginx pod tag to reference Angular Docker image created by Github actions workflow**
11. **Submit Template to Nexlayer**

## Updating this repository and building new images

NOTICE: You will need to tag the commit you would like the images built for to start the Github actions workflow

1. **After creating the commit with the changes you would like built into Docker images, tag the commit with the name of the tag you would like to give your Docker images**:
  ```bash
  git tag <tag-name>
  ```
2. **Push the commit and tag to the remote repository** (this will start the Github actions workflow):
  ```bash
  git push origin <branch name> <tag-name>
  ```
3. **View your new Docker images under the Packages tab when you click on your user profile**
