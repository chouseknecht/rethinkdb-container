# rethinkdb-container 

[![Build Status](https://travis-ci.org/chouseknecht/rethinkdb-container.svg?branch=master)](https://travis-ci.org/chouseknecht/rethinkdb-container)

Adds a [rethinkdb](https://rethinkdb.com) service to your [Ansible Container](https://github.com/ansible-container) project.

To add the servcie to your project, simply do the following:

   ```
   # Set the working directory to your existing Ansible Container project
   $ cd myproject

   # Add the service  
   $ ansible-container install chouseknecht.rethinkdb-container 
   ```

## Requirements

- [Ansible Container](https://githbu.com/ansible-container)
- An existing Ansible Container project. Use the following to create a new project: 

    ```
    # Create an empty directory
    $ mkdir myproject

    # Change into the new empty directory
    $ cd myproject
  
    # Initialize the project with Ansible Container
    $ ansible-contianer init
    ```

## Role Variables

At present there are no role variables. The rethinkdb package is installed, and the service is executed with the defaut configuration.


## Dependencies

None.


## License

Apache v2

## Author Information

[@chouseknecht](https://github.com/chouseknecht)
