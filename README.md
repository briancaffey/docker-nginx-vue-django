TODO:

[] run `pip freeze > requirements.txt` on the layer right after `pip install`. Do we need to do this? 

We might want specific versions for each package. We should 

[] figure out why docker is creating .pyc files locally. Ideally, docker will not do this.


## Environment variables

We want to separate env variables for local, staging, testing and production and perhaps for debugging, too. 


# S3 

Think about how the `sync_file_hashed` operation could be used for S3 resources in dev and prod

For local testing, we should probably not use S3 resource. Perhaps we should set up a folder that the system can use? Media? Nothing is actually stored there, but it exists and will be mounted, and can thus


## About the JWT

We want to obtain a base64 encoded token:

```
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTM4MzMwNTk5LCJlbWFpbCI6IiJ9.rIHFjBmbqBHnqKwCNlHenImMtQSmzFkbGLA8pddQ6AY
```

and then decode it using base64:


```json
{"typ":"JWT","alg":"HS256"}{"user_id":2,"username":"admin","exp":1538330599,"email":""}Ō稬6QޜY<P
```


```python

```


## Docker system pruning

If you have lots of untagged images, run the following command: 

```
docker rmi $(docker images -f "dangling=true"-q)
```

There could potentially be lots of these images, and when you run:

```
docker system prune
```

It doesn't show the images as they are being untagged and deleted, so it seems like the docker command is hanging. 

## A funky issue with __pycache__

I think the volume should be read only? Docker h

## NPM packages to install

- axios

- fontawesome

- highcharts

- tables