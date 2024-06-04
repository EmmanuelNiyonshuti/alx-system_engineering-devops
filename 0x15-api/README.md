                        0x15. API
                        =========

                Background Context
                ------------------

        *Old-school system administrators usually only know Bash and that is what they use to build their scripts. While Bash is perfectly fine for a lot of things, it can quickly get messy and not efficient compared to other programming languages. The new generation of system administrators, usually called SREs, are pretty much regular software engineers but instead of building products, they are managing systems. And one of the big differences with their predecessors is that they know more than just Bash scripting.

        *One popular way to expose an application and dataset is to use an API. Often, they are the public facing part of websites and micro-services so that allow outsiders to interact with them – access and modify their data. In this project, you will access employee data via an API to organize and export them to different data structures.

        *This is a perfect example of a task that is not suited for Bash scripting, so let’s build Python scripts.

                Overview
                --------
        *In this project, I delved into REST APIs. An Application Programming Interface (API) is a way for two software systems to interact with each other. Representational State Transfer (REST) is an architectural style that defines a set of principles and constraints for creating web services. REST APIs, often referred to as RESTful APIs, adhere to these principles, making them lightweight, scalable, and easy to use.

                Project Details
                ---------------
        *In this project, I used the ``requests`` module in Python3 to interact with REST API endpoints. Specifically, one I worked with is the JSONPlaceholder API, a free online REST API that provides fake online REST endpoints for testing and prototyping
