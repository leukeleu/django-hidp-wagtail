# HIdP Wagtail Sandbox

The HIdP Wagtail Sandbox project.

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
