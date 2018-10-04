# Documentation

## Gitlab

By including `.gitlab-ci.yml` in our base directory, we trigger the GitLab CI/CD process. It is currently failing because it can't find `db`. When settings `DATABASES` in `settings.py`, we should set the database conditionally if it picks up a certain variable in the CI runner. 