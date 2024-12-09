# What is `docker-compose` ?

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/HUpIoF_conA/0.jpg)](https://www.youtube.com/watch?v=HUpIoF_conA)

There are many images in docker, and in real world application, we want to use different services/images

Why we may want to use serparate services?

<img src="https://raw.githubusercontent.com/paulc4/microservices-demo/master/shopping-system.jpg" height=300/>

Here are some key reasons for using separate services in Docker Compose for your application, summarized in one line each:

1. Modularity: Each service can be developed, tested, and deployed independently, promoting a modular architecture.
2. Scalability: Services can be scaled independently based on demand, allowing for efficient resource management.
3. Isolation: Each service runs in its own container, providing isolation and reducing the risk of conflicts between dependencies.
4. Maintainability: Smaller, focused services are easier to maintain and update without affecting the entire application.
5. Flexibility: Different services can use different technologies or programming languages, allowing for a polyglot architecture.
6. Fault Tolerance: If one service fails, it does not necessarily bring down the entire application, improving overall reliability.
7. Simplified Networking: Docker Compose automatically sets up a network for services to communicate, simplifying inter-service communication.
8. Environment Consistency: Each service can have its own environment variables and configurations, ensuring consistent behavior across different environments.
9. Easier Collaboration: Teams can work on different services simultaneously without stepping on each other's toes, enhancing collaboration.

Here is a basic `docker-compose.yaml` file:

```Docker
version: '2'

services:
  database:
    image: postgres

  webserver:
    image: nginx
    ports:
      - "8080:80"
```

**Note**: ports - "8080:80" means expose the server port 80 to 8080 port

# Understanding `docker compose up`

The `docker compose up` command is used to create and start containers defined in a Docker Compose file (`docker-compose.yml`). Here’s a breakdown of what this command does:

## How to Start/Run Docker Images

Once the images are built or pulled (the images need to be either built from a Dockerfile or pulled from a registry before they can be run), you can run the Docker containers (not just images) using the `docker compose up` command. This command simplifies the process of starting and managing multi-container applications defined in a single configuration file.

### Key Functions of `docker compose up`

1. **Reads the Configuration**:

   - The command reads the `docker-compose.yml` file in the current directory to understand the services, networks, and volumes defined in the configuration.

2. **Builds Images (if necessary)**:

   - If the services defined in the Compose file specify a `build` context (i.e., a Dockerfile), `docker compose up` will build the images before starting the containers. If the images are already built and up to date, this step is skipped.

3. **Creates Containers**:

   - It creates containers for each service defined in the Compose file. If a container for a service already exists, it will be reused unless the configuration has changed.

4. **Starts Containers**:

   - The command starts the containers in the order defined by the `depends_on` option, ensuring that any dependencies are started first. For example, if a web server depends on a database, the database container will start before the web server.

5. **Attaches to Logs**:

   - By default, `docker compose up` attaches to the logs of the containers, allowing you to see the output in real-time. You can stop the logs by pressing `Ctrl + C`.

6. **Runs in Detached Mode (optional)**:

   - You can run `docker compose up` in detached mode by adding the `-d` flag (i.e., `docker compose up -d`). This starts the containers in the background and returns control to the terminal, allowing you to continue using it while the containers run.

7. **Creates Networks and Volumes**:
   - If the Compose file defines networks or volumes, `docker compose up` will create them as needed. This allows the containers to communicate with each other and persist data.

### Example Usage

```
docker compose up
```

- This command will start all the services defined in the `docker-compose.yml` file, build images if necessary, and attach to their logs.

```
docker compose up -d
```

- This command will start all the services in detached mode, running them in the background.

## Summary

The `docker compose up` command is a powerful tool for managing multi-container applications. It simplifies the process of starting and managing services, handling dependencies, and providing a unified way to run applications defined in a single configuration file.
