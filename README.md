# Google Auth Webapp

This repository contains a django webapp which implements a microservice to handle the university
authentication of GSuite.

## Documentation

The project has [detailed documentation](https://uisautomation.github.io/gauth-webapp/) for
developers, including a "getting started" guide.

## Developer quickstart

Firstly, [install docker-compose](https://docs.docker.com/compose/install/).

Then, most tasks can be performed via the ``compose.sh`` script:

```bash
# Start development server
$ ./compose.sh development

# Start development server in background
$ ./compose.sh development up -d

# View logs
$ ./compose.sh development logs

# Stop the development server
$ ./compose.sh development down

# Run tests
$ ./compose.sh tox run --rm tox

# Start a server using the production Docker image
$ ./compose.sh production build
$ ./compose.sh production up -d
$ ./compose.sh production exec production_app ./manage.py migrate
```

Additionally the ``tox.sh`` and ``manage_development.sh`` wrapper scripts
provide convenient ways to run ``tox`` and management commands:

```bash
# Rebuild all testenvs
$ ./tox.sh -r

# Run only the flake8 tests
$ ./tox.sh -e flake8

# Run the migrate management command using the development images
$ ./manage_development.sh migrate

# Run tests and write coverage/documentation to build directory
$ ./compose.sh tox run -v $PWD:/tmp/workspace -e TOXINI_ARTEFACT_DIR=/tmp/workspace/build --rm tox
```

## Copyright License

See the [LICENSE](LICENSE) file for details.
