## django.db.utils.OperationalError: could not translate host name "db" to address: Name or service not known

https://gitlab.com/gitlab-org/gitlab-runner/issues/2166

```
image: docker:latest

stages:
  - build
  - test
  - release

variables:
  CONTAINER_TEST_IMAGE: mygitlab.com:4567/jonas/rails-ci-test:$CI_BUILD_REF_NAME
  CONTAINER_RELEASE_IMAGE: mygitlab.com:4567/jonas/rails-ci-test:latest
  POSTGRES_DB: db
  POSTGRES_USER: jonas
  POSTGRES_PASSWORD: ""
  POSTGRES_HOST: postgres

build:
  stage: build
  script:
    - docker login -u gitlab-ci-token -p $CI_BUILD_TOKEN mygitlab.com:4567
    - docker build --pull -t $CONTAINER_TEST_IMAGE .
    - docker push $CONTAINER_TEST_IMAGE

rails-test:
  stage: test
  image: mygitlab.com:4567/jonas/rails-ci-test:$CI_BUILD_REF_NAME
  services:
    - postgres:latest
  script:
    - rails test

release-image:
  stage: release
  script:
    - docker login -u gitlab-ci-token -p $CI_BUILD_TOKEN mygitlab.com:4567
    - docker pull $CONTAINER_TEST_IMAGE
    - docker tag $CONTAINER_TEST_IMAGE $CONTAINER_RELEASE_IMAGE
    - docker push $CONTAINER_RELEASE_IMAGE
  only:
    - master
```