# auth-with-email-code-validation
This repo will be implementing basic authentication API. Each account will have to be validated with code sent via email by our server.

To simulate email validation process please find below the mailtrap credentials:

* usr: codesnobility@gmail.com 
* psswd: -%nubs_-2A7Hs6X

Once connected click:
* Sandbox > inboxes


Build image & compose
# docker-compose up -d

Restart container
# docker restart <container-id> or <container-name>

Rebuild
# docker-compose build --no-cache

Delete image
# docker image rm <image-id>

# docker inspect <container-id>

# docker exec -it <container-id> sh

#docker-compose up --build
