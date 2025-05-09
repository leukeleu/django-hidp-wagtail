# Hidp Wagtail Sandbox

The Hidp Wagtail Sandbox project.

## Development

See [docker/README.md](docker/README.md)

### Git hooks

This project contains two git hooks:

1. `pre-commit` runs linting in the backend.
2. `pre-push` runs linting in the backend.

To enable the hooks, run the following command:

```shell
make install-git-hooks
```

This will create symbolic links to the hooks in the `.git/hooks` directory.

## Releasing

This project is released using GitHub Actions.

To create a new release, follow these steps:

1. Make sure `@leukeleu/contributors` and `leukeleu-bot` can access the repository.
   <https://github.com/leukeleu/hidp_wagtail_sandbox/settings/access>

2. Make sure the project is configured in [leukeleu-ansible](https://github.com/leukeleu/leukeleu-ansible/).
   If not, use the [new-host workflow in leukeleu-ansible][1] to configure the project.

3. Make sure the secret [`DEPLOYER_ACCESS_TOKEN`][2] is available to the repository.
   (Note: Admin privileges are required to configure this secret, ask a colleague if you cannot access it.)

4. Make sure the PR from step 2 is merged, then create a new release by running
   the [release workflow][3].

[1]: https://github.com/leukeleu/leukeleu-ansible/actions/workflows/new-host.yml
[2]: https://github.com/organizations/leukeleu/settings/secrets/actions/DEPLOYER_ACCESS_TOKEN
[3]: https://github.com/leukeleu/hidp_wagtail_sandbox/actions/workflows/release.yml

## Sentry

Staging and live environments should be monitored by Sentry.

Configure the `sentry_dsn` and `sentry_environment` settings in
[leukeleu-ansible](https://github.com/leukeleu/leukeleu-ansible/).

Find the correct `sentry_dsn` for this project here:

<https://sentry.io/settings/leukeleu/projects/hidp_wagtail_sandbox/keys/>

Or, if this is a new project, create a new Sentry project here:

<https://sentry.io/organizations/leukeleu/projects/new/>

### Client-Side Sentry

The base template (`frontend/templates/base.html`) is configured to report
client side errors to Sentry when `sentry_dsn` and `sentry_environment`
are set.
